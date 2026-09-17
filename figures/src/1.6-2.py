lam = 3
r = np.arange(0, 12)
pmf = stats.poisson.pmf(r, lam)
colours = [ACCENT] * len(r)
colours[0] = GOOD
colours[3] = WARM
ax.bar(r, pmf, color=colours, width=0.6)
for i in (0, 3):
    ax.annotate(f"{pmf[i]*100:.2f}%", xy=(i, pmf[i]), xytext=(0, 4),
                textcoords="offset points", ha="center", fontsize=8, color=INK)
ax.set_xlabel("Defaults r in one year")
ax.set_ylabel("P(X=r)")
ax.set_xticks(r)
ax.set_title("Poisson(λ=3): a clean year (r=0) vs the modal year (r=3)", loc="left")
