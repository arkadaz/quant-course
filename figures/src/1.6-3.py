rng = np.random.default_rng(0)
lam = 3
years = np.arange(1, 21)
counts = rng.poisson(lam, size=20)
colours = [GOOD if c == 0 else (BAD if c >= 6 else ACCENT) for c in counts]
ax.bar(years, counts, color=colours, width=0.65)
ax.axhline(lam, color=MUTED, lw=1, ls=(0, (4, 3)))
ax.annotate("λ = 3 (long-run average)", xy=(20, lam), xytext=(0, 6),
            textcoords="offset points", ha="right", fontsize=7.5, color=MUTED)
ax.set_xlabel("Simulated year")
ax.set_ylabel("Defaults that year")
ax.set_xticks(years)
ax.set_title("Same λ=3 every year, a different count every single time", loc="left")
