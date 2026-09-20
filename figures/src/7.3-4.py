assets=['Thai stocks','Bonds','Gold']
money=np.array([50,30,20]);risk=np.array([85.84,1.46,12.70]);parity=np.array([21.15,58.69,20.16])
x=np.arange(3);wd=.26
b1=ax.bar(x-wd,money,wd,color=ACCENT,label='share of money (50/30/20)')
b2=ax.bar(x,risk,wd,color=BAD,label='share of risk it carries')
b3=ax.bar(x+wd,parity,wd,color=GOOD,label='risk-parity money (equal risk)')
for bars in (b1,b2,b3):
 for r in bars:
  ax.annotate(f'{r.get_height():.1f}',(r.get_x()+r.get_width()/2,r.get_height()),textcoords='offset points',xytext=(0,2),ha='center',fontsize=7)
ax.set_xticks(x);ax.set_xticklabels(assets);ax.set_ylim(0,100);ax.set_ylabel('% of portfolio')
ax.set_title('Half the money carries 85.8% of the risk',loc='left');ax.legend(fontsize=7,loc='upper right')
