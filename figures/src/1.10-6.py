mu, sigma, s0 = 0.15, 0.55, 120.0
m = mu - sigma**2/2
marks = [m-3*sigma, m, m+3*sigma]
prices = [s0*np.exp(v) for v in marks]
xs = np.linspace(0, max(prices)*1.08, 300)
pdf = stats.lognorm.pdf(xs, s=sigma, scale=s0*np.exp(m))
ax.plot(xs, pdf, color=ACCENT, lw=2)
for v, price, colour in zip(marks, prices, [BAD, MUTED, GOOD]):
    ax.axvline(price, color=colour, lw=1.2, ls="--")
    ax.text(price, pdf.max()*0.75, f"{v:.2f} log return", rotation=90, ha="right", fontsize=7, color=INK)
ax.set_xlabel("NVDA terminal price S_T (USD)")
ax.set_ylabel("Lognormal density")
ax.set_title("Three-sigma marks after exponentiation", fontsize=9, loc="left")
