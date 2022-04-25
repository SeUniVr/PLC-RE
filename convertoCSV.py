import json
import pandas as pd
import glob
import os


def flatten_json(nested_json: dict, exclude: list=[''], sep: str='_') -> dict:
    """
    Flatten a list of nested dicts.
    """
    out = dict()
    def flatten(x: (list, dict, str), name: str='', exclude=exclude):
        if type(x) is dict:
            for a in x:
                if a not in exclude:
                    flatten(x[a], f'{name}{a}{sep}')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, f'{name}{i}{sep}')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

def convert(plc) :
    # list of json files
    files = sorted(glob.glob('historian/plc'+plc+'*.json'))


    # list to add dataframe from each file
    df_list = list()

    #list to save timestamps values
    timestamp = list()

    # iterate through json files
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:

            # read with json
            data = json.loads(f.read().replace('%','').replace('.','').replace('127001','PLC'+plc))
            #print (os.path.basename(file)[20:43])
            print(file)
            #print(os.path.basename(file)[20:43])
            #save timestamps values
            timestamp.append(os.path.basename(file)[20:43])
            # flatten_json into a dataframe and add to the dataframe list
            df_list.append(pd.DataFrame.from_dict(flatten_json(data), orient='index').T)


            
    # concat all dataframes together
    df = pd.concat(df_list).reset_index(drop=True)

    if(plc == 1):
        # insert timestamps in the first column
        df.insert(0,'timestamps', timestamp) 

         
    print(df)
    df.to_csv(r'PLC_CSV/PLC'+plc+'Dataset.csv', index = False)
convert(str(1))
convert(str(2))
convert(str(3))
