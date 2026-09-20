rng=np.random.default_rng(41)
n,m,T=800,10,251
fvol=np.array([1.10,.55,.45,.40,.35,.32,.28,.25,.22,.20])/100
Cf=np.eye(m)*0.7+0.3*np.ones((m,m));Of=np.outer(fvol,fvol)*Cf
B=rng.normal(0,1,(n,m));B[:,0]=1.0
se=rng.uniform(0.012,0.030,n);Oei=np.diag(1/se**2)
G=np.linalg.inv(B.T@Oei@B)
infl=1+np.diag(G)/np.diag(Of)
L=np.linalg.cholesky(Of);acc=np.zeros(m)
for _ in range(200):
    f=L@rng.standard_normal((m,T))
    r=B@f+rng.normal(0,1,(n,T))*se[:,None]
    fh=np.linalg.solve(B.T@Oei@B,B.T@Oei@r)
    acc+=np.diag(fh@fh.T/T)/np.diag(Of)
acc/=200
x=np.arange(1,m+1)
band=np.sqrt(2/T)
ax.fill_between(x,1-band,1+band,color=GRID,alpha=.9,label='what one year alone would scatter over')
ax.plot(x,infl,color=BAD,lw=2.4,marker='o',ms=6,label='predicted by the formula')
ax.plot(x,acc,'s',color=ACCENT,ms=7,label='measured, average of 200 years')
ax.axhline(1,color=INK,lw=1.2)
ax.annotate(f'{(infl[-1]-1)*100:.1f}% too high',xy=(m,infl[-1]),xytext=(-96,6),
            textcoords='offset points',fontsize=8,color=BAD)
ax.annotate(f'{(infl[0]-1)*100:.2f}%',xy=(1,infl[0]),xytext=(6,10),textcoords='offset points',
            fontsize=8,color=BAD)
ax.set_xticks(x)
ax.set_xlabel('factor, largest to smallest');ax.set_ylabel('measured variance / true variance')
ax.set_title('The bias is invisible in one year and large for small factors',loc='left')
ax.legend(fontsize=7,loc='upper left')
