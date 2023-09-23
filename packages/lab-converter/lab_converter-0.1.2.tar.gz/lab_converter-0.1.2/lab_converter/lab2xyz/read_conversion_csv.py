import pandas as pd

def extract_store_base10_hex_conversion(csv_path):
    # Read in conversion table into pandas dataframe
    conversion = pd.read_csv(csv_path)
    return conversion