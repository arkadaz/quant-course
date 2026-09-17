for n, colour in [(10, ACCENT), (20, WARM), (50, GOOD)]:
    r = np.arange(0, n + 1)
    ax.plot(r, stats.binom.pmf(r, n, 0.5), marker="o", ms=2.5, lw=1.5, color=colour, label=f"Binomial(n={n}, p=0.5)")
ax.set_xlabel("Number of wins r")
ax.set_ylabel("PMF P(X=r)")
ax.set_title("Same p, longer track record: Binomial PMFs", fontsize=9, loc="left")
ax.legend(fontsize=7)
