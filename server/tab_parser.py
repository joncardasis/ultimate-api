import sys
import json
import requests
from .parser import html_tab_to_json_dict

def dict_from_ultimate_tab(url: str) -> json:
    '''
    Given a Ultimate Guitar tab url, will return a dictionary representing the
    song along with the song info
    '''
    html = requests.get(url).content
    ug_tags = ['js-tab-content', 'js-copy-content'] # tags the tabs are contained in
    tab_dict = html_tab_to_json_dict(html, ug_tags)
    return tab_dict


def json_from_ultimate_tab(url: str) -> json:
    '''
    Given a Ultimate Guitar tab url, will return a json object representing the
    song along with the song info
    '''
    tab_dict = dict_from_ultimate_tab(url)
    data = json.dumps(tab_dict, ensure_ascii=False)
    return data


if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except:
        print('INCORRECT USAGE\n')
        print('  Usage:')
        print('    python %s {url}' % sys.argv[0])
        sys.exit()

    json_data = json_from_ultimate_tab(url)

    pretty_format_json = json.dumps(json.loads(json_data), indent=4, sort_keys=True)
    print(pretty_format_json)
