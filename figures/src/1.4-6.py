mu, sigma = 0.0, 1.0
for k, colour in [(1, GOOD), (2, WARM), (3, BAD)]:
    ax.plot([mu-k*sigma, mu+k*sigma], [k, k], color=colour, lw=5, solid_capstyle="butt")
    ax.text(mu, k+0.12, f"μ ± {k}σ", ha="center", fontsize=8, color=INK)
ax.axvline(mu, color=INK, lw=1, ls="--")
ax.set_yticks([1,2,3], ["1σ", "2σ", "3σ"])
ax.set_xlabel("Outcome units")
ax.set_title("Standard deviation σ is a spread ruler", fontsize=9, loc="left")
