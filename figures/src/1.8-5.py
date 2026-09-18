def F(t):
    return 0.2 * t - 0.01 * t**2

people = 1000
edges_min = np.arange(0, 11, 1.0)
edges_10s = np.arange(0, 10 + 1e-9, 1 / 6)
count_min = people * (F(edges_min[1:]) - F(edges_min[:-1]))
count_10s = people * (F(edges_10s[1:]) - F(edges_10s[:-1]))
ax.bar(edges_min[:-1], count_min, width=1.0, align="edge", color=MUTED, alpha=0.45,
       edgecolor="white", label="1-minute bars (people per bar)")
ax.bar(edges_10s[:-1], count_10s, width=1 / 6, align="edge", color=ACCENT,
       edgecolor="white", linewidth=0.3, label="10-second bars (people per bar)")
ts = np.linspace(0, 10, 200)
ax.plot(ts, people * (0.2 - 0.02 * ts), color=BAD, lw=2,
        label="people per minute = 1000 x f(t)")
ax.annotate("3-4 min bar: 130 people", xy=(3.5, 130), xytext=(4.6, 165),
            fontsize=7.5, color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9), arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.annotate("3:00-3:10 bar: 23 people\n23 / (1/6 min) = 138 per min", xy=(3.08, 23),
            xytext=(4.6, 60), fontsize=7.5, color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9),
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.set_xlim(0, 10)
ax.set_xticks(range(11))
ax.set_xlabel("Wait for the bus t (minutes)")
ax.set_ylabel("People")
ax.legend(fontsize=7, loc="upper right", frameon=False)
ax.set_title("Narrow bars hold fewer people; divided by width they all sit on one curve", loc="left")
