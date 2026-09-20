rng=np.random.default_rng(2)
base=rng.standard_normal(250)*0.012
ks=np.arange(0,9)
zs,ds=[],[]
for k in ks:
    x=np.concatenate([base[:250-k],np.full(k+1,0.50)])
    zs.append(0.50/x.std())
    ds.append(0.50/np.median(np.abs(x)))
ax.plot(ks,zs,'o-',color=BAD,lw=2.4,ms=5,label='divide by the standard deviation')
ax.plot(ks,ds,'o-',color=GOOD,lw=2.4,ms=5,label='divide by the median absolute value')
ax.axhline(10,color=INK,ls='--',lw=1.2)
ax.annotate('a threshold of 10',xy=(6.2,10),xytext=(0,5),textcoords='offset points',
            fontsize=7.5,color=INK)
ax.annotate(f'{zs[0]:.1f}',xy=(0,zs[0]),xytext=(6,4),textcoords='offset points',fontsize=8,color=BAD)
ax.annotate(f'{ds[0]:.1f}',xy=(0,ds[0]),xytext=(6,-2),textcoords='offset points',fontsize=8,color=GOOD)
ax.annotate('by here the outliers have\nhidden themselves completely',xy=(5,zs[5]),xytext=(2.4,22),
            fontsize=8,color=BAD,arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.annotate('the median does not move',xy=(7,ds[7]),xytext=(3.2,50),fontsize=8,color=GOOD,
            arrowprops=dict(arrowstyle='->',color=GOOD,lw=.9))
ax.set_xlabel('number of outliers already sitting in the 251-day window')
ax.set_ylabel('score given to an outlier of 50 percent')
ax.set_title('An outlier inflates its own denominator, then slips through',loc='left')
ax.legend(frameon=False,fontsize=8,loc='center right')
