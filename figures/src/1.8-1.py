rng = np.random.default_rng(0)
sigma = 0.0189
x_data = rng.normal(0, sigma, 3000)
for n_bins, c in zip([8, 32, 128], [MUTED, ACCENT, INK]):
    ax.hist(x_data, bins=n_bins, density=True, histtype="step", color=c, lw=1.6, label=f"{n_bins} bins")
xs = np.linspace(-0.07, 0.07, 400)
pdf = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-xs**2/(2*sigma**2))
ax.plot(xs, pdf, color=BAD, lw=2.2, label="limit: smooth f(x)")
ax.set_xlabel("Daily return x (decimal)")
ax.set_ylabel("Density")
ax.set_title("More, narrower bins -> histogram outline becomes the PDF", loc="left")
ax.legend(fontsize=7, loc="upper right")
ax.set_xlim(-0.07, 0.07)
