import requests
from stix2 import MemoryStore
from stix2 import Filter


# Obtenemos la matriz al completo y la guardamos en src para poder despues hacer la query
def get_data_from_branch(domain):
    """get the ATT&CK STIX data from MITRE/CTI. Domain should be 'enterprise-attack', 'mobile-attack' or 'ics-attack'. Branch should typically be master."""
    stix_json = requests.get(
        f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/{domain}/{domain}.json").json()
    return MemoryStore(stix_data=stix_json["objects"])


src = get_data_from_branch("enterprise-attack")

def getTacticsByMatrix(thesrc):
    tactics = {}
    matrix = thesrc.query([
        Filter('type', '=', 'x-mitre-matrix'),
    ])

    for i in range(len(matrix)):
        tactics[matrix[i]['name']] = []
        for tactic_id in matrix[i]['tactic_refs']:
            tactics[matrix[i]['name']].append(thesrc.get(tactic_id))

    print (tactics)

# get tactic layout
getTacticsByMatrix(src)
