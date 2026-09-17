rng=np.random.default_rng(1755);r=np.array([-.02,-.01,0,.01,.03]);b=rng.choice(r,size=(10000,5),replace=True).mean(axis=1)
ax.hist(b*100,bins=np.arange(-2.1,3.2,.2),color=ACCENT,alpha=.8);ax.axvline(.2,color=BAD);ax.set_xlabel('Bootstrap daily mean (%)');ax.set_ylabel('Resamples')
