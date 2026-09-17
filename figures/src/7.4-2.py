x=np.linspace(-11,8,360);marg_mean=0.03;marg_sd=3.0
beta=0.60;xobs=-3.0;muX=0.04;cond_mean=marg_mean+beta*(xobs-muX);cond_sd=np.sqrt(7.56)
marg=stats.norm.pdf(x,loc=marg_mean,scale=marg_sd);cond=stats.norm.pdf(x,loc=cond_mean,scale=cond_sd)
ax.plot(x,marg,color=MUTED,lw=2,label='QQQ marginal: mean 0.03%, SD 3.00%')
ax.plot(x,cond,color=GOOD,lw=2,label=f'conditional: mean {cond_mean:.3f}%, SD {cond_sd:.2f}%')
ax.axvline(cond_mean,color=GOOD,ls='--',lw=.9)
ax.set_xlabel('QQQ return (%)');ax.set_ylabel('density');ax.legend(loc='upper left',fontsize=7)
ax.set_title('Conditioning shifts the mean and removes explained variance',fontsize=9,loc='left')
