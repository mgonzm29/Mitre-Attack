import requests
import pandas as pd
from stix2 import MemoryStore
from stix2 import Filter

#Obtenemos la matriz al completo y la guardamos en src para poder despues hacer la query
def get_data_from_branch(domain):
    """get the ATT&CK STIX data from MITRE/CTI. Domain should be 'enterprise-attack', 'mobile-attack' or 'ics-attack'. Branch should typically be master."""
    stix_json = requests.get(f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/{domain}/{domain}.json").json()
    return MemoryStore(stix_data=stix_json["objects"])
  
src = get_data_from_branch("enterprise-attack")

#Inicio de la query.
t1134 = src.query([
    Filter("external_references.external_id", "=", "T1027.005"),
    Filter("type", "=", "attack-pattern")
])[0]

print(t1134)
#name+","+t1134.description 
