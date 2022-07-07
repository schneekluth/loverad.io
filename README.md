# Loverad.io
Dieses Repository enthält die Playlisten vom **06.07.2022** der folgenden 6 Radiosender:
+ 90s90s
+ Barbaradio
+ Radio Bob
+ Delta Radio
+ RSH

# API
Alle gelisteten Senderdaten werden von einem Drupal Backend der Firma [Regiocast](https://www.regiocast.de/services/) öffentlich bereitgestellt. Dafür werden senderspezifische URLs verwendet.

## URLs
URL-Schema am Beispiel Delta Radio:
```
https://iris-delta.loverad.io/search.json?station=3&=start=2022-07-06T00%3A00%3A00%2B02%3A00&end=2022-07-06T23%3A59%3A59%2B02%3A00
```

Start und Endzeitraum müssen encodiert werden, bspw. mit [URL-Encoder](https://www.urlencoder.org/). 
Eingabeformat für den Encoder: `2022-07-06T23:59:59+02:00`

### Sender
Sender mit Loverad.io Backend sind [hier](https://www.regiocast.de/unternehmen/) gelistet.

### Api für Playlist
Im folgenden 6 Beispiele, samt URLs zur API:

| Sender        | Link zur Playlist-API                                                                                                                             |
|-------------- |-------------------------------------------------------------------------------------------------------------------------------------------------- |
| Delta         | [klick](https://iris-delta.loverad.io/search.json?station=3&=start=2022-07-06T00%3A00%3A00%2B02%3A00&end=2022-07-06T23%3A59%3A59%2B02%3A00)       |
| RSH           | [klick](https://iris-rsh.loverad.io/search.json?station=2&start=2022-07-06T00%3A00%3A00%2B02%3A00&end=2022-07-06T23%3A59%3A59%2B02%3A00)          |
| PSR           | [klick](https://iris-psr.loverad.io/search.json?station=7&start=2022-07-06T00%3A00%3A00%2B02%3A00&end=2022-07-06T23%3A59%3A59%2B02%3A00)          |
| Bob           | [klick](https://iris-bob.loverad.io/search.json?station=3&start=2022-07-06T00%3A00%3A00%2B02%3A00&end=2022-07-06T23%3A59%3A59%2B02%3A00s)         |
| 90s90s        | [klick](https://iris-90s90s.loverad.io/search.json?station=141&start=2022-07-06T00%3A00%3A00%2B02%3A00&end=2022-07-06T23%3A59%3A59%2B02%3A00)     |
| Barbaradio    | [klick](https://iris-barbaradio.loverad.io/search.json?station=278&start=2022-07-06T00%3A00%3A00%2B02%3A00&end=2022-07-06T23%3A59%3A59%2B02%3A00) |

**Achtung:**  
Die API wirft bei suchen über längere Zeiträume nicht valides JSON zurück. Sieht Doppelkomma und Doppeleintrag für `"airtime"`:
```
{"airtime":"2022-07-06T21:52:53+02:00","duration":"193",,{"airtime":"2022-07-06T21:49:04+02:00","duration":"232",
    "song": {
        "found": "1",
        "entry": [
```

### API für Verkehrs- und Blitzermeldungen
| Sender        | Link zur Verkehrs API                                 |
|-------------- | ----------------------------------------------------- |
| PSR           | [klick](https://traffic-service.loverad.io/v2/psr)    |
| RSH           | [klick](https://traffic-service.loverad.io/v2/rsh)    |
| Delta         | [klick](https://traffic-service.loverad.io/v2/delta)  |

## Ressources
+ [python-prettytable](https://pypi.org/project/prettytable/)