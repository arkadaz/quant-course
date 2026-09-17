mu, sigma = 25.0, 661.0
N = np.linspace(1, 1500, 400)
mu_N = mu*N
sigma_N = sigma*np.sqrt(N)
ax.plot(N, mu_N, color=ACCENT, lw=2, label="μ·N (edge, linear)")
ax.plot(N, sigma_N, color=BAD, lw=2, label="σ·√N (noise, sqrt)")
N_cross = (sigma/mu)**2
ax.axvline(N_cross, color=MUTED, lw=1, ls=(0, (4, 3)))
ax.plot(N_cross, mu*N_cross, "o", color=INK, ms=6, zorder=4)
ax.annotate(f"crossover N≈{N_cross:.0f}", xy=(N_cross, mu*N_cross), xytext=(N_cross+30, mu*N_cross+7000),
            fontsize=8, color=INK)
ax.axvline(1000, color=GOOD, lw=1, ls=(0, (2, 2)))
ax.set_ylim(0, mu*1500*1.08)
ax.annotate("N=1,000 trades/yr", xy=(1000, mu*1500*1.0), xytext=(1000, mu*1500*1.0), fontsize=7.5, color=GOOD, ha="center", va="bottom")
ax.set_xlabel("Number of trades N")
ax.set_ylabel("Cumulative $ (mean or std dev)")
ax.set_title("Edge grows linearly, noise grows as sqrt(N) - crossover near N=699", loc="left")
ax.legend(loc="upper left", fontsize=8)
