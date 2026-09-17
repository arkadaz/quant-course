x = np.array([-1, 0, 2])
p = np.array([0.55, 0.15, 0.30])
colors = [BAD, MUTED, GOOD]
ax.bar(x, p, width=0.6, color=colors)
for xi, pi in zip(x, p):
    ax.text(xi, pi + 0.02, f"{pi:.2f}", ha="center", fontsize=8.5, color=INK)
ax.set_xticks(x, ["-1R (stop)", "0R (breakeven)", "+2R (target)"])
ax.set_ylim(0, 0.72)
ax.set_xlabel("Trade outcome X (R-multiples)")
ax.set_ylabel("PMF p(x)")
ax.set_title("Three outcomes, weights sum to exactly 1.00", loc="left")
