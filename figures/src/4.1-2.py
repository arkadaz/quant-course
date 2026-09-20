names=['AAPL long','JPM long','NVDA short']
vals=np.array([12.5,7.5,-5.0])
colors=[GOOD,GOOD,BAD]
ax.bar(names, vals, color=colors, width=0.58)
ax.axhline(0,color=INK,lw=0.9)
for i,v in enumerate(vals): ax.text(i, v+(0.45 if v>=0 else -0.75), f'${v:.1f}M', ha='center', va='bottom' if v>=0 else 'top', fontsize=9, color=INK)
ax.set_ylim(-8,16)
ax.set_ylabel('Dollar exposure ($M)')
ax.set_title('Weights translated into a $25M portfolio', loc='left')
