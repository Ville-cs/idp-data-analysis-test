import numpy as np
import os

def memory_mapped_reader(filename):
    dtype = np.int16
    n_columns = 2

    file_size = os.path.getsize(filename)
    n_values = file_size // np.dtype(dtype).itemsize
    n_rows = n_values // n_columns

    data = np.memmap(
        filename,
        dtype=dtype,
        mode="r",
        shape=(n_rows, n_columns)
    )

    print(data[:10])