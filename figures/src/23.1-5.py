def opt(u,d,X0=10.0,I=9.0,R=1.05):
    q=(R-d)/(u-d)
    V2=[max(X0*u**k*d**(2-k)-I,0) for k in (2,1,0)]
    V1u=max(X0*u-I,(q*V2[0]+(1-q)*V2[1])/R);V1d=max(X0*d-I,(q*V2[1]+(1-q)*V2[2])/R)
    return (q*V1u+(1-q)*V1d)/R
sp=np.linspace(0.12,1.2,109);vals=[opt(1.1+s/2,1.1-s/2) for s in sp]
ax.plot(sp,vals,color=ACCENT,lw=2.2,label='value of the right to wait')
ax.axhline(1.0,color=MUTED,lw=1,ls=(0,(4,3)),label='invest today: 1.0')
ax.axvline(0.3026,color=BAD,lw=.9,ls=':')
ax.text(0.315,3.55,'below 0.30 the worst node\nstays above I = 9.0',fontsize=7.3,color=BAD,va='top')
ax.scatter([0.6],[2.6392],color=INK,zorder=3,s=30)
ax.annotate('u 1.4, d 0.8: 2.6392',xy=(0.6,2.6392),xytext=(8,-14),textcoords='offset points',fontsize=7.5)
ax.annotate('flat 1.8367 = 10 - 9/1.05^2',xy=(0.13,1.8367),xytext=(-8,10),textcoords='offset points',fontsize=7.5,ha='left')
ax.set_xlabel('Gap between multipliers u - d (centre kept at 1.1)');ax.set_ylabel('Value today (USD M)')
ax.set_ylim(0.6,4.0);ax.set_title('Uncertainty adds value only once a branch can lose',loc='left');ax.legend(fontsize=7.5,loc='lower right');ax.grid(alpha=.2)
