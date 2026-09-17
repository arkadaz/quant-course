sigma = 0.0189
x0 = 0.012345
xs = np.linspace(-0.07, 0.07, 400)
pdf = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-xs**2/(2*sigma**2))
ax.plot(xs, pdf, color=INK, lw=2)
for w, c, lbl in [(0.008, MUTED, "width=0.0080"), (0.0008, ACCENT, "width=0.0008")]:
    mask = (xs >= x0-w/2) & (xs <= x0+w/2)
    ax.fill_between(xs[mask], pdf[mask], color=c, alpha=0.6, label=lbl)
f_x0 = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-x0**2/(2*sigma**2))
ax.plot(x0, f_x0, "o", color=BAD, ms=6, zorder=5, label="width -> 0: area -> 0")
ax.set_xlabel("Daily return x (decimal)")
ax.set_ylabel("Density f(x)")
ax.set_title("Narrower interval -> shaded area (probability) shrinks toward zero", loc="left")
ax.legend(fontsize=7, loc="upper left")
ax.set_xlim(-0.07, 0.07)
