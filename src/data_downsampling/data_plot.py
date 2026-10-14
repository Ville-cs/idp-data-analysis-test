import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# fs is the sampling rate, step is how many samples are used
# 50 000 / 100 = 500 samples/second. Not sure if optimal
def plot_bin(path, ncols=2, fs=50_000, step=100):
    
    data = np.memmap(path, dtype=np.int16, mode="r").reshape(-1, ncols)
    data = data[::step]
    t = np.arange(len(data)) * step / fs        # time in seconds

    # simple scatter plot of downsampled values with both channels
    for i in range(ncols):
        plt.scatter(t, data[:, i], s=2, label=f"channel {i}")

    plt.xlabel("time (s)")
    plt.ylabel("signal intensity")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_lines_bin(path, ncols=2, fs=50_000, step=100):
    data = np.memmap(path, dtype=np.int16, mode="r").reshape(-1, ncols)
    data = data[::step]
    # calculates average of both channels per data point
    avg = data.mean(axis=1)
    # calculates time in seconds (because it's not in the original data)
    t = np.arange(len(avg)) * step / fs

    # plots lines instead of dots
    # change lw to edit the width of the lines (peaks)
    plt.plot(t, avg, lw=0.5)
    plt.xlabel("time (s)")
    plt.ylabel("signal intensity")
    plt.show()


def plot_window_bin(path, ncols=2, fs=50_000, step=100, duration=75):
    n = int(duration * fs)
    raw = np.memmap(path, dtype=np.int16, mode="r")
    # first 75 s only. Change value of duration to test different windows
    data = raw[: n * ncols].reshape(-1, ncols)
    data = data[::step]
    # calculates average of both channels per data point
    avg = data.mean(axis=1)
    # calculates time in seconds (because it's not in the original data)
    t = np.arange(len(avg)) * step / fs

    # plots lines instead of dots
    # change lw to edit the width of the lines (peaks)
    plt.plot(t, avg, lw=2.5)
    plt.xlabel("time (s)")
    plt.ylabel("signal intensity")
    plt.show()


def plot_csv(path, ncols=2, fs=50_000, step=100):

    data = pd.read_csv(path, header=0, usecols=range(ncols)).to_numpy()
    data = data[::step]
    t = np.arange(len(data)) * step / fs

    for i in range(ncols):
        plt.scatter(t, data[:, i], s=2, label=f"channel {i}")

    plt.xlabel("time (s)")
    plt.ylabel("signal intensity")
    plt.legend()
    plt.grid(True)
    plt.show()
