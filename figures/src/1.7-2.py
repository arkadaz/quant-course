labels = ["Naive answer\n(uses sensitivity)", "Correct P(Crash | Flag)\n(Bayes)"]
values = [90.0, 0.89]
bars = ax.bar(labels, values, color=[BAD, GOOD], width=0.55)
for b, v in zip(bars, values):
    ax.text(b.get_x() + b.get_width()/2, v + 2, f"{v:.2f}%", ha="center", fontsize=9, color=INK)
ax.set_ylim(0, 100)
ax.set_ylabel("Probability (%)")
ax.set_title("90% sensitivity is not 90% chance of a real crash", loc="left")
