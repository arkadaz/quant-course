B=np.array([[1,1.2,1],[1,-0.4,1],[1,0.6,0],[1,-1.4,0]],float)
f=np.array([0.80,-0.50,0.30])
names=['A','B','C','D']
x=np.arange(4)
parts=[B[:,j]*f[j] for j in range(3)]
labs=['market x (+0.80%)','momentum x (-0.50%)','tech x (+0.30%)']
cols=[ACCENT,WARM,GOOD]
for j,(p,l,c) in enumerate(zip(parts,labs,cols)):
    ax.bar(x+(j-1.5)*0.19,p,width=0.18,color=c,label=l)
tot=sum(parts)
ax.bar(x+1.5*0.19,tot,width=0.18,color=INK,label='sum: what the factors explain')
for i,v in enumerate(tot):
    ax.annotate(f'{v:+.2f}%',xy=(x[i]+1.5*0.19,v),xytext=(0,5 if v>0 else -12),
                textcoords='offset points',fontsize=7.5,ha='center',color=INK)
ax.axhline(0,color=INK,lw=.9)
ax.set_xticks(x);ax.set_xticklabels([f'stock {n}' for n in names])
ax.set_ylabel('contribution to the day (%)')
ax.set_title('Four stocks, one day, three columns added up',loc='left')
ax.legend(fontsize=7,loc='lower left')
