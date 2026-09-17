basis = np.linspace(-20, 20, 81)
resid = basis*50
ax.plot(basis, resid, color=ACCENT, lw=2.1)
ax.axhline(0, color=MUTED, lw=1)
ax.axvline(0, color=MUTED, lw=1)
ax.set_xlabel('Basis change (points)')
ax.set_ylabel('Residual P&L (USD per contract)')
ax.set_title('A matching notional cannot remove basis movement', loc='left')
