"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.12
"""

from kedro.pipeline import Pipeline, pipeline
from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([nodes.return_load_env_chem_data])
