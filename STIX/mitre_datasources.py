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

def get_techniques_or_subtechniques(thesrc, include="both"):
    """Filter Techniques or Sub-Techniques from ATT&CK Enterprise Domain.
    include argument has three options: "techniques", "subtechniques", or "both"
    depending on the intended behavior."""
    if include == "techniques":
        query_results = thesrc.query([
            Filter('type', '=', 'attack-pattern'),
            Filter('x_mitre_is_subtechnique', '=', False)
        ])
    elif include == "subtechniques":
        query_results = thesrc.query([
            Filter('type', '=', 'attack-pattern'),
            Filter('x_mitre_is_subtechnique', '=', True)
        ])
    elif include == "both":
        query_results = thesrc.query([
            Filter('type', '=', 'attack-pattern')
        ])
    else:
        raise RuntimeError("Unknown option %s!" % include)

    return query_results


subtechniques = get_techniques_or_subtechniques(src, "subtechniques")
techniques = get_techniques_or_subtechniques(src, "techniques")

#Si se quiere sacar una posición en concreto o la matriz completa
#print(subtechniques)
#print(techniques[1].x_mitre_data_sources)

print("Name",",", "ID",",", "DataSources",",","Total")
for x in techniques:
	#Creado para que no entre en aquellas TTPs cuyo ID ha sido cambiado y no tienen x.mitre_data_sources (y casca). Estas TTPs iran al except y se desecharán
	try: 	
		if(x.x_mitre_data_sources is not None):
			#Sacamos por pantalla Nombre, ID, Data Sources y numero de data sources
			print(x.name,",",x.external_references[0].external_id,",",x.x_mitre_data_sources,",",len(x.x_mitre_data_sources))
		
	except: None
	

for x in subtechniques:
	#Creado para que no entre en aquellas TTPs cuyo ID ha sido cambiado y no tienen x.mitre_data_sources (y casca). Estas TTPs iran al except y se desecharán
	try: 	
		if(x.x_mitre_data_sources is not None):
			#Sacamos por pantalla Nombre, ID, Data Sources y numero de data sources
			print(x.name,",",x.external_references[0].external_id,",",x.x_mitre_data_sources,",",len(x.x_mitre_data_sources))
		
	except: None


 # see https://github.com/mitre/cti/blob/master/USAGE.md#removing-revoked-and-deprecated-objects

