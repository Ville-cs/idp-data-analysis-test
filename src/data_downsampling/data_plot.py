import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_bin(path, ncols=2, fs=50_000, step=100):

    data = np.memmap(path, dtype=np.int16, mode="r").reshape(-1, ncols)
    data = data[::step]                         # every 100th sample
    t = np.arange(len(data)) * step / fs        # time in seconds

    for i in range(ncols):
        plt.scatter(t, data[:, i], s=2, label=f"channel {i}")

    plt.xlabel("time (s)")
    plt.ylabel("signal intensity")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_csv(path, ncols=2, fs=50_000, step=100):

    data = pd.read_csv(path, header=0, usecols=range(ncols)).to_numpy()
    data = data[::step]                         # every 100th sample
    t = np.arange(len(data)) * step / fs        # time in seconds

    for i in range(ncols):
        plt.scatter(t, data[:, i], s=2, label=f"channel {i}")

    plt.xlabel("time (s)")
    plt.ylabel("signal intensity")
    plt.legend()
    plt.grid(True)
    plt.show()