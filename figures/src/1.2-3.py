n = np.arange(1, 8)
p_streak = 0.55 ** n
colors = [BAD if k == 5 else MUTED for k in n]
ax.bar(n, p_streak, color=colors, width=0.6)
for k, v in zip(n, p_streak):
    ax.text(k, v + 0.012, f"{v*100:.1f}%", ha="center", fontsize=7.8, color=INK)
ax.axvline(5, color=BAD, lw=0.8, ls=(0, (4, 3)))
ax.set_xticks(n)
ax.set_xlabel("n consecutive losses")
ax.set_ylabel(r"$P(\text{n losses in a row}) = 0.55^n$")
ax.set_title("Five losses in a row: about 1 in 20 sets, if trades stay independent", loc="left")
