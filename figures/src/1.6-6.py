r = np.arange(0, 10)
pmf = stats.poisson.pmf(r, 3)
colors = [ACCENT] * len(r)
colors[2] = WARM
colors[3] = WARM
ax.bar(r, pmf, color=colors, width=0.6)
for i in [2, 3]:
    ax.annotate(f"{pmf[i]*100:.2f}%", xy=(i, pmf[i]), xytext=(0, 5), textcoords="offset points", ha="center", fontsize=8, color=INK)
ax.set_xlabel("Default count r")
ax.set_ylabel("P(X=r)")
ax.set_title("Poisson(3) has two equal modes: r=2 and r=3", fontsize=9, loc="left")
