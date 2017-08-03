import requests
import json
from parser import html_tab_to_json_dict
import sys

def json_from_ultimate_tab(url: str) -> json:
    '''
    Given a Ultimate Guitar tab url, will return a json object representing the
    song along with the song info
    '''
    html = requests.get(url).content
    ug_tags = ['js-tab-content', 'js-copy-content'] # tags the tabs are contained in
    tab_dict = html_tab_to_json_dict(html, ug_tags)
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

    print(json_data)
    with open("data.json", "w") as file:
         file.write(json_data)
