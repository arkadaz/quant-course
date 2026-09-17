n = 10
p_range = np.linspace(0.01, 0.99, 200)
var = n * p_range * (1 - p_range)
ax.plot(p_range, var, color=ACCENT, lw=2.5, zorder=2)
ax.axvline(0.5, color=MUTED, lw=1, ls=(0, (4, 3)))
ax.plot(0.5, n*0.25, "o", color=BAD, ms=6, zorder=3)
ax.annotate("max Var = n/4 = 2.5\nat p = 0.5 (coin flip)", xy=(0.5, n*0.25), xytext=(0.55, n*0.25-0.7),
            fontsize=8, color=INK)
ax.set_xlabel("p (true skill, prob of beating the market in one year)")
ax.set_ylabel("Var(X) = np(1-p)")
ax.set_title("Uncertainty about the record peaks exactly at zero skill", loc="left")
