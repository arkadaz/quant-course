labels=['buy basket','sell 50,000 ETF','gross','creation fee','ETF half-spread','basket spread','impact','settlement','net']
vals=[-5_000_000,5_060_000,60_000,-500,-1_000,-7_500,-7_500,-1_000,42_500]
show=np.array([v/1000 for v in vals])
steps=show[2:]
x=np.arange(len(steps))
run=0;bottoms=[];heights=[]
for i,v in enumerate(steps):
    if i==0 or i==len(steps)-1: bottoms.append(0);heights.append(v);run=v if i==0 else run
    else: bottoms.append(run+v if v<0 else run);heights.append(abs(v));run+=v
cols=[ACCENT]+[BAD]*5+[GOOD]
ax.bar(x,heights,bottom=bottoms,color=cols,width=.6)
for xi,v,b,h in zip(x,steps,bottoms,heights): ax.text(xi,b+h+1,f'{v:+,.1f}k' if 0<xi<len(steps)-1 else f'{v:,.1f}k',ha='center',fontsize=7.5)
ax.set_xticks(x);ax.set_xticklabels(labels[2:],rotation=20,fontsize=7.5)
ax.set_ylabel('USD thousand per creation unit');ax.set_ylim(0,78)
ax.text(.30,.93,'buy basket 5,000.0k, sell ETF 5,060.0k',transform=ax.transAxes,fontsize=7.5,color=INK)
ax.set_title('Creation route: 60,000 gross becomes 42,500 net',loc='left');ax.grid(axis='y',alpha=.2)
