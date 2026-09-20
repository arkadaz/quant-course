# The solver's answer read back against the labelled limits of the prospectus.
w = np.array([0.25, 0.15, 0.25, 0.25, 0.10])
x = np.arange(5)
cols = [ACCENT, ACCENT, GOOD, GOOD, GOOD]
ax.bar(x, w, color=cols, width=0.6)
for i, v in enumerate(w):
    ax.text(i, v + 0.008, f'{v:.2f}', ha='center', fontsize=10)
ax.axhline(0.25, color=BAD, ls='--', lw=1.2, label='single-asset cap 0.25')
ax.axvspan(-0.45, 1.45, color=ACCENT, alpha=0.08, label='assets 1 + 2 capped at 0.40 (uses 0.40)')
ax.set_xticks(x, [f'asset {i+1}' for i in x])
ax.set_ylim(0, 0.42)
ax.set_ylabel('weight')
ax.legend(fontsize=8, loc='upper right', ncol=1, framealpha=0.95)
ax.set_title("The answer is only tradable with its labels: weights vs limits", loc='left')
