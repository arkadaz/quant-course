betas = np.linspace(0.7, 1.5, 81)
res = (betas*10_000_000 - 44*250_000)/1000
ax.plot(betas, res, color=ACCENT, lw=2.1)
ax.axhline(0, color=MUTED, lw=1)
ax.axvline(1.10, color=WARM, lw=1.2, ls=(0,(4,3)), label='Assumed beta 1.10')
ax.set_xlabel('Actual portfolio beta')
ax.set_ylabel('Residual exposure (USD thousands)')
ax.set_title('A stale beta quietly brings market risk back', loc='left')
ax.legend(loc='best')
