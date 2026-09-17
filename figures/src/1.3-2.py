labels = ["Win side\n(+2R x 0.30)", "Loss side\n(-1R x 0.55)", "Net E[X]"]
vals = [0.60, -0.55, 0.05]
colors = [GOOD, BAD, ACCENT]
ax.bar(labels, vals, color=colors, width=0.55)
for i, v in enumerate(vals):
    ax.annotate(f"{v:+.2f}R", xy=(i, v), xytext=(0, 4 if v>=0 else -14), textcoords="offset points", ha="center", fontsize=8.5, color=INK)
ax.axhline(0, color=INK, lw=1)
ax.set_ylabel("Contribution to E[X] (R)")
ax.set_title("Win side beats loss side by a hair: payoff ratio 2.00 edges out frequency ratio 1.83", loc="left")
