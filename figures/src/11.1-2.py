T = np.linspace(0, 60, 601)
drift = 0.0808 * T * 100
noise = 2 * 0.28 * np.sqrt(T) * 100
ax.plot(T, drift, color=ACCENT, lw=2, label='log drift: 8.08% x years')
ax.plot(T, noise, color=WARM, lw=2, label='2 SD of noise: 2 x 28% x sqrt(years)')
tx = (2 * 0.28 / 0.0808) ** 2
ax.scatter([tx], [0.0808 * tx * 100], color=GOOD, zorder=3)
ax.annotate(f'cross at {tx:.1f} years', (tx, 0.0808 * tx * 100), xytext=(10, -22), textcoords='offset points', fontsize=8)
ax.set_xlabel('Horizon (years)')
ax.set_ylabel('Percent (log return)')
ax.set_title('Drift grows like t, noise like sqrt(t)', loc='left')
ax.legend(loc='upper left', fontsize=8)
