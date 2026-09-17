sigma = 0.0189
xs = np.linspace(-0.07, 0.07, 400)
pdf = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-xs**2/(2*sigma**2))
cdf = stats.norm.cdf(xs, 0, sigma)
ax.plot(xs, pdf, color=ACCENT, lw=2, label="f(x): density (left)")
x_cut = 0.01
mask = xs <= x_cut
ax.fill_between(xs[mask], pdf[mask], color=ACCENT, alpha=0.3)
ax2 = ax.twinx()
ax2.plot(xs, cdf, color=INK, lw=2, label="F(x): cumulative (right)")
F_cut = stats.norm.cdf(x_cut, 0, sigma)
ax2.plot(x_cut, F_cut, "o", color=WARM, ms=6, zorder=5)
ax2.annotate(f"F({x_cut})={F_cut:.3f}", xy=(x_cut, F_cut), xytext=(x_cut+0.012, F_cut-0.12),
             fontsize=7.5, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.set_xlabel("Daily return x (decimal)")
ax.set_ylabel("f(x)", color=ACCENT)
ax2.set_ylabel("F(x)", color=INK)
ax.set_title("Shaded area under f up to x equals the height of F at x", loc="left")
ax.set_xlim(-0.07, 0.07)
