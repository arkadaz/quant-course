rng = np.random.default_rng(0)
rate = 0.2
u = np.linspace(0.001, 0.999, 200)
x = -np.log(1 - u) / rate
ax.plot(u, x, color=ACCENT, lw=2)
us = rng.uniform(0, 1, 6)
xs = -np.log(1 - us) / rate
ax.plot(us, xs, "o", color=WARM, ms=6, zorder=3)
for uu, xx in zip(us, xs):
    ax.plot([uu, uu], [0, xx], color=MUTED, lw=0.6, ls=(0, (2, 2)))
    ax.plot([0, uu], [xx, xx], color=MUTED, lw=0.6, ls=(0, (2, 2)))
ax.set_xlim(0, 1)
ax.set_ylim(0, 30)
ax.set_xlabel(r"$\mathrm{Uniform}(0,1)$ draw $U$")
ax.set_ylabel(r"Exponential sample $X = F^{-1}(U)$ (s)")
ax.set_title("Every Monte Carlo distribution starts as a Uniform(0,1) draw", loc="left")
