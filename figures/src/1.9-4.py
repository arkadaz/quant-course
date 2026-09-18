mu, sigma = 0.04, 1.1
x = np.linspace(mu-8*sigma, mu+8*sigma, 800)
pdf = stats.norm.pdf(x, mu, sigma)
distribution(ax, x, {"Normal model of daily return": pdf}, title="Black Monday 1987 sits ~20 sigma out -- off this axis entirely", xlabel="Daily return (%)")
ax.axvline(mu-8*sigma, color=BAD, lw=1.4, ls=(0, (4, 3)))
ax.annotate("Black Monday 1987, Dow: -22.6%\nz = -20.6, far off this axis", xy=(mu-8*sigma, pdf.max()*0.05),
            xytext=(mu-7.5*sigma, pdf.max()*0.55), fontsize=7.5, color=BAD,
            arrowprops=dict(arrowstyle="->", color=BAD, lw=1))
ax.set_xlim(mu-8.5*sigma, mu+8*sigma)
