r = np.arange(0, 11)
lam = 3
for n, colour, lw in [(20, WARM, 1.2), (50, GOOD, 1.5), (1000, BAD, 1.9)]:
    p = lam / n
    ax.plot(r, stats.binom.pmf(r, n, p), color=colour, marker="o", ms=4, lw=lw,
            alpha=0.85, label=f"Binomial(n={n}, p={lam}/{n})")
ax.plot(r, stats.poisson.pmf(r, lam), color=INK, lw=2.2, ls=(0, (4, 2)),
        label="Poisson(λ=3) target")
ax.set_xlabel("Count r")
ax.set_ylabel("P(X=r)")
ax.set_xticks(r)
ax.legend(loc="best", fontsize=7.3)
ax.set_title("n grows, p shrinks, n·p=3 fixed — Binomial converges onto Poisson", loc="left")
