#!/usr/bin/python

import requests
import time
import sys

values = {
        "65-US Central": "US Central",
        "1-US East": "US East",
        "4-US West": "US West",
        "91-WINDFLIX US": "WINDFLIX US",
        "7-Canada East": "Canada East",
        "63-Canada West": "Canada West",
        "69-Austria": "Austria",
        "75-Belgium": "Belgium",
        "74-Bulgaria": "Bulgaria",
        "97-Croatia": "Croatia",
        "70-Czech Republic": "Czech Republic",
        "62-Denmark": "Denmark",
        "99-Estonia": "Estonia",
        "73-Finland": "Finland",
        "21-France": "France",
        "16-Germany": "Germany",
        "84-Greece": "Greece",
        "71-Hungary": "Hungary",
        "80-Iceland": "Iceland",
        "58-Ireland": "Ireland",
        "79-Israel": "Israel",
        "55-Italy": "Italy",
        "76-Latvia": "Latvia",
        "90-Lithuania": "Lithuania",
        "83-Moldova": "Moldova",
        "13-Netherlands": "Netherlands",
        "48-Norway": "Norway",
        "68-Poland": "Poland",
        "92-Portugal": "Portugal",
        "45-Romania": "Romania",
        "94-Slovakia": "Slovakia",
        "51-Spain": "Spain",
        "24-Sweden": "Sweden",
        "33-Switzerland": "Switzerland",
        "100-Tunisia": "Tunisia",
        "10-United Kingdom": "United Kingdom",
        "93-WINDFLIX UK": "WINDFLIX UK",
        "102-Albania": "Albania",
        "82-Azerbaijan": "Azerbaijan",
        "56-India": "India",
        "42-Russia": "Russia",
        "104-Serbia": "Serbia",
        "103-Slovenia": "Slovenia",
        "66-South Africa": "South Africa",
        "60-Turkey": "Turkey",
        "77-Ukraine": "Ukraine",
        "30-Australia": "Australia",
        "67-New Zealand": "New Zealand",
        "23-Hong Kong": "Hong Kong",
        "87-Indonesia": "Indonesia",
        "39-Japan": "Japan",
        "78-Malaysia": "Malaysia",
        "98-Philippines": "Philippines",
        "36-Singapore": "Singapore",
        "59-South Korea": "South Korea",
        "85-Thailand": "Thailand",
        "81-Vietnam": "Vietnam",
        "89-Argentina": "Argentina",
        "64-Brazil": "Brazil",
        "96-Colombia": "Colombia",
        "54-Mexico": "Mexico"
}

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

for key, value in values.items():
        for proto in ["tcp", "udp"]:
                data = {
                  'location': key,
                  'protocol': proto,
                  'port': '1194',
                  'cipher': 'cbc'
                }

                filename = "{name}-{protocol}.ovpn".format(
                        name=value.replace(' ', '-'),
                        protocol=proto
                )
                time.sleep(5)
                response = requests.post('https://nld.windscribe.com/getconfig/openvpn', headers=headers, data=data)
                f = open(filename, "w")
                f.write(response.text)
