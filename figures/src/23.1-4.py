from matplotlib.ticker import NullFormatter
S0,u,d,r=400,1.2,0.9,0.10;q=(1+r-d)/(u-d)
S=lambda t,k:S0*u**k*d**(t-k)
Up=np.zeros((11,11))
for t in range(9,-1,-1):
    for k in range(t+1):
        Up[t,k]=(max(S(t,k)-240,0)*12500+q*Up[t+1,k+1]+(1-q)*Up[t+1,k])/(1+r)
U=np.zeros((11,11));ex=[];wt=[]
for t in range(9,-1,-1):
    for k in range(t+1):
        A=(max(S(t,k)-200,0)*1e4+q*U[t+1,k+1]+(1-q)*U[t+1,k])/(1+r);E=Up[t,k]-4e6
        U[t,k]=max(A,E);(ex if E>A else wt).append((t,S(t,k)))
ax.scatter([p[0] for p in wt],[p[1] for p in wt],s=22,color=MUTED,label='keep old equipment',zorder=3)
ax.scatter([p[0] for p in ex],[p[1] for p in ex],s=44,color=GOOD,marker='s',label='upgrade now (10 nodes)',zorder=3)
ax.axhline(200,color=BAD,lw=1,ls=(0,(4,3)));ax.text(5.6,183,'old extraction cost 200',fontsize=7.5,color=BAD,va='top')
ax.axhline(2160,color=WARM,lw=1,ls=(0,(4,3)));ax.text(3.6,2250,'year 9 needs above 2,160',fontsize=7.5,color=WARM)
ax.set_yscale('log');ax.set_yticks([150,200,300,400,600,1000,1500,2400])
ax.set_yticklabels(['150','200','300','400','600','1,000','1,500','2,400']);ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_ylim(120,3000);ax.set_xticks(range(10))
ax.set_xlabel('Year t');ax.set_ylabel('Gold price at the node (USD/oz)')
ax.set_title('Simplico: nodes where the 4M upgrade pays',loc='left');ax.legend(fontsize=7.5,loc='upper left');ax.grid(alpha=.2)
