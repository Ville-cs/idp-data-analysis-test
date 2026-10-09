import numpy as np
import pandas as pd

def show_stats(path):

    df = pd.read_csv(path, header=0).select_dtypes(include="number")
    print(f"Lowest:  {df.min().min()}")
    print(f"Highest: {df.max().max()}") 
    print(f"Median:  {np.median(df.to_numpy())}")