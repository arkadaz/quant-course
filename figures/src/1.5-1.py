n, p = 10, 0.5
r = np.arange(0, n+1)
pmf = stats.binom.pmf(r, n, p)
colors = [BAD if k >= 8 else ACCENT for k in r]
ax.bar(r, pmf, color=colors, width=0.6, zorder=2)
for k, v in zip(r, pmf):
    if k >= 8:
        ax.annotate(f"{v:.3f}", xy=(k, v), xytext=(0, 4), textcoords="offset points",
                    ha="center", fontsize=7.5, color=INK)
tail = pmf[8:].sum()
ax.annotate(f"tail P(X>=8) = {tail*100:.2f}%", xy=(9, pmf[8]), xytext=(5.2, pmf.max()*0.75),
            fontsize=8.5, color=BAD, arrowprops=dict(arrowstyle="->", color=BAD, lw=0.9))
ax.set_xticks(r)
ax.set_xlabel("Years beating the S&P 500 out of 10 (r)")
ax.set_ylabel("P(X = r)")
ax.set_title("Binomial(n=10, p=0.5): a 'good' record is common under pure luck", loc="left")
