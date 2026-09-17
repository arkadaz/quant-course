rng = np.random.default_rng(0)
n_mgr, n_year, p = 100, 10, 0.5
wins = rng.binomial(n_year, p, size=n_mgr)
lucky = wins >= 8
side = 10
xs, ys = np.meshgrid(np.arange(side), np.arange(side))
xs, ys = xs.flatten(), ys.flatten()
colors = np.where(lucky, GOOD, MUTED)
ax.scatter(xs, -ys, c=colors, s=90, edgecolors="white", linewidths=0.6, zorder=2)
ax.set_xlim(-1, side)
ax.set_ylim(-side, 1)
ax.set_xticks([]); ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_title(f"100 zero-skill managers, {int(lucky.sum())} light up green from luck alone", loc="left")
