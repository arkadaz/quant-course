rng=np.random.default_rng(4)
n=14
style=rng.normal(0,1,(n,3)).round(2)
ctry=np.zeros((n,2));ctry[np.arange(n),rng.integers(0,2,n)]=1
ind=np.zeros((n,4));ind[np.arange(n),rng.integers(0,4,n)]=1
M=np.hstack([np.ones((n,1)),style,ctry,ind])
im=ax.imshow(M,cmap='RdBu_r',vmin=-2.2,vmax=2.2,aspect='auto')
ax.set_xticks(range(M.shape[1]))
ax.set_xticklabels(['market','value','mom','vol','US','JP','tech','banks','energy','health'],
                   rotation=45,ha='right',fontsize=7)
ax.set_yticks(range(n));ax.set_yticklabels([f'stock {i+1}' for i in range(n)],fontsize=6.5)
for x,lab,col in ((0,'intercept',INK),(2,'style: z-scored',INK),(4.5,'country: 0/1',INK),(7.5,'industry: 0/1',INK)):
    ax.annotate(lab,xy=(x,-1.1),fontsize=7.5,color=col,ha='center')
for x in (0.5,3.5,5.5):
    ax.axvline(x,color=INK,lw=1.6)
ax.set_title('Each row is a stock; the 1s in three blocks sum to trouble in 27.1',loc='left')
