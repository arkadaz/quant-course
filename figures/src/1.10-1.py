S0, mu, sigma = 120.0, 0.15, 0.55
m = mu - sigma**2/2
R = np.linspace(m - 3*sigma, m + 3*sigma, 400)
S = S0*np.exp(R)
ax.plot(R, S, color=ACCENT, lw=2, zorder=2)
marks = [m-2*sigma, m-sigma, m, m+sigma, m+2*sigma]
labels = [r'$m - 2\sigma$', r'$m - \sigma$', r'$m$', r'$m + \sigma$', r'$m + 2\sigma$']
ymax = S0*np.exp(m+3*sigma)
for r, lbl in zip(marks, labels):
    s = S0*np.exp(r)
    ax.plot([r, r], [0, s], color=MUTED, lw=0.8, ls=(0, (3, 2)), zorder=1)
    ax.plot([R.min(), r], [s, s], color=MUTED, lw=0.6, ls=(0, (2, 2)), zorder=1)
    ax.plot(r, s, "o", ms=5, color=WARM, zorder=3)
    ax.annotate(lbl, xy=(r, 0), xytext=(0, 6), textcoords="offset points",
                ha="center", va="bottom", fontsize=7.5, color=INK)
ax.set_ylim(0, ymax*1.05)
ax.set_xlabel(r'Log return $R$ (equal $1\sigma$ steps)')
ax.set_ylabel(r'Price $S = S_0 e^R$ ($)')
ax.set_title("Equal steps in R, unequal steps in S — exponential stretches the upside", loc="left")
