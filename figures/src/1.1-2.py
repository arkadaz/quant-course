xs_known = np.array([-4, -3, -2, 0, 2, 3, 4])
Fs_known = np.array([0.002, 0.010, 0.025, 0.470, 0.978, 0.995, 0.999])
x_fine = np.linspace(-4, 4, 400)
F_fine = np.interp(x_fine, xs_known, Fs_known)
ax.plot(x_fine, F_fine, color=ACCENT, lw=2)
highlight_x = [-3, -2, 0, 2]
highlight_F = [0.010, 0.025, 0.470, 0.978]
for hx, hF in zip(highlight_x, highlight_F):
    ax.plot([hx, hx], [0, hF], color=MUTED, lw=0.7, ls=":")
    ax.plot([-4, hx], [hF, hF], color=MUTED, lw=0.7, ls=":")
    ax.plot(hx, hF, "o", color=BAD, ms=5, zorder=5)
    ax.annotate(f"{hF:.3f}", xy=(hx, hF), xytext=(hx+0.15, hF-0.07), fontsize=7, color=INK)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 1.05)
ax.set_xlabel("daily portfolio return, x (%)")
ax.set_ylabel("F(x) = P(X <= x)")
ax.set_title("Four points, one full CDF", fontsize=9, loc="left")
