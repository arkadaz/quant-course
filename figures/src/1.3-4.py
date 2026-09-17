w = np.linspace(0, 0.85, 200)
loss_rate = 0.85 - w
EX = 2*w - 1*loss_rate + 0*0.15
ax.plot(w, EX, color=ACCENT, lw=2.2)
ax.axhline(0, color=MUTED, lw=1)
w_be = 0.85/3
ax.plot(w_be, 0, "o", color=BAD, ms=7, zorder=3)
ax.annotate(f"breakeven w={w_be*100:.2f}%", xy=(w_be,0), xytext=(w_be-0.55, 0.22), fontsize=8, color=BAD, arrowprops=dict(arrowstyle="->", color=BAD, lw=0.8))
w_actual = 0.30
ex_actual = 2*w_actual - 1*(0.85-w_actual)
ax.plot(w_actual, ex_actual, "o", color=GOOD, ms=7, zorder=3)
ax.annotate(f"actual w=30%\nE[X]=+0.05R", xy=(w_actual, ex_actual), xytext=(w_actual+0.08, ex_actual+0.12), fontsize=8, color=GOOD, arrowprops=dict(arrowstyle="->", color=GOOD, lw=0.8))
ax.set_xlabel("Win rate w")
ax.set_ylabel("E[X] (R)")
ax.set_xlim(0, 0.85)
ax.set_title("Only 1.67 percentage points separate the actual edge from breakeven", loc="left")
