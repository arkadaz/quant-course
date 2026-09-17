divs = np.linspace(0, 4, 41)
strike = 100
boundary = strike + 0.55*divs + 0.15*divs**2
ax.plot(divs, boundary, color=ACCENT, lw=2.2)
ax.fill_between(divs, boundary, 110, color=GOOD, alpha=0.12, label='Illustrative exercise region')
ax.set_xlabel('Cash dividend before ex-date (USD)')
ax.set_ylabel('Stock price S_t (USD)')
ax.set_ylim(100, 110)
ax.set_title('Larger dividends can make early exercise more attractive', loc='left')
ax.legend(loc='best')
