rng = np.random.default_rng(0)
mu, sigma = 0.04, 1.1
n = 250
R = rng.normal(mu, sigma, n)
idx = np.arange(n)
colors = np.where(R < -2.0, BAD, MUTED)
ax.scatter(idx, R, c=colors, s=10, alpha=0.85, zorder=3)
ax.axhline(-2.0, color=BAD, lw=1.1, ls=(0, (4, 3)))
ax.axhline(mu, color=MUTED, lw=0.8)
n_hit = int((R < -2.0).sum())
ax.annotate(f"{n_hit} of 250 days below -2%", xy=(5, -2.0), xytext=(5, -5.2),
            fontsize=8, color=BAD)
ax.set_xlabel("Trading day of the year")
ax.set_ylabel("Simulated daily return (%)")
ax.set_title("250 simulated trading days — red dots breach the 2% loss line", loc="left")
