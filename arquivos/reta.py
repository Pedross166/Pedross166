from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

config_plt = {
    "xtick.top": True,
    "ytick.right": True,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "axes.titlesize": 12,
    "axes.labelsize": 12,
    "legend.fontsize": 9,
    "figure.subplot.wspace": 0.5,
    "figure.subplot.hspace": 0.5,
}

plt.style.use([config_plt])

x = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4])
y = np.array([7.1, 9.6, 16.9, 21, 25.4, 28.1, 35.7, 39])
u_x = np.array([ 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06])
u_y = np.array([ 0.06, 0.06, 0.06, 0.06, 0.6, 0.6, 0.06, 0])

result = stats.linregress(x, y)

print(
    f"Linear regression:\n Slope: {result.slope:.2f}+-{result.stderr:.2f} \n Intercept: {result.intercept:.2f} +-{result.intercept_stderr:.2f}"
)

fig3, ax3 = plt.subplots(1, 1)

ax3.errorbar(
    x,
    y,
    xerr=u_x,
    yerr=u_y,
    fmt="o",
    elinewidth=1,
    capsize=3,
    capthick=1,
    ms=3,
    c="b",
    ecolor="black",
)

ax3.plot(x, x * result.slope + result.intercept)

ax3.set_xlabel("y (arb.u.")
ax3.set_ylabel("y (arb. u.")

plt.scatter(x, y)
plt.grid("on")
plt.show()