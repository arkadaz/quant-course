S0, mu = 120.0, 0.15
sigma_range = np.linspace(0.001, 0.90, 300)
mean_price = S0*np.exp(mu)
median_price = S0*np.exp(mu - sigma_range**2/2)
gap = mean_price - median_price
ax.plot(sigma_range, gap, color=ACCENT, lw=2.5, label="mean minus median")
ax.axhline(0, color=MUTED, lw=0.8)
sig_nvda = 0.55
gap_nvda = mean_price - S0*np.exp(mu - sig_nvda**2/2)
ax.axvline(sig_nvda, color=BAD, lw=1, ls=(0, (4, 3)))
ax.plot(sig_nvda, gap_nvda, "o", color=BAD, ms=6, zorder=3)
ax.annotate(f"NVDA sigma=55% -> gap ${gap_nvda:.2f}", xy=(sig_nvda, gap_nvda),
            xytext=(sig_nvda+0.03, gap_nvda+8), fontsize=8, color=INK)
ax.set_xlabel(r"Annual volatility $\sigma$")
ax.set_ylabel("Mean price - Median price ($)")
ax.set_title(r"Volatility drag: mean barely moves, median falls away as $\sigma$ rises", loc="left")
ax.legend(loc="upper left", fontsize=8)
