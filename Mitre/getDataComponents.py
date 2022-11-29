import json
from pathlib import Path
import pandas as pd


strt = "Technique"
# returns JSON object as
# a dictionary

#Leemos Name de los DS a sacar
in_file = open('data.csv', "r")
try:
    DS = pd.read_csv('data.csv', header=0)
    #print(ID['ID'])
    list_DS=DS['Data Source']
    #print(list_DS)

except:
    print("Error al abrir el archivo .csv. Por favor revíselo")


#Leemos el .json con todos los DS
for p in Path('.').glob('*.json'):
    with open(p.name) as json_file:
        json_load = json.load(json_file)

#Iteramos para sacar los DataComponents de los DS que están en el csv
for b in json_load['datasources']:
    for x in list_DS:
        if(x == b['name']):
            print(b['name'],"," , len(b['data_components']),",")
            for y in b['data_components']:
                print(y['name'])

