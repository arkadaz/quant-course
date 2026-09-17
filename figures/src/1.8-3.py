sigma = 0.0189
xs = np.linspace(-0.07, 0.07, 400)
pdf = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-xs**2/(2*sigma**2))
ax.plot(xs, pdf, color=ACCENT, lw=2.2)
ax.axhline(1.0, color=BAD, lw=1.2, ls=(0, (4, 3)))
peak = pdf.max()
ax.annotate(f"peak f(0) = {peak:.2f}", xy=(0, peak), xytext=(0.018, peak*0.92),
            fontsize=8, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
ax.annotate("f(x) = 1", xy=(0.045, 1.0), xytext=(0.045, 3.0), fontsize=7.5, color=BAD)
ax.set_xlabel("Daily return x (decimal)")
ax.set_ylabel("Density f(x)")
ax.set_title("Density height exceeds 1 -- height is not a probability", loc="left")
ax.set_xlim(-0.07, 0.07)
