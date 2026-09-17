data = np.zeros((6, 6), dtype=int)
sums = np.zeros((6, 6), dtype=int)
for i in range(6):
    for j in range(6):
        y1, y2 = i + 1, j + 1
        s = y1 + y2
        sums[i, j] = s
        inA, inB = y1 >= 4, s >= 8
        data[i, j] = 2 if (inA and inB) else (1 if inB else 0)
from matplotlib.colors import ListedColormap
cmap = ListedColormap([MUTED, ACCENT, GOOD])
ax.imshow(data, cmap=cmap, vmin=0, vmax=2, alpha=0.9)
for i in range(6):
    for j in range(6):
        ax.text(j, i, str(sums[i, j]), ha="center", va="center", fontsize=8,
                color="white" if data[i, j] else INK)
ax.plot([-0.5, 5.5, 5.5, -0.5, -0.5], [2.5, 2.5, 5.5, 5.5, 2.5],
        color=WARM, lw=1.6, ls=(0, (4, 2)))
ax.text(5.5, 2.25, "prior region A: Y1>=4 (18 cells)", color=WARM, fontsize=7, ha="right")
ax.set_xticks(range(6), [str(k) for k in range(1, 7)])
ax.set_yticks(range(6), [str(k) for k in range(1, 7)])
ax.set_xlabel("Y2 (second die)")
ax.set_ylabel("Y1 (first die)")
ax.set_title("Grey = deleted once sum>=8 is known; green = survives AND first die>=4", loc="left")
