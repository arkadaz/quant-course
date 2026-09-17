mu, sigma = 0.04, 1.1
x = np.linspace(mu-6*sigma, mu+4*sigma, 800)
pdf = stats.norm.pdf(x, mu, sigma)
distribution(ax, x, {"Portfolio daily return": pdf}, title="Tail thins fast: loss doubles (2%->4%), probability falls 265x", xlabel="Daily return (%)")
mask2 = x <= -2.0
mask4 = x <= -4.0
ax.fill_between(x[mask2], pdf[mask2], color=WARM, alpha=0.45, label="R < -2% (3.18%)")
ax.fill_between(x[mask4], pdf[mask4], color=BAD, alpha=0.85, label="R < -4% (0.012%)")
ax.axvline(-2.0, color=WARM, lw=1, ls=(0, (4, 3)))
ax.axvline(-4.0, color=BAD, lw=1, ls=(0, (4, 3)))
ax.legend(loc="upper left", fontsize=7.5)
