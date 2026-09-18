G = 0.0941487
theta_vol_day = 3.3215668 / 365
x = np.linspace(-1.2, 1.2, 481)
pnl = 10_000 * (0.5 * G * x**2 - theta_vol_day)
ax.plot(x, pnl, color=ACCENT, lw=2, label='long call, delta hedged')
ax.plot(x, -pnl, color=BAD, lw=1.5, ls='--', label='short call, delta hedged')
ax.axhline(0, color=INK, lw=.8)
be = 0.24 * 35 / np.sqrt(365)
for sgn in (-1, 1):
    ax.axvline(sgn * be, color=MUTED, lw=1, ls=':')
ax.text(-1.18, 120, f'breakeven: move of {be:.2f} USD either way', fontsize=8)
ax.scatter([1.0], [10_000 * (0.5 * G - theta_vol_day)], color=GOOD, zorder=3)
ax.annotate('1 USD move: +380', (1.0, 10_000 * (0.5 * G - theta_vol_day)), xytext=(-95, 5), textcoords='offset points', fontsize=8)
ax.set_xlabel('Stock move in one day (USD)')
ax.set_ylabel('One-day P&L, 10,000 shares (USD)')
ax.set_title('Gamma earns the square of the move, theta costs 91 USD a day', loc='left')
ax.legend(loc='lower center', fontsize=8)
