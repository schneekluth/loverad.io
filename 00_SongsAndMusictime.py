import json
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
        "path": "./delta_2022-07-06.json"
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

x = PrettyTable()
x.field_names = ["Sender", "Songs pro Tag", "Musikzeit [h]", "Tagesanteil Musik [%]"]

for file in files:
    f = open(file['path'])
    data = json.load(f)
    f.close

    station = file['name']
    songsPerDay = int(data['result']['found'])

    duration = 0
    for n in data['result']['entry']:
        duration = duration + int(n['duration'])

    musicHours = round(duration/3600, 2)
    musicPerDayPercent = round(musicHours/24*100, 2)

    x.add_row([station, songsPerDay, "{:.2f}".format(musicHours), "{:.2f}".format(musicPerDayPercent)] )

print(x)
