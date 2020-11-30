import pandas as pd

def load_and_process(url):
    df=(pd.read_csv(url).drop(columns=["DGUID", "UOM", "SCALAR_FACTOR", "VECTOR", "COORDINATE", "STATUS", "SYMBOL", "TERMINATED", "UOM_ID", "SCALAR_ID", "DECIMALS", "VALUE"]).dropna().reset_index(drop=True))
    
    df_provinces=(df.loc[~df.GEO.str.contains("Canada excluding")].reset_index(drop=True)
                  .assign(Primary_Types=(df["Primary types of cancer (ICD-O-3)"].str.split('[').str[0])).drop(columns="Primary types of cancer (ICD-O-3)")
                  .assign(Stage=(df["Stage at diagnosis"].str.split('(').str[0])).drop(columns="Stage at diagnosis")
                 )

    return df_provinces

    