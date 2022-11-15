import json
from pathlib import Path


strt = "Technique"
# returns JSON object as
# a dictionary

for p in Path('.').glob('*.json'):
    with open(p.name) as json_file:
        json_load = json.load(json_file)

    #json_data ='paloalto'

    #json_load = (json.loads(json_data))

    for b in json_load['Adversaries'][0]['Detections_By_Step']:

        for a in range(len(json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'])):
            for x in range(len(json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'])):
                if (json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x]['Subtechnique'][
                    'Subtechnique_Id']) is None:

                    for y in range(len(json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x]['Detections'])):

                        if (json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x]['Detections'][
                            y]['Detection_Type'] == strt):
                            print(json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Technique']['Technique_Name'], ',',
                                  json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Technique']['Technique_Id'], ',',
                                  json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Detections'][y]['Detection_Type'], ',', '1', sep="")
                        else:
                            print(json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Technique']['Technique_Name'], ',',
                                  json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Technique']['Technique_Id'], ',',
                                  json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Detections'][y]['Detection_Type'], ',', 'x', sep="")
                else:
                    for y in range(len(json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                           'Detections'])):
                        if (json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x]['Detections'][
                            y]['Detection_Type'] == strt):
                            print(json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Subtechnique']['Subtechnique_Name'], ',',
                                  json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Subtechnique']['Subtechnique_Id'], ',',
                                  json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Detections'][y]['Detection_Type'], ',', '1', sep="")
                        else:
                            print(json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Subtechnique']['Subtechnique_Name'], ',',
                                  json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                      'Subtechnique']['Subtechnique_Id'], ',',
                                  json_load['Adversaries'][0]['Detections_By_Step'][b]['Steps'][a]['Substeps'][x][
                                          'Detections'][y]['Detection_Type'], ',', 'x', sep="")
