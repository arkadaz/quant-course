import matplotlib.patches as patches
mu = 0.05
outcomes = [(2.0, 0.30, GOOD, "big winner"), (-1.0, 0.55, BAD, "stop-loss"), (0.0, 0.15, MUTED, "scratch")]
ax.axhline(0, color=INK, lw=1.2, zorder=2)
ax.plot(mu, 0, "o", ms=6, color=INK, zorder=5)
ax.annotate("μ = 0.05R", xy=(mu, 0), xytext=(0, -16), textcoords="offset points", ha="center", fontsize=8, color=INK)
for x, p, colour, name in outcomes:
    d = abs(x - mu)
    left = min(mu, x)
    weighted = d**2 * p
    alpha = 0.30 + 0.60*p
    sq = patches.Rectangle((left, 0), d, d, facecolor=colour, edgecolor=INK, lw=1.0, alpha=alpha, zorder=3)
    ax.add_patch(sq)
    ax.plot(x, 0, "o", ms=5, color=INK, zorder=5)
    ax.annotate(f"{name}\nx={x:g}R, p={p:.2f}\narea={d**2:.3f}, weighted={weighted:.3f}", xy=(left+d/2, d),
                xytext=(0, 4), textcoords="offset points", ha="center", fontsize=6.8, color=INK)
ax.set_xlim(-2.0, 3.0)
ax.set_ylim(0, 2.7)
ax.set_xlabel("Outcome X (R multiples)")
ax.set_ylabel("(X - μ)² — literal square area")
ax.set_title("Each outcome's squared distance from μ, drawn as an actual square", loc="left")
