categories = ["At or below -2%", "Inside (-2%, +2%]", "Above +2%"]
days = [4/252*252, 245/252*252, 3/252*252]
colors_ = [BAD, GOOD, WARM]
ax.bar(categories, days, color=colors_)
for i, d in enumerate(days):
    inside = d > 200
    ax.text(i, d - 18 if inside else d + 4, f"{d:.0f} days", ha="center", fontsize=8,
            color="white" if inside else INK)
ax.axhline(252, color=MUTED, lw=0.8, ls="--")
ax.text(2.45, 255, "252 trading days/yr", color=INK, fontsize=7, va="bottom", ha="right")
ax.set_ylabel("days per year")
ax.set_title("Empirical probability x 252 trading days", fontsize=9, loc="left")
ax.set_ylim(0, 275)
