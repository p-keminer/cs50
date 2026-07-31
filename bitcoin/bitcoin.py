import sys
import requests

if len(sys.argv) != 2:
    sys.exit("missing command-line argument")
else:
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("no number")

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=1788ca784202fc99f1a38dd6bb8cc43317c304b9a0d7c90342d45fa726e6981b")

print(f"${float(response.json()['data']['priceUsd']) * float(sys.argv[1]):,.4f}")
#  formatierter string -> antwort auf nachfrage in json format -> gehe in den key 'data' aus dem dictionary ----------------------------+
#                                                                                           |                                           |
#                                                                                           v                                           |
#                                                                           hole den key 'priceUsd' aus dem key von 'data'              |
#                                                                                           |                                           |
#                                                                                           v                                           |
#                                                                      multipliziere ihn mit dem kommandozeileargument                  |
#                                                                                           |                                           |
#                                                                                           v                                           |
#                                               gebe ihn formatiert(:) mit',' alle 3 stellen und 4 nachkommastellen(.4) als float aus   |
#{                                                                                                                                      |
# "data": {                                                                           <-----+-------------------------------------------+
#   "id": "bitcoin",                                                                        |
#   "rank": "1",                                                                            |
#   "symbol": "BTC",                                                                        |
#  "name": "Bitcoin",                                                                       |
#  "supply": "19823321.0000000000000000",                                                   |
#  "maxSupply": "21000000.0000000000000000",                                                |
#  "marketCapUsd": "1939613325892.4607145113457500",                                        |
#  "volumeUsd24Hr": "12341417371.3505338276601668",                                         |
#  "priceUsd": "97845.0243474572557500",                   <--------------------------------+
#  "changePercent24Hr": "1.4324165997531723",
#  "vwap24Hr": "96203.8859537212418977",
#  "explorer": "https://blockchain.info/"
# },
#  "timestamp": 1739399343596
#}
#
#
#
#
#
#
#
#
#

