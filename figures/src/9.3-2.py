rng=np.random.default_rng(632);m=500;n=180;h=.25;dt=h/n;start=.8;t=np.linspace(0,h,n+1);p=np.c_[np.full(m,start),start+np.cumsum(rng.normal(0,np.sqrt(dt),(m,n)),axis=1)]
for i in range(25):ax.plot(t,p[i],color=ACCENT,alpha=.09,lw=.8)
ax.plot(t,p.mean(axis=0),color=GOOD,lw=2.5,label='ensemble mean')
ax.axhline(start,color=INK,ls='--',lw=1.1,label='current value')
ax.set_xlabel('Future horizon');ax.set_ylabel('Process value');ax.set_title('Uncertainty grows while the conditional mean stays put',loc='left');ax.legend(loc='upper left')
