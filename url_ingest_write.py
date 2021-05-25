import json
from datetime import datetime

from urllib.request import urlopen

with urlopen("https://feeds.citibikenyc.com/stations/stations.json") as response:
    source = response.read()

#load the source into data object
data = json.loads(source)
#print(json.dumps(data, indent=2))
#print(len(data['stationBeanList']))

#parse the json file
for each in data['stationBeanList']:
    #print(bean['stationName']) 
    print(each['testStation'])
    del each['testStation']     

with open(str(datetime.now().strftime('%Y%m%d-%H%M%S')) + '-mlogistics' + '.json', 'w') as write_file:
    json.dump(data, write_file, indent=2)
