# Portfolio return as a waterfall of weight x return contributions (the product itself lives in the page as LaTeX).
c = np.array([0.0060, -0.0018, -0.0008])
starts = np.array([0.0, 0.0060, 0.0042])
labels = ['asset 1\nw 0.50, r +1.2%', 'asset 2\nw 0.30, r -0.6%', 'asset 3\nw -0.20, r +0.4%', 'portfolio']
for i, (s0, v) in enumerate(zip(starts, c)):
    ax.bar(i, v, bottom=s0, color=GOOD if v > 0 else BAD, width=0.6)
    ax.text(i, s0 + v + (0.00015 if v > 0 else -0.00015), f'{v*100:+.2f}%', ha='center', va='bottom' if v > 0 else 'top', fontsize=10)
ax.bar(3, 0.0034, color=ACCENT, width=0.6)
ax.text(3, 0.0034 + 0.00015, '+0.34%', ha='center', va='bottom', fontsize=11, weight='bold')
for i, top in enumerate([0.0060, 0.0042, 0.0034]):
    ax.plot([i + 0.3, i + 0.7], [top, top], color=MUTED, lw=0.8, ls=':')
ax.axhline(0, color=MUTED, lw=0.8)
ax.set_xticks(range(4), labels)
ax.set_ylim(-0.0004, 0.0072)
ax.yaxis.set_major_formatter(lambda y, _: f'{y*100:.1f}%')
ax.set_ylabel('Contribution to portfolio return')
ax.set_title('Each weight times its return, stacked: the row-times-column product', loc='left')
