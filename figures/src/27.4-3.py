rng=np.random.default_rng(29)
n=600
se=rng.uniform(0.012,0.032,n)
C=np.eye(n)
for i,j,r in [(0,1,.82),(2,3,.74),(4,5,.68)]: C[i,j]=C[j,i]=r
for a in range(10,15):
    for b in range(10,15):
        if a!=b: C[a,b]=.58
full=np.outer(se,se)*C
def risk(w): return np.sqrt(w@full@w), np.sqrt((w**2*se**2).sum())
cases=[]
w=np.zeros(n);w[0]=w[1]=1e6; cases.append(('long both halves\nof one company',)+risk(w))
w=np.zeros(n);w[0],w[1]=1e6,-1e6; cases.append(('long one, short\nthe other',)+risk(w))
w=np.zeros(n);w[10:15]=1e6;       cases.append(('long a five-stock\nhidden theme',)+risk(w))
x=np.arange(3)
mod=[c[2]/1000 for c in cases]; tru=[c[1]/1000 for c in cases]
ax.bar(x-0.19,mod,width=.36,color=GRID,edgecolor=MUTED,label='what the diagonal model says')
ax.bar(x+0.19,tru,width=.36,color=ACCENT,label='the truth')
for i,(m_,t_) in enumerate(zip(mod,tru)):
    ax.annotate(f'{m_:.1f}k',xy=(i-0.19,m_),xytext=(0,4),textcoords='offset points',fontsize=8,ha='center',color=MUTED)
    ax.annotate(f'{t_:.1f}k',xy=(i+0.19,t_),xytext=(0,4),textcoords='offset points',fontsize=8,ha='center',color=ACCENT)
    pct=(t_/m_-1)*100
    ax.annotate(f'{pct:+.0f}%',xy=(i,max(m_,t_)),xytext=(0,20),textcoords='offset points',
                fontsize=9.5,ha='center',color=BAD if pct<0 else GOOD,weight='bold')
ax.annotate('same number for both:\nthe model cannot see the sign',xy=(0.5,25.7),xytext=(0.62,72),
            fontsize=8,color=MUTED,arrowprops=dict(arrowstyle='->',color=MUTED,lw=.9))
ax.set_xticks(x);ax.set_xticklabels([c[0] for c in cases],fontsize=8)
ax.set_ylabel('daily risk (USD thousand)')
ax.set_ylim(0,132)
ax.set_title('One assumption, three portfolios, errors in both directions',loc='left')
ax.legend(fontsize=7,loc='upper left')
