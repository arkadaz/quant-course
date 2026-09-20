rng=np.random.default_rng(29)
n,T=600,251
se=rng.uniform(0.012,0.032,n)
C=np.eye(n)
for i,j,r in [(0,1,.82),(2,3,.74),(4,5,.68)]: C[i,j]=C[j,i]=r
for a in range(10,15):
    for b in range(10,15):
        if a!=b: C[a,b]=.58
E=(np.linalg.cholesky(C+1e-10*np.eye(n))@rng.standard_normal((n,T)))*se[:,None]
emp=np.corrcoef(E)
k=20
M=np.where(np.abs(emp[:k,:k])>0.40,emp[:k,:k],0.0)
np.fill_diagonal(M,0.0)
ax.imshow(M,cmap='Reds',vmin=0,vmax=0.9,aspect='equal')
for i in range(k):
    for j in range(k):
        if M[i,j]>0: ax.text(j,i,f'{M[i,j]:.2f}',ha='center',va='center',fontsize=6,color='white')
ax.set_xticks(range(k));ax.set_xticklabels(range(1,k+1),fontsize=6)
ax.set_yticks(range(k));ax.set_yticklabels(range(1,k+1),fontsize=6)
for a,b,lab in ((0,2,'share classes'),(10,15,'a theme')):
    ax.add_patch(plt.Rectangle((a-0.5,a-0.5),b-a if b>5 else 2,b-a if b>5 else 2,
                               fill=False,edgecolor=ACCENT,lw=2.0))
ax.annotate('three pairs of share classes',xy=(1,-1.2),fontsize=8,color=ACCENT)
ax.annotate('five stocks that move together\nbut are too few to be a factor',
            xy=(12,16.8),fontsize=8,color=ACCENT,ha='center')
ax.set_title('After thresholding at 0.40: everything else is exactly zero',loc='left')
