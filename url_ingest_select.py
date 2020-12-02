import json
from datetime import datetime

from urllib.request import urlopen

with urlopen("https://feeds.citibikenyc.com/stations/stations.json") as response:
    source = response.read()

#load the source into data obj
data = json.loads(source)

#Option to print the url feed and length of data
#print(json.dumps(data, indent=2))
#print(len(data['stationBeanList']))

#parse the json file & print selected results to stdout
for each in data['stationBeanList']:
    print(each['stationName'], each['statusValue'])
    #del each['testStation']
print(len(data['stationBeanList']))

#Option to write to a file below
with open(str(datetime.now().strftime('%Y%m%d-%H%M%S')) + '-mlogistics-url-ingest-select' + '.json', 'w') as write_file:
    json.dump(data, write_file, indent=2)