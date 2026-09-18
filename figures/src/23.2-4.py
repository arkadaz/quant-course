rng=np.random.default_rng(13);n=48
eps=rng.standard_normal(n);N=rng.poisson(0.03,n)
kappa,theta,sig,J=0.25,np.log(70),0.03,np.log(3.0)
a=np.empty(n+1);b=np.empty(n+1);a[0]=b[0]=theta
for t in range(n):
    a[t+1]=a[t]+kappa*(theta-a[t])+sig*eps[t]
    b[t+1]=b[t]+kappa*(theta-b[t])+sig*eps[t]+J*N[t]
h=np.arange(n+1)
ax.plot(h,np.exp(a),color=ACCENT,lw=2,label='same shocks, no jump term')
ax.plot(h,np.exp(b),color=BAD,lw=2,label='with jump term (price x3 once)')
ax.axhline(70,color=MUTED,lw=1,ls=(0,(4,3)))
k=int(np.nonzero(N)[0][0])+1
ax.annotate(f'hour {k}: {np.exp(b[k]):.0f}',xy=(k,np.exp(b[k])),xytext=(k+3,np.exp(b[k])-10),fontsize=7.5)
ax.set_xlabel('Hour');ax.set_ylabel('Power price (USD/MWh)')
ax.set_title('One simulated jump dominates two days of hourly prices',loc='left');ax.legend(fontsize=7.5,loc='upper left');ax.grid(alpha=.2)
