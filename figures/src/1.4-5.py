x = np.linspace(-4, 4, 300)
for sigma, colour, label in [(0.8, GOOD, "σ=0.8"), (1.8, BAD, "σ=1.8")]:
    ax.plot(x, stats.norm.pdf(x, 0, sigma), color=colour, lw=2, label=label)
ax.axvline(0, color=MUTED, lw=1, ls="--")
ax.set_xlabel("Outcome X (same mean μ=0)")
ax.set_ylabel("Density")
ax.set_title("Same mean, different variance changes tail exposure", fontsize=9, loc="left")
ax.legend(fontsize=7)
