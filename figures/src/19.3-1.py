rm = np.linspace(-0.04, 0.04, 81)
vp = 10_000_000
beta = 1.10
mu = 50
F = 5000
N = -44
unhedged = vp*beta*rm
futures = N*mu*F*rm
hedged = unhedged + futures
ax.plot(rm*100, unhedged/1000, color=BAD, label='Unhedged portfolio')
ax.plot(rm*100, hedged/1000, color=GOOD, label='Portfolio + short ES')
ax.axhline(0, color=MUTED, lw=1)
ax.set_xlabel('S&P 500 return (%)')
ax.set_ylabel('Approximate P&L (USD thousands)')
ax.set_title('Beta hedge flattens market P&L, not every risk', loc='left')
ax.legend(loc='best')
