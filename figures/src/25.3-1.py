rng=np.random.default_rng(3)
se,sn,P0=0.0256,0.012,50.0
n=120
m=P0+np.cumsum(se*rng.standard_normal(n))
side=rng.choice([-1,1],n)
p=m+sn*side
t=np.arange(n)
ax.fill_between(t,m-0.012,m+0.012,color=GRID,alpha=.9,label='bid to ask, 2.4 cents wide')
ax.plot(t,m,color=INK,lw=2.2,label='true value (never observed)')
ax.plot(t,p,'o',color=ACCENT,ms=3.2,label='price you record each minute')
ax.annotate('same value, two different prints',xy=(t[41],p[41]),xytext=(48,m[41]+0.10),fontsize=7.5,color=ACCENT,
            arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.8))
ax.set_xlabel('minute of the trading day');ax.set_ylabel('price (USD)')
ax.set_title('The bounce is not news, it is who crossed the spread',loc='left')
ax.legend(fontsize=7,loc='upper left')
