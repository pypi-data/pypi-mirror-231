
import json
import os
import datetime


class data:
    def __init__(self, path:str ="C:/Users/amy_m/OneDrive/Skrivebord/"):
        '''
        path::  the path to the folder where the data file is located

        '''
        dictory = { "fish": {}, "Data": {
        "total weight": 0,
        "total fish": 0,
        "species caught": ""
            }
        }

        # Get the current date
        self.current_date = datetime.date.today()

        self.path = path + f'{self.current_date}FishData.json'
    # Created the JSON file for the data
        if not os.path.exists(self.path):
            with open(self.path, 'w') as file:
                json.dump(dictory, file, indent=4)
  
    def add_fish(self, fish:str, weight:float, length:float, good:bool = True):
        '''Adds a fish to the data file

        fish::  the fish type

        weight::  the weight of the fish (in kg)
        
        length::  the length of the fish (in mm)

        good::  if the fish is good or not (default is True)
        '''

        with open(self.path, "r") as json_file:
            data = json.load(json_file)

        if fish in data['fish']:
            if good == True:
                size = "sizeH"
            else:
                size = "sizeL"
            
            data['fish'][fish][size]['fanget'] += 1
            data['fish'][fish][size]['weight'] += weight
            #data['fish'][fish][size]['length'] += length

        else:
            if data['Data']['species caught'] == "":
                data['Data']['species caught'] = fish
            else:
                data['Data']['species caught'] = fish + "," + data['Data']['species caught']

            if good == True:
                data['fish'][fish] = {
                    "sizeH": {
                        "fanget": 1,
                        "weight": weight,
                    #    "length": length
                    },
                    "sizeL": {
                        "fanget": 0,
                        "weight": 0,
                    #    "length": 0
                    }
                }
            else:
                data['fish'][fish] = {
                    "sizeH": {
                        "fanget": 0,
                        "weight": 0,
                    #    "length": 0
                    },
                    "sizeL": {
                        "fanget": 1,
                        "weight": weight,
                    #    "length": length
                    }
                }

        
        data['Data']['total weight'] += weight
        data['Data']['total fish'] += 1

        # Step 3: Write the modified data back to the JSON file
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)
    
    def get_data(self):
        '''Returns the data as a dictionary'''
        with open(self.path, "r") as json_file:
            data = json.load(json_file)
        return data
    
    def get_fishdata(self, fish:str):
        '''Returns the fish data as a dictionary'''
        with open(self.path, "r") as json_file:
            data = json.load(json_file)
        return data['fish'][fish]




if __name__ == "__main__":
    data.__init__()