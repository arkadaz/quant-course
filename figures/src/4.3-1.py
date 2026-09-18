# Each factor exposure split into the piece every position contributes: C[i, j] = A[i, j] w[j].
A = np.array([[1.0, 0.8, 0.6], [0.3, 0.5, 0.2], [0.1, 0.2, 0.4]])
w = np.array([2, -1, 1])
C = A * w
x = np.arange(3); bw = 0.22
for j, (name, col) in enumerate(zip(['AAPL', 'MSFT', 'JPM'], [ACCENT, WARM, GOOD])):
    ax.bar(x + (j - 1) * bw, C[:, j], bw, color=col, label=f'{name}  {w[j]:+d}M')
y = C.sum(axis=1)
ax.scatter(x + 0.42, y, color=INK, marker='D', s=36, zorder=3, label='exposure = row sum')
for i, v in enumerate(y):
    ax.text(i + 0.50, v, f'{v:.1f}', va='center', fontsize=10, weight='bold')
ax.axhline(0, color=MUTED, lw=0.8)
ax.set_xticks(x, ['market', 'quality', 'rates'])
ax.set_xlim(-0.5, 2.85)
ax.set_ylabel('USD million')
ax.legend(fontsize=8, ncol=2, loc='upper right')
ax.set_title('Every position feeds every factor: loading x position, then add', loc='left')
