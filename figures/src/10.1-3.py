mu, sig, dt = 0.12, 0.28, 1 / 252
z = np.array([0.83, -1.42, 0.05])
s = 100 * np.exp(np.cumsum((mu - sig**2 / 2) * dt + sig * np.sqrt(dt) * z))
s = np.r_[100, s]
x = np.arange(4)
ax.plot(x, s, marker='o', color=ACCENT)
for i, v in enumerate(s):
    lab = 'start' if i == 0 else f'Z={z[i-1]:+.2f}'
    ax.annotate(f'{v:.2f}\n{lab}', (i, v), xytext=(0, 10) if i != 2 else (0, -28), textcoords='offset points', ha='center', fontsize=8)
ax.set_ylim(98.0, 102.6)
ax.set_xticks(x, ['Start', 'Day 1', 'Day 2', 'Day 3'])
ax.set_ylabel('Price (USD/share)')
ax.set_title('Each day needs only today\'s price and one new Z', loc='left')
