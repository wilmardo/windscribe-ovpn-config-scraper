#!/usr/bin/python

import sys
import re
import requests
from bs4 import BeautifulSoup

# https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/#retry-on-failure
retry_strategy = requests.packages.urllib3.util.retry.Retry(
    total=10,
    status_forcelist=[403],
    allowed_methods=["POST"],
    backoff_factor=2
)

adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

headers = {
    'authority': 'nld.windscribe.com',
    'cache-control': 'max-age=0',
    'origin': 'https://nld.windscribe.com',
    'upgrade-insecure-requests': '1',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'referer': 'https://nld.windscribe.com/getconfig/openvpn',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': sys.argv[1]
}

# Parse optgroup containing the locations
content = http.get('https://windscribe.com/getconfig/openvpn', headers=headers)
soup = BeautifulSoup(content.text, 'html.parser')
optgroup = soup.optgroup

for location in optgroup.find_all('option'):
    for protocol in ["tcp", "udp"]:
            data = {
                'location': location.attrs['value'],
                'protocol': protocol,
                'port': '1194',
                'version' : '3b'  # openvpn 2.4.6 or newer
            }
            response = http.post('https://windscribe.com/getconfig/openvpn', headers=headers, data=data)

            filename = f"exports/{location.string.replace(' ', '')}-{protocol}.ovpn"
            f = open(filename, "w")
            f.write(response.text)
            print(f"Grabbed {filename}")
