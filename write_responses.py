import os
import json
import requests

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

years = range(2000, 2020)

for year in years:
    for state in states:
        if not os.path.exists(state):
            os.makedirs(state)
        os.chdir(state)
        url = "http://127.0.0.1:8000/api/v1/election/?format=json&limit=0&state__postal=%s&start_date__year=%s" % (state, year)
        r = requests.get(url)
        with open(f'{year}.json', 'w', encoding='utf-8') as f:
            json.dump(r.json(), f, ensure_ascii=False, indent=4)
        os.chdir('..')
