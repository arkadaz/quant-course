rate = 0.2
x = np.linspace(0, 30, 300)
pdf = rate*np.exp(-rate*x)
ax.plot(x, pdf, color=ACCENT, lw=2)
ax.fill_between(x, pdf, color=ACCENT, alpha=0.12)
mask = x >= 10
ax.fill_between(x[mask], pdf[mask], color=BAD, alpha=0.35)
ax.axvline(10, color=INK, lw=0.8, ls=(0, (2, 2)))
ax.annotate("P(wait>10s) = 13.53%", xy=(11, pdf[np.searchsorted(x,11)]+0.01), fontsize=8, color=BAD)
ax.annotate("mean wait = 5s", xy=(5.3, rate*np.exp(-rate*5)+0.01), fontsize=8, color=INK)
ax.set_xlabel("Seconds until next ES order")
ax.set_ylabel("Density")
ax.set_title("Exponential waiting time -- memoryless: the last 10s tell you nothing", loc="left")
