#!/usr/bin/env python3

import json
import urllib.request

with urllib.request.urlopen("https://ipv4.geojs.io/v1/ip/geo.json") as url:
    data = json.loads(url.read().decode())
    str = " " + data['ip'] + " (" + data['city'] + ", " + data['country_code'] + ")"
    print(str, end='')
