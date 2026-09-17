ax.axis('off')
# Keep the labels above their matrices: the old returns label sat on the first value.
ax.text(0.21, 0.84, 'weights  (1 x 3)', fontsize=14, color=INK, ha='center', weight='bold')
ax.text(0.005, 0.50, '[', fontsize=30, color=INK, va='center')
for x, value in zip([0.065, 0.200, 0.350], ['0.5', '0.3', '-0.2']):
 ax.text(x, 0.50, value, fontsize=22, color=ACCENT, ha='center', va='center', family='monospace', weight='bold')
ax.text(0.425, 0.50, ']', fontsize=30, color=INK, va='center')
ax.text(0.452, 0.50, '×', fontsize=25, color=INK, ha='center', va='center')
ax.text(0.605, 0.84, 'returns  (3 x 1)', fontsize=14, color=INK, ha='center', weight='bold')
for y, value in zip([0.64, 0.49, 0.34], ['0.012', '-0.006', '0.004']):
 ax.text(0.475, y, '[', fontsize=24, color=INK, va='center')
 ax.text(0.605, y, value, fontsize=21, color=WARM, ha='center', va='center', family='monospace', weight='bold')
 ax.text(0.725, y, ']', fontsize=24, color=INK, va='center')
ax.text(0.780, 0.50, '=', fontsize=27, color=INK, ha='center', va='center')
ax.text(0.905, 0.56, '0.0034', fontsize=26, color=GOOD, ha='center', va='center', family='monospace', weight='bold')
ax.text(0.905, 0.34, 'portfolio return', fontsize=11, color=MUTED, ha='center', weight='bold')
ax.set_title('Dimensions determine what a multiplication means', loc='left', fontsize=14, color=INK, pad=14)
