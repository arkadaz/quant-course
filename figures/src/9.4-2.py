rng=np.random.default_rng(54);paths=[];steps=500
for j in range(80):
    r=1;g=1;z=[0.5]
    for n in range(steps):
        if rng.random()<r/(r+g):r+=1
        else:g+=1
        z.append(r/(r+g))
    paths.append(z)
paths=np.array(paths);t=np.arange(steps+1)
ax.plot(t,paths[:24].T,color=ACCENT,alpha=0.16,lw=0.8);ax.plot(t,paths.mean(axis=0),color=INK,lw=2.4,label='cross-path mean');ax.axhline(0.5,color=WARM,ls='--')
ax.set_xlabel('Draw count');ax.set_ylabel('Red share');ax.set_ylim(0,1);ax.legend(loc='upper right')
