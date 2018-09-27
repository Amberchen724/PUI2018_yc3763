import pylab as pl
import os 
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib 
import os
import sys
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+sys.argv[1]+'&VehicleMonitoringDetailLevel=calls&LineRef='+sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)
variable1 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
variable1 
index = 0

print ('Bus Line ' +  sys.argv[2])
busnumber=0
for k in variable1:
    busnumber+=1 
print ('Active Bus Line '+ str(busnumber))
for k in variable1:
    k = k['MonitoredVehicleJourney']
    index += 1 
    print ('Bus',index,'is at latitude',k['VehicleLocation']['Latitude'], 'Longitude', k['VehicleLocation']['Longitude'])