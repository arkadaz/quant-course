m,T,jump,mult=40,320,120,2.5
rng=np.random.default_rng(19)
true=np.ones(T);true[jump:]=mult
f=rng.standard_normal((m,T))*true
lam=0.5**(1/63);ew=np.zeros(T);ew[0]=1.
for t in range(1,T): ew[t]=(1-lam)*np.mean(f[:,t-1]**2)+lam*ew[t-1]
lam0=0.5**(1/15);u=np.linalg.norm(f,axis=0)/np.sqrt(m);st=np.zeros(T);st[0]=1.
for t in range(1,T): st[t]=(1-lam0)*u[t]+lam0*st[t-1]
d=np.arange(T)
ax.fill_between(d,np.sqrt(ew),true,where=(d>=jump),color=BAD,alpha=.12)
ax.step(d,true,where='post',color=INK,lw=2.2,label='the truth')
ax.plot(d,np.sqrt(ew),color=WARM,lw=2.2,label='exponential weighting, 63-day half-life')
ax.plot(d,st,color=ACCENT,lw=2.2,label='cross-sectional update, 15-day half-life')
ax.axvline(jump,color=MUTED,ls=':',lw=1.4)
ax.annotate('regime change',xy=(jump,0.75),xytext=(5,0),textcoords='offset points',fontsize=7.5,color=MUTED)
ax.plot(jump+44,1.75,'v',color=WARM,ms=9);ax.plot(jump+14,1.75,'v',color=ACCENT,ms=9)
ax.annotate('halfway: 14 days',xy=(jump+14,1.75),xytext=(-8,10),textcoords='offset points',
            fontsize=7.5,color=ACCENT,ha='right')
ax.annotate('halfway: 44 days',xy=(jump+44,1.75),xytext=(10,-14),textcoords='offset points',
            fontsize=7.5,color=WARM)
ax.annotate('every day in here the book\nis bigger than it should be',xy=(200,1.85),
            xytext=(196,1.02),fontsize=8,color=BAD,arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.set_xlabel('trading day');ax.set_ylabel('volatility, as a multiple of normal')
ax.set_ylim(0.7,2.8)
ax.set_title('One layer forgets smoothly; the market does not change smoothly',loc='left')
ax.legend(fontsize=7,loc='lower right')
