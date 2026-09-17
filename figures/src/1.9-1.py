mu, sigma = 0.04, 1.1
x = np.linspace(mu-4*sigma, mu+4*sigma, 600)
pdf = stats.norm.pdf(x, mu, sigma)
distribution(ax, x, {"Portfolio daily return": pdf}, title="1sigma=\$550K, 2sigma=\$1.1M, 3sigma=\$1.65M on a \$50M book", xlabel="Daily return (%)")
bands = [(3, 0.10, BAD), (2, 0.18, WARM), (1, 0.30, GOOD)]
for k, alpha, colour in bands:
    mask = (x >= mu-k*sigma) & (x <= mu+k*sigma)
    ax.fill_between(x[mask], pdf[mask], color=colour, alpha=alpha, zorder=2)
for k, dollar in [(1, "0.55M"), (2, "1.1M"), (3, "1.65M")]:
    ax.axvline(mu-k*sigma, color=MUTED, lw=0.7, ls=(0, (2, 2)))
    ax.annotate(f"-{k}sigma=\${dollar}", xy=(mu-k*sigma, 0), xytext=(0, 6+(k-1)*10),
                textcoords="offset points", ha="center", va="bottom", fontsize=6.8, color=INK)
ax.legend(loc="upper right", fontsize=7.5)
