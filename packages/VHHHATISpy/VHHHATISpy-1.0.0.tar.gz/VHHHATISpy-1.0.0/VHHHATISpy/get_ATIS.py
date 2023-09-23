import requests
import random
from bs4 import BeautifulSoup

# def get_ATIS() -> dict:
#     return {'a':1}


USER_AGENTS = [
    'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)', 
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
]
URL = "https://atis.cad.gov.hk/ATIS/ATISweb/atis.php"
USER_AGENT = random.choice(USER_AGENTS) 
HEADERS = {'User-Agent': USER_AGENT}

def _remove_br_in_raw(r:list) -> list:
    """
    remove the "<br/>" in the list
    return list
    """
    return list(filter(lambda x:isinstance(x, str), r))

def get_ATIS() -> dict:
    """
    return ATIS_dict = {
        'Arrival': str,
        'Departure': str
    }
    """
    response = requests.post(URL, headers=HEADERS)
    # print(f"Fetch status: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    raw_arr = soup.find('div', class_="data_name_arr")
    raw_arr_list = _remove_br_in_raw(raw_arr.contents)
    arrival_ATIS = '\n'.join(raw_arr_list[:-1]) # skip "ACKNOWLEDGE INFO (?) ON FIRST CTC WITH APP."

    raw_dep = soup.find('div', class_="data_name_dep")
    raw_dep_list = _remove_br_in_raw(raw_dep.contents)
    departure_ATIS = '\n'.join(raw_dep_list[:-1])    # skip "ACKNOWLEDGE INFO (?) ON FIRST CTC WITH DELIVERY."

    # # print result
    # print("======== get ATIS Result ========")
    # print('ARRIVAL:')
    # print(arrival_ATIS)
    # print()
    # print('DEPARTURE:')
    # print(departure_ATIS)

    # res
    ATIS_dict = {
        'Arrival': arrival_ATIS,
        'Departure': departure_ATIS
    }
    return ATIS_dict