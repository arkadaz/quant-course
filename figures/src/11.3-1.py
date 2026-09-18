m, s = 0.10 - 0.25**2 / 2, 0.25
for S, col in ((100, ACCENT), (20, WARM)):
    d = np.linspace(-S * 0.6, S * 1.2, 800)
    R = 1 + d / S
    pdf = stats.lognorm.pdf(R, s=s, scale=np.exp(m)) / S
    sd = S * np.exp(0.10) * np.sqrt(np.exp(0.0625) - 1)
    ax.plot(d, pdf, color=col, lw=2, label=f'start {S} USD: SD {sd:.2f} USD')
ax.axvline(0, color=MUTED, lw=.8)
ax.set_xlabel('Dollar change over one year (USD)')
ax.set_ylabel('Density')
ax.set_title('Same ratio, very different dollar spread', loc='left')
ax.legend(fontsize=8)
