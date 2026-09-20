
rho=np.linspace(-.8,1,300);var=.25*.2**2+.25*.3**2+2*.5*.5*.2*.3*rho
ax.plot(rho,var,color=ACCENT);ax.scatter([.2,.4],[.0385,.0445],color=[GOOD,BAD],s=70)
ax.set_xlabel('Correlation');ax.set_ylabel('Index variance (per year)');ax.axhline(0,color=INK,lw=1)
