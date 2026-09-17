xs = np.array([-1, 0, 2])
ps = np.array([0.55, 0.15, 0.30])
cdf = np.cumsum(ps)
x_plot = np.linspace(-2.5, 3.5, 500)
y_plot = np.zeros_like(x_plot)
for xi, ci in zip(xs, cdf):
    y_plot[x_plot >= xi] = ci
ax.plot(x_plot, y_plot, color=ACCENT, lw=2.2, drawstyle="steps-post")
prev = 0.0
for xi, ci in zip(xs, cdf):
    ax.plot(xi, ci, "o", color=ACCENT, ms=6, zorder=3)
    ax.plot(xi, prev, "o", mfc="white", mec=ACCENT, ms=6, zorder=3)
    ax.text(xi, ci + 0.05, f"{ci:.2f}", ha="center", fontsize=8, color=INK)
    prev = ci
ax.set_ylim(0, 1.18)
ax.set_xlabel("x (R-multiples)")
ax.set_ylabel(r"$F(x) = P(X \leq x)$")
ax.set_title("CDF is a staircase for a discrete variable, always ending at 1.00", loc="left")
