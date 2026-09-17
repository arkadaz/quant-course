lam = 3
k = np.arange(0, 13)
mean_t, var_t = 3.0, 9.0
p_nb = mean_t / var_t
n_nb = mean_t * p_nb / (1 - p_nb)
sf_pois = stats.poisson.sf(k - 1, lam) * 100
sf_nb = stats.nbinom.sf(k - 1, n_nb, p_nb) * 100
ax.plot(k, sf_pois, color=ACCENT, marker="o", ms=4, lw=2, label="Independent (Poisson, λ=3)")
ax.plot(k, sf_nb, color=BAD, marker="o", ms=4, lw=2, label="Correlated (same mean, 3x variance)")
ax.axvline(8, color=MUTED, lw=1, ls=(0, (4, 3)))
ax.annotate("8+ defaults:\n1.2% vs 8.3%", xy=(8, sf_nb[8]), xytext=(8.4, sf_nb[8] + 20),
            fontsize=7.3, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.set_yscale("log")
ax.set_xlabel("k (defaults)")
ax.set_ylabel("P(X ≥ k), % (log scale)")
ax.set_xticks(k)
ax.legend(loc="best", fontsize=7.3)
ax.set_title("Break independence and the right tail gets fat fast", loc="left")
