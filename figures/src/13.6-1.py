w=np.linspace(-3,3,400);lam=.1/.28;z=np.exp(-lam*w-.5*lam**2);ax.plot(w,z,color=ACCENT,lw=2);ax.axhline(1,color=MUTED,ls='--')
for x in (-1,0,1):
    y=np.exp(-lam*x-.5*lam**2);ax.scatter([x],[y],color=WARM,s=30,zorder=3);ax.text(x+.08,y+.12,f'{y:.4f}',fontsize=8)
ax.set_xlabel('Physical Brownian terminal value $W_1$');ax.set_ylabel('Path weight $dQ/dP$');ax.set_title('Measure change reweights; it does not redraw',loc='left')
