import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data():
    np.random.seed(42)
    time = np.arange(100)
    values = 20 + 5 * np.sin(time * 0.2) + np.random.normal(0, 1, 100)
    return pd.DataFrame({"Time": time, "Value": values})


def plot_series(df):
    plt.figure(figsize=(8, 4))
    plt.plot(df["Time"], df["Value"])
    plt.title("Time Series")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("timeseries.png", dpi=300)
    plt.show()


def rolling_mean(df):
    df = df.copy()
    df["Rolling"] = df["Value"].rolling(window=5).mean()
    plt.figure(figsize=(8, 4))
    plt.plot(df["Time"], df["Value"], label="Original")
    plt.plot(df["Time"], df["Rolling"], label="Rolling Mean")
    plt.legend()
    plt.title("Rolling Mean")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("rolling_mean.png", dpi=300)
    plt.show()


def autocorrelation(series, max_lag=30):
    acf = [series.autocorr(lag=i) for i in range(max_lag)]
    plt.figure(figsize=(8, 4))
    markerline, stemlines, baseline = plt.stem(range(max_lag), acf)
    plt.setp(markerline, markersize=4)
    plt.title("Autocorrelation")
    plt.xlabel("Lag")
    plt.ylabel("Autocorrelation")
    plt.tight_layout()
    plt.savefig("autocorrelation.png", dpi=300)
    plt.show()


def power_spectrum(series):
    fft_vals = np.fft.rfft(series - np.mean(series))
    power = np.abs(fft_vals) ** 2
    freqs = np.fft.rfftfreq(len(series))
    plt.figure(figsize=(8, 4))
    plt.plot(freqs, power)
    plt.title("Power Spectrum")
    plt.xlabel("Frequency")
    plt.ylabel("Power")
    plt.tight_layout()
    plt.savefig("power_spectrum.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    df = load_data()
    print(df["Value"].describe())
    plot_series(df)
    rolling_mean(df)
    autocorrelation(df["Value"], max_lag=30)
    power_spectrum(df["Value"])
