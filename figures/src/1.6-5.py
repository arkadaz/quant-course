r = np.arange(0, 22)
for lam, colour in [(1, ACCENT), (4, WARM), (10, GOOD)]:
    ax.plot(r, stats.poisson.pmf(r, lam), marker="o", ms=3, lw=1.8, color=colour, label=f"Poisson(λ={lam})")
ax.set_xlabel("Event count r")
ax.set_ylabel("P(X=r)")
ax.set_title("Poisson PMF shifts with the event rate λ", fontsize=9, loc="left")
ax.legend(fontsize=7)
