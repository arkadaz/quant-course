rng=np.random.default_rng(24)
fig=plt.gcf();ax.remove();a1,a2=fig.subplots(1,2,gridspec_kw={'width_ratios':[1.6,1]});fig.subplots_adjust(wspace=.35)
t=np.cumsum(rng.exponential(1/20,80));t=t[t<1.0];isA=rng.random(len(t))<0.6
a1.vlines(t,1.7,2.3,color=ACCENT,lw=1.4);a1.vlines(t[isA],0.7,1.3,color=GOOD,lw=1.4);a1.vlines(t[~isA],-0.3,0.3,color=WARM,lw=1.4)
a1.set_yticks([0,1,2]);a1.set_yticklabels([f'B passive: {(~isA).sum()}',f'A marketable: {isA.sum()}',f'all orders: {len(t)}'],fontsize=7)
a1.set_xlim(0,1);a1.set_ylim(-0.6,2.6);a1.set_xlabel('time (minutes)');a1.set_title('One minute, each order marked A with p = 0.60',loc='left',fontsize=8)
n=rng.poisson(20,3000);nA=rng.binomial(n,0.6);nB=n-nA
a2.scatter(nA+rng.uniform(-.25,.25,len(nA)),nB+rng.uniform(-.25,.25,len(nB)),s=3,alpha=.25,color=MUTED)
a2.axvline(nA.mean(),color=GOOD,lw=1.2);a2.axhline(nB.mean(),color=WARM,lw=1.2)
a2.set_xlabel('A orders per minute');a2.set_ylabel('B orders per minute')
a2.set_title(f'3,000 minutes: means {nA.mean():.1f} and {nB.mean():.1f}, corr {np.corrcoef(nA,nB)[0,1]:+.2f}',loc='left',fontsize=8)
