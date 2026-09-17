xs = [-5, -1, 0, 2]
ps = [0.0, 0.55, 0.15, 0.30]
colors = [BAD, BAD, MUTED, GOOD]
for xi, pi, c in zip(xs, ps, colors):
    if pi == 0.0:
        ax.bar(xi, 0.06, width=0.6, facecolor="none", edgecolor=BAD, linestyle=(0, (4, 3)), linewidth=1.4)
        ax.text(xi, 0.10, "never in\nthe table", ha="center", fontsize=7.2, color=BAD)
    else:
        ax.bar(xi, pi, width=0.6, color=c)
        ax.text(xi, pi + 0.02, f"{pi:.2f}", ha="center", fontsize=8.2, color=INK)
ax.set_xticks(xs, ["-5R (gap)", "-1R", "0R", "+2R"])
ax.set_ylim(0, 0.70)
ax.set_xlabel("Trade outcome X (R-multiples)")
ax.set_ylabel("PMF p(x)")
ax.set_title("Illustration: buy at 100, planned stop 98, gap fill 90 gives -5R", loc="left")
