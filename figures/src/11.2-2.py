v = np.linspace(0, .8, 300)
g = .14 - .5 * v * v
ax.plot(v * 100, g * 100, color=BAD, lw=2, label='median growth 14% - vol^2 / 2')
ax.axhline(14, color=MUTED, ls='--', label='drift 14%')
ax.axhline(0, color=INK, lw=.8)
ax.scatter([32], [8.88], color=GOOD, zorder=3)
ax.annotate('vol 32% -> 8.88%', (32, 8.88), xytext=(8, 4), textcoords='offset points', fontsize=8)
vz = np.sqrt(2 * .14) * 100
ax.scatter([vz], [0], color=BAD, zorder=3)
ax.annotate(f'vol {vz:.1f}% -> 0%', (vz, 0), xytext=(8, 6), textcoords='offset points', fontsize=8)
ax.set_xlabel('Annual volatility (%)')
ax.set_ylabel('Median log-growth (%/year)')
ax.set_title('Volatility drag grows with the square', loc='left')
ax.legend(loc='lower left', fontsize=8)
