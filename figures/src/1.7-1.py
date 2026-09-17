branches = [
    ("Crash", 0.001, [("Flag", 0.90, []), ("No flag", 0.10, [])]),
    ("No crash", 0.999, [("Flag", 0.10, []), ("No flag", 0.90, [])]),
]
prob_tree(ax, "Today", branches,
          title="Two roads lead to Flag - only the top one is a real crash")
ax.text(3.3, 1.5, "P(Crash and Flag) = 0.09%", fontsize=7.5, color=GOOD, ha="right", va="top")
ax.text(3.3, 1.2, "P(No crash and Flag) = 9.99%", fontsize=7.5, color=BAD, ha="right", va="top")
ax.text(3.3, 0.9, "P(Flag) = 10.08% total", fontsize=7.5, color=INK, ha="right", va="top")
