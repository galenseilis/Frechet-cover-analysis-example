"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.12
"""

import requests

from kedro.pipeline import node
import pandas as pd

def load_env_chem_data():
    '''Load the environmental chemistry data.'''
    url = 'https://doi.org/10.1371/journal.pone.0282068.s001'
    response = requests.get(url)
    data = response.content
    out_path = './data/01_raw/' +\
            'journal.pone.0282068.s001.xlsx'

    with open(out_path, 'wb') as f:
        f.write(data)

    return pd.read_excel(out_path)

return_load_env_chem_data = node(func=load_env_chem_data, inputs=None, outputs="env_chem_raw_data")


