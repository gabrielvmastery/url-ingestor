import json
from datetime import datetime

from urllib.request import urlopen

with urlopen("https://feeds.citibikenyc.com/stations/stations.json") as response:
    source = response.read()

#load the source into data objwest
data = json.loads(source)
#print(json.dumps(data, indent=2))
#print(len(data['stationBeanList']))

#parse the json file
for each in data['stationBeanList']:
    #print(bean['stationName']) #use this line to print
    print(each['testStation'])
    del each['testStation']     #use this line to remove lines

with open(str(datetime.now().strftime('%Y%m%d-%H%M%S')) + '-mlogistics' + '.json', 'w') as write_file:
    json.dump(data, write_file, indent=2)