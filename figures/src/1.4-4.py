edge_ratio = 25.0/661.0
Ns = np.array([20, 100, 250, 1000])
z = edge_ratio*np.sqrt(Ns)
p_loss = (1 - stats.norm.cdf(z))*100
colours = [BAD if n < 699 else GOOD for n in Ns]
ax.bar([str(n) for n in Ns], p_loss, color=colours)
for i, p in enumerate(p_loss):
    ax.text(i, p + 1.2, f"{p:.1f}%", ha="center", fontsize=8, color=INK)
ax.set_xlabel("Number of trades N (same strategy, same edge, same σ)")
ax.set_ylabel("P(cumulative result < 0)  (%)")
ax.set_title("Surviving the first N trades is a coin flip long before the edge shows up", loc="left")
ax.set_ylim(0, 55)
