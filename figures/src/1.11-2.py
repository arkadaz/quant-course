s = np.sqrt(1/3)
x = np.linspace(-6, 6, 900)
normal_pdf = stats.norm.pdf(x)
t_pdf = stats.t.pdf(x/s, 3) / s
ax.plot(x, normal_pdf, color=MUTED, lw=1.6, ls=(0, (4, 2)), label="Normal, variance 1")
ax.plot(x, t_pdf, color=BAD, lw=2, label="Student-t(3), variance 1")
z = -1.855
mask = x <= z
ax.fill_between(x[mask], t_pdf[mask], color=BAD, alpha=0.30)
ax.fill_between(x[mask], normal_pdf[mask], color=MUTED, alpha=0.35)
ax.axvline(z, color=INK, lw=0.8, ls=(0, (2, 2)))
ax.annotate("scaled t(3): 2.44%", xy=(-5.4, 0.11), fontsize=8, color=BAD)
ax.annotate("normal: 3.18%", xy=(-5.4, 0.045), fontsize=8, color=INK)
ax.set_xlim(-6, 6)
ax.set_xlabel("Standardized return")
ax.set_ylabel("Density")
ax.legend(loc="upper right", fontsize=8)
ax.set_title("At z=-1.855, equal-variance t(3) is below Normal", loc="left")
