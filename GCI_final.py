import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    # Component values
    L = 65e-3      # 65 mH
    C = 1e-9       # 1 nF
    R = 161        # 161 ohms

    # Linear frequency sweep in kHz
    f_khz = np.linspace(1, 200, 2000)   # 1 kHz to 200 kHz
    freq = f_khz * 1e3                  # convert to Hz for calculations

    # Impedances
    w = 2 * np.pi * freq
    Z_L = 1j * w * L
    Z_C = 1 / (1j * w * C)
    Z_R = R

    Z_total = Z_L + Z_C + Z_R

    # Transfer function (voltage across R)
    H = Z_R / Z_total
    mag_db = 20 * np.log10(np.abs(H))

    # --- Plot ---
    plt.figure(figsize=(10,5))
    plt.plot(f_khz, mag_db, linewidth=2)

    # Marker at 20 kHz
    plt.axvline(20, linestyle="--", color="green")

    plt.xlabel("Frequency (kHz)")
    plt.ylabel("Magnitude (dB)")
    plt.title("Series RLC Response Across R (Linear Frequency Axis)")

    # Remove grid
    plt.grid(False)

    # Make ticks evenly spaced (every 10 kHz)
    plt.xticks(np.arange(0, 210, 10))

    plt.show()

    return


if __name__ == "__main__":
    app.run()
