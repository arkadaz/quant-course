rng=np.random.default_rng(31)
n=4000
truth=0.007558
rhos=np.linspace(0,0.95,40)
rep=[]
for r in rhos:
    m=rng.standard_normal(n)
    x=r*m+np.sqrt(max(1-r*r,1e-12))*rng.standard_normal(n)
    y=0.00333+truth*m+0.007496*x
    X1=np.column_stack([np.ones(n),m])
    rep.append(np.linalg.lstsq(X1,y,rcond=None)[0][1])
ax.plot(rhos,np.array(rep)*100,color=ACCENT,lw=2.4,label='what the old model reports for momentum')
ax.axhline(truth*100,color=BAD,ls='--',lw=1.8,label='the truth: 0.7558%')
ax.plot(0.4812,1.1013,'o',color=INK,ms=8)
ax.annotate('this topic: correlation 0.4812\nreported 1.1013%, 45.7% too high',
            xy=(0.4812,1.1013),xytext=(0.06,1.42),fontsize=8,color=INK,
            arrowprops=dict(arrowstyle='->',color=INK,lw=.9))
ax.set_xlabel('correlation between the new characteristic and momentum')
ax.set_ylabel('coefficient the old model reports (%)')
ax.set_title('A missing column makes the columns you kept look better than they are',loc='left')
ax.legend(fontsize=7,loc='upper left')
