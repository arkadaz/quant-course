rng = np.random.default_rng(0)
n_trades = 1000
outcomes = np.array([2.0, -1.0, 0.0])
probs = np.array([0.30, 0.55, 0.15])
n_show = 6
sims = rng.choice(outcomes, size=(n_show, n_trades), p=probs)
cum = np.cumsum(sims, axis=1) * 1000.0
t = np.arange(1, n_trades+1)
for i in range(n_show):
    ax.plot(t, cum[i], color=ACCENT, alpha=0.35, lw=1.0)
expected_line = t * 0.05 * 1000.0
ax.plot(t, expected_line, color=WARM, lw=2.2, label="E[X] x n x $1,000/R")
ax.axhline(0, color=MUTED, lw=0.8)
ax.set_xlabel("Trade number n")
ax.set_ylabel("Cumulative P&L ($)")
ax.legend(loc="upper left", fontsize=8)
ax.set_title("Any single path wanders - the expected line is the only thing computable in advance", loc="left")
