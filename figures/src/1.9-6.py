from math import comb
die = np.ones(6) / 6
cases = [("1 die", die, 1, MUTED), ("2 dice", np.convolve(die, die), 2, WARM),
         ("3 dice", np.convolve(np.convolve(die, die), die), 3, GOOD)]
for label, pmf, first, colour in cases:
    values = np.arange(first, first + len(pmf))
    mean = (values * pmf).sum()
    sd = np.sqrt(((values - mean) ** 2 * pmf).sum())
    ax.plot((values - mean) / sd, pmf * sd, marker="o", ms=4, lw=1.4, color=colour, label=label)
k = np.arange(11)
coin = np.array([comb(10, i) for i in k]) / 2**10
sd10 = np.sqrt(2.5)
ax.plot((k - 5) / sd10, coin * sd10, marker="s", ms=4, lw=1.4, color=ACCENT, label="10 coins (heads)")
z = np.linspace(-3.5, 3.5, 300)
ax.plot(z, stats.norm.pdf(z), color=BAD, lw=2.2, ls=(0, (4, 2)), label="bell: exp(-z^2/2) / sqrt(2 pi)")
ax.set_xlim(-3.5, 3.5)
ax.set_xlabel("distance from the mean, in SDs (z)")
ax.set_ylabel("probability x SD (same scale for all)")
ax.set_title("Add more pieces and the shape turns into the same bell", loc="left")
ax.legend(fontsize=7, loc="upper left", frameon=False)
