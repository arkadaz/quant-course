from matplotlib.patches import Circle, FancyArrowPatch
ax.axis('off')
pts = [(.15, .55, 'Price\nfalls', BAD), (.38, .80, 'Margin\ncall', WARM), (.62, .55, 'Forced\nsale', BAD), (.38, .25, 'Liquidity\ndries up', WARM)]
for x, y, label, col in pts:
    ax.add_patch(Circle((x, y), .11, color=col, alpha=.25))
    ax.text(x, y, label, ha='center', va='center', fontsize=9)
for i in range(4):
    a, b = np.array(pts[i][:2]), np.array(pts[(i + 1) % 4][:2])
    d = (b - a) / np.linalg.norm(b - a)
    ax.add_patch(FancyArrowPatch(tuple(a + .12 * d), tuple(b - .12 * d), arrowstyle='->', mutation_scale=14, color=INK))
ax.set_xlim(0, .8); ax.set_ylim(0, 1); ax.set_aspect('equal')
ax.set_title('Stylized leverage–liquidity feedback', loc='left')
