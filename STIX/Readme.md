# Queries with STIX
## mitre_tacticas.py
Se obtendran todas las tácticas que componen la matriz de MITRE junto con su información adicional
```powershell
python mitre_tecnicas.py > output.txt
```

## mitre_tecnicas.py
Se obtendran todas las técnicas y subtécnicas que componen la matriz de MITRE junto con su información adicional
```powershell
python mitre_tacticas.py > output.txt
```

## mitre_data_sources.py
Se obtendrás todos los data sources de todas las TTP:
```powershell
python mitre_tacticas.py > output.txt
```
El output obtenido, será el siguiente:

Nombre TTP, ID TTP, [Data source:Data component,...], Total de Data sources
```powershell
Screen Capture,T1113,['Command: Command Execution', 'Process: OS API Execution'],2
```
## mitre-busqueda_TTP.py
Teniendo un archivo input.txt en el mismo path que el ejecutable py, leerá el archivo txt, obtendra todas las TTPs que identifique, y devolvera el nombre de dicha TTP :
```powershell
python mitre-busqueda_TTP.py > output.txt
```
![image](https://github.com/user-attachments/assets/06e4923c-256c-46dd-9b2f-369d23022860)



