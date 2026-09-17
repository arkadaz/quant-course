n = np.arange(35, 53)
residual = (1.10*10_000_000 - n*250_000)/1000
ax.bar(n, residual, color=[GOOD if abs(x-44) <= 0 else ACCENT for x in n], width=0.7)
ax.axhline(0, color=MUTED, lw=1)
ax.set_xlabel('Short ES contracts')
ax.set_ylabel('Residual market exposure (USD thousands)')
ax.set_title('Integer hedge size leaves a small notional remainder', loc='left')
