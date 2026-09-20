m,mult=40,2.5
rng=np.random.default_rng(23)
T,on,off=400,100,220
true=np.ones(T);true[on:off]=mult
f=rng.standard_normal((m,T))*true
lam=0.5**(1/63);ew=np.zeros(T);ew[0]=1.
for t in range(1,T): ew[t]=(1-lam)*np.mean(f[:,t-1]**2)+lam*ew[t-1]
lam0=0.5**(1/15);u=np.linalg.norm(f,axis=0)/np.sqrt(m);st=np.zeros(T);st[0]=1.
for t in range(1,T): st[t]=(1-lam0)*u[t]+lam0*st[t-1]
d=np.arange(T)
ax.fill_between(d,st,np.sqrt(ew),where=(d>=off),color=GOOD,alpha=.15)
ax.step(d,true,where='post',color=INK,lw=2.2,label='the truth')
ax.plot(d,np.sqrt(ew),color=WARM,lw=2.2,label='63-day half-life')
ax.plot(d,st,color=ACCENT,lw=2.2,label='cross-sectional, 15-day half-life')
ax.axvline(off,color=MUTED,ls=':',lw=1.4)
ax.annotate('storm ends',xy=(off,0.8),xytext=(5,0),textcoords='offset points',fontsize=7.5,color=MUTED)
ax.annotate('still says 1.60x four months later',xy=(off+80,np.sqrt(ew[off+80])),
            xytext=(off+92,2.05),fontsize=8,color=WARM,arrowprops=dict(arrowstyle='->',color=WARM,lw=.9))
ax.annotate('the book runs 38% too small\nthrough all of this',xy=(off+55,1.55),xytext=(240,0.98),
            fontsize=8,color=GOOD,arrowprops=dict(arrowstyle='->',color=GOOD,lw=.9))
ax.set_xlabel('trading day');ax.set_ylabel('volatility, as a multiple of normal')
ax.set_ylim(0.7,2.9)
ax.set_title('Being slow on the way down costs money nobody ever sees',loc='left')
ax.legend(fontsize=7,loc='upper left')
