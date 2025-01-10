import requests
import os
from stix2 import MemoryStore, Filter

# Obtenemos la matriz al completo y la guardamos en src para poder despues hacer la query
def get_data_from_branch(domain):
    """get the ATT&CK STIX data from MITRE/CTI. Domain should be 'enterprise-attack', 'mobile-attack' or 'ics-attack'. Branch should typically be master."""
    stix_json = requests.get(
        f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/{domain}/{domain}.json").json()
    return MemoryStore(stix_data=stix_json["objects"])


src = get_data_from_branch("enterprise-attack")

# Leer TTPs desde un archivo
def read_ttp_ids(file_name="input.txt"):
    ttp_ids = []
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, "r") as file:
            for line in file:
                items = line.replace(",", " ").split()
                for item in items:
                    if item.strip().startswith("T") and len(item.strip()) >= 5:
                        ttp_ids.append(item.strip())
        print(f"Se encontraron {len(ttp_ids)} TTP IDs.")
        return ttp_ids
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no se encontró en el directorio '{script_dir}'.")
        return []
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
        return []

# Ejecución principal
if __name__ == "__main__":
    ttp_list = read_ttp_ids()
    if ttp_list:
        print("\nLista de TTP IDs encontrados:")
        for ttp in ttp_list:
            #print(ttp)
            results = src.query([
                Filter("external_references.external_id", "=", ttp),
                Filter("type", "=", "attack-pattern")
            ])
            if results:
                ttp_data = results[0]
                print(ttp,",",ttp_data.name)
            else:
                print(f"No se encontró información para el TTP ID: {ttp}")
