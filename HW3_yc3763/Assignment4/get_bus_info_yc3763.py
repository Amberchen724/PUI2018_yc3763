import csv
import pylab as pl
import os 
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib 
import os
import sys
import pandas as pd
url ='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+sys.argv[1]+'&VehicleMonitoringDetailLevel=calls&LineRef='+sys.argv[2]
print(url)
df = pd.read_json(url)
df.to_csv("busline.csv")
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)
variable1 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
variable1 
index = 0
df_all=pd.DataFrame(columns=['latitude','Longitude','Busstop','Stopstatus'])
for k in variable1:
    k = k['MonitoredVehicleJourney']
    latitude = k['VehicleLocation']['Latitude']
    Longitude = k['VehicleLocation']['Longitude']
    Busstop = k['OnwardCalls']['OnwardCall'][0]['StopPointName']
    Stopstatus= k['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    index+=1 
    df_all.loc[index] = [latitude,Longitude,Busstop,Stopstatus]
    print (latitude,Longitude,Busstop,Stopstatus)
df_all
df_all.to_csv('bustime.csv')
