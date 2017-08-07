import json
from bs4 import BeautifulSoup
from .tab import UltimateTab, UltimateTabInfo
import re

def _tab_info_from_soup(soup: BeautifulSoup) -> UltimateTabInfo:
    '''
    Returns a populated UltimateTabInfo object based on the provided soup.
    Parses based on UG site construction as of 9/3/17.

    Parameters:
        - soup: A BeautifulSoup for a Ultimate Guitar tab's html (or html body)
    '''
    # Get song title and artist
    try:
        song_title = soup.find(attrs={'itemprop': 'name'}).text
        song_title = re.compile(re.escape('chords'), re.IGNORECASE).sub(r'', song_title).strip() # Remove the word 'chords'
    except:
        song_title = "UNKNOWN"

    try:
        artist_name = soup.find(attrs={'class': 't_autor'}).text.replace('\n', '')
        artist_name = re.compile(re.escape('by'), re.IGNORECASE).sub(r'', artist_name).strip()# Remove the word 'by'
    except:
        artist_name = "UNKNOWN"

    # Get info - author, capo, tuning, etc.
    author = "UNKNOWN"
    difficulty = None
    key = None
    capo = None
    tuning = None
    try:
        info_header_text = soup.find(attrs={'class': 't_dt'}).text.replace('\n', '')
        info_headers = [x.lower() for x in info_header_text.split(' ') if x] # Split string and make lowercase
        info_header_values = soup.findAll(attrs={'class': 't_dtde'})

        for index, header in enumerate(info_headers):
            try:
                if header == 'author':
                    author = info_header_values[index].a.text
                elif header == 'difficulty':
                    difficulty = info_header_values[index].text.strip()
                elif header == 'key':
                    key = info_header_values[index].text.strip()
                elif header == 'capo':
                    capo = info_header_values[index].text.strip()
                elif header == 'tuning':
                    tuning = info_header_values[index].text.strip()
            except:
                continue
    except:
        pass

    tab_info = UltimateTabInfo(song_title, artist_name, author, difficulty, key, capo, tuning)
    return tab_info


def html_tab_to_json_dict(html_body: str, pre_class_tags: [str]) -> json:
    '''
    Returns a json form of a 'pre' tag in an untimate guitar html tabs body.

    Parameters:
        - html_body: The full html body of an ultimate guitar tab site
        - pre_class_tags: An array of strings for the class names of a 'pre' tag where the chords are located to parse
    '''
    soup = BeautifulSoup(html_body, "html.parser")

    # Get UltimateTabInfo object from soup html for artist, title, etc.
    tab_info = _tab_info_from_soup(soup)

    # Get tab's content from html (lyrics + chords)
    tabs_html_content = soup.find('pre', attrs={'class': pre_class_tags})

    # Strip `pre` tag and convert to string to parse
    formatted_tab_string = ''.join(map(str, tabs_html_content.contents))

    # Parse each line of the string into json
    tab = UltimateTab()
    for tab_line in formatted_tab_string.split('\n'):
        re_span_tag = re.compile(r'<span[^>]*>|<\/span[^>]*>')

        if not tab_line: # Line is blank
            tab.append_blank_line()
        elif re_span_tag.search(tab_line): # Line contains chords
            sanitized_tab_line = re_span_tag.sub(r' ', tab_line)
            tab.append_chord_line(sanitized_tab_line)
        else: # Line contains lyrics/string
            #tab_line = tab_line.encode('ascii', 'replace') # Encode as ascii
            tab.append_lyric_line(tab_line)

    # Construct full json object
    json = {
        'title': tab_info.title,
        'artist_name': tab_info.artist,
        'author': tab_info.author
    }

    # add tab info if it exists
    if tab_info.difficulty is not None:
        json['difficulty'] = tab_info.difficulty
    if tab_info.key is not None:
        json['key'] = tab_info.key
    if tab_info.capo is not None:
        json['capo'] = tab_info.capo
    if tab_info.tuning is not None:
        json['tuning'] = tab_info.tuning

    json['lines'] = tab.as_json_dictionary()['lines']

    # Return constructed json under a single tag
    return {'tab': json}
