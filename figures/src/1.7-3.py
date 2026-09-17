pi = np.linspace(0.0005, 0.20, 400)
sens, fpr = 0.90, 0.10
post = (sens*pi) / (sens*pi + fpr*(1-pi))
ax.plot(pi*100, post*100, color=ACCENT, lw=2.2)
pi0 = 0.001
post0 = (sens*pi0)/(sens*pi0 + fpr*(1-pi0))
ax.plot(pi0*100, post0*100, "o", color=BAD, ms=6, zorder=3)
ax.annotate(f"base rate 0.1% -> {post0*100:.2f}%", xy=(pi0*100, post0*100),
            xytext=(pi0*100+2, post0*100+15), fontsize=7.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.set_xlabel("Base rate P(Crash) (%)")
ax.set_ylabel("Posterior P(Crash | Flag) (%)")
ax.set_title("Same 90% sensitivity, same 10% false-alarm rate - posterior lives on the base rate", loc="left")
