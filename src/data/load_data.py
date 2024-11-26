import pandas as pd

def load_data(filepath='data/raw/soil_measures.csv'):
    """Carrega os dados do arquivo CSV especificado."""
    return pd.read_csv(filepath)
