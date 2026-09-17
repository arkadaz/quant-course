labels = ["Prior crash", "Prior no crash", "Posterior crash", "Posterior no crash"]
vals = [0.001, 0.999, 0.00893, 0.99107]
ax.bar(labels, vals, color=[BAD, MUTED, BAD, GOOD])
ax.set_ylabel("Probability")
ax.set_ylim(0, 1.05)
ax.set_title("Same flag, different information set: prior → posterior", fontsize=9, loc="left")
ax.tick_params(axis="x", rotation=18)
