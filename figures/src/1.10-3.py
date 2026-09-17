S0, mu, sigma, T = 120.0, 0.15, 0.55, 1.0
x = np.linspace(1, 420, 2000)
scale = S0*np.exp((mu - sigma**2/2)*T)
pdf = stats.lognorm.pdf(x, s=sigma*np.sqrt(T), scale=scale)
distribution(ax, x, {"NVDA S_T (lognormal)": pdf}, title="NVDA in one year: median near spot, mean far above", xlabel="Price ($)")
median = S0*np.exp((mu-sigma**2/2)*T)
mean = S0*np.exp(mu*T)
ax.axvline(median, color=GOOD, lw=1.6, ls=(0, (4, 3)))
ax.axvline(mean, color=WARM, lw=1.6, ls=(0, (4, 3)))
ax.axvline(S0, color=MUTED, lw=1, ls=(0, (2, 2)))
mask_lo = x <= median
ax.fill_between(x[mask_lo], pdf[mask_lo], color=BAD, alpha=0.28)
ax.annotate(f"median ${median:.2f}", xy=(median, pdf.max()*0.55), xytext=(median-100, pdf.max()*0.8),
            fontsize=7.5, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.annotate(f"mean ${mean:.2f}", xy=(mean, pdf.max()*0.28), xytext=(mean+15, pdf.max()*0.55),
            fontsize=7.5, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.annotate(f"spot ${S0:.0f}", xy=(S0, pdf.max()*0.06), fontsize=7.5, color=INK)
ax.set_xlim(0, 420)
