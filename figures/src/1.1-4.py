categories = ["At or below -2%", "Inside (-2%, +2%]", "Above +2%"]
days = [4/251*250, 244/251*250, 3/251*250]
colors_ = [BAD, GOOD, WARM]
ax.bar(categories, days, color=colors_)
for i, d in enumerate(days):
    ax.text(i, d + 4, f"{d:.1f} days", ha="center", fontsize=8, color=INK)
ax.axhline(250, color=MUTED, lw=0.8, ls="--")
ax.text(2.45, 253, "250 trading days/yr", color=INK, fontsize=7, va="bottom", ha="right")
ax.set_ylabel("days per year")
ax.set_title("Empirical probability x 250 trading days", fontsize=9, loc="left")
ax.set_ylim(0, 275)
