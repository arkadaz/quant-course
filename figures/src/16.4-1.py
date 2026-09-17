rng=np.random.default_rng(164);n=260;om=1.8e-6;al=.09;be=.89;v=np.zeros(n);eps=np.zeros(n);v[0]=om/(1-al-be)
for i in range(1,n):
 eps[i-1]=np.sqrt(v[i-1])*rng.normal();v[i]=om+al*eps[i-1]**2+be*v[i-1]
eps[-1]=np.sqrt(v[-1])*rng.normal();ret=eps*100;vol=np.sqrt(v)*100;fig=plt.gcf();fig.subplots_adjust(hspace=.45);ax.remove();axs=fig.subplots(2,1,sharex=True);axs[0].plot(ret,color=ACCENT,lw=.7);axs[0].axhline(0,color=INK,lw=.5);axs[0].set_ylabel('return (%)');axs[0].set_title('GARCH-like returns: large moves cluster',loc='left');axs[1].plot(vol,color=WARM,lw=1.5);axs[1].set_ylabel('conditional sigma (%)');axs[1].set_xlabel('trading day');axs[1].set_title('The forecast volatility moves with information',loc='left')
