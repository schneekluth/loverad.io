import json
import csv
from prettytable import PrettyTable

files = [
    {
        "name": "rsh",
        "path": "./rsh_2022-07-06.json"
    },{
        "name": "bob",
        "path": "./bob_2022-07-06.json"
    },{
        "name": "delta",
        "path": "./deltaradio_2022-07-06.json"
    },{
        "name": "psr",
        "path": "./psr_2022-07-06.json"
    },{
        "name": "90s90s",
        "path": "./90s90s_2022-07-06.json"
    },{
        "name": "barbaradio",
        "path": "./barbaradio_2022-07-06.json"
    }
]

for file in files:
    f = open(file['path'])
    data = json.load(f)
    f.close

    station = file['name']
    header = ['GUID', 'AIRTIME', 'ARTIST', 'TRACK']

    with open(f"{station}_2022-07-06.csv", 'w', encoding='UTF8') as fi:
        writer = csv.writer(fi)
        writer.writerow(header)

        for i in data['result']['entry']:
            guid = i['song']['entry'][0]['guid']
            airtime = i['airtime']
            track = i['song']['entry'][0]['title']
            artist = i['song']['entry'][0]['artist']['entry'][0]['name']

            writer.writerow([guid, artist, track, airtime])

    fi.close()