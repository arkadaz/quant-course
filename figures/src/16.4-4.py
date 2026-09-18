h=np.arange(0,61);V=9e-5;v0=.0002348;v=V+.98**h*(v0-V)
ax.plot(h,np.sqrt(v)*100,color=ACCENT,lw=2,label='forecast sigma = sqrt of forecast variance')
ax.axhline(np.sqrt(V)*100,color=GOOD,ls='--',label='long-run 0.9487%')
ax.axvline(34.31,color=BAD,ls=':',label='variance half-life 34.3 days')
for d,dy in ((0,-12),(20,6),(60,6)):
 ax.annotate(f'{np.sqrt(v[d])*100:.3f}%',(d,np.sqrt(v[d])*100),textcoords='offset points',xytext=(6,dy),fontsize=7)
ax.set_xlabel('horizon (trading days)');ax.set_ylabel('daily volatility (%)')
ax.set_title('Sixty days after the shock, sigma is still 21% above normal',loc='left');ax.legend(fontsize=7)
