import numpy as np
import pandas as pd

def csv_to_bin(input_file, output_file):

    chunk_size = 100_000
    with open(output_file, "wb") as f:
        # read in chunks to manage huge file sizes
        for chunk in pd.read_csv(
            input_file,
            dtype=np.int16,
            header=0,
            chunksize=chunk_size
        ):
            chunk.to_numpy(dtype=np.int16).tofile(f)