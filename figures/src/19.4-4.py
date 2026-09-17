q = np.linspace(0, 0.05, 51)
S0 = 100
K = 100
r = 0.05
T = 0.5
parity = S0*np.exp(-q*T) - K*np.exp(-r*T)
ax.plot(q*100, parity, color=ACCENT, lw=2.2)
ax.set_xlabel('Dividend yield q (%)')
ax.set_ylabel('C - P parity value (USD)')
ax.set_title('Dividend yield shifts the parity anchor', loc='left')
