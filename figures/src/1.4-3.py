mu_a, sig_a = 50000.0, 41800.0
x = np.linspace(mu_a - 4*sig_a, mu_a + 4*sig_a, 500)
pdf = stats.norm.pdf(x, mu_a, sig_a)
distribution(ax, x, {"Annual P&L (CLT normal approx)": pdf},
             title="11.6% of years still close negative, despite a genuine positive edge",
             xlabel="Annual P&L ($)")
mask = x <= 0
ax.fill_between(x[mask], pdf[mask], color=BAD, alpha=0.35)
ax.axvline(0, color=BAD, lw=1.4, ls=(0, (4, 3)))
ax.axvline(mu_a, color=GOOD, lw=1.2, ls=(0, (2, 2)))
ax.annotate("P(loss year) ≈ 11.6%", xy=(0, pdf.max()*0.12), xytext=(-4.3*sig_a, pdf.max()*0.55),
            fontsize=8, color=BAD, arrowprops=dict(arrowstyle="->", color=BAD, lw=0.9))
