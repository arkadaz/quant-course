g=(1.1008-1.0900)/1.0900
local=.030-.024
cf=g+.024-.048
tot=local+cf
labels=['local excess\nstock minus EUR rate','currency, rate-adjusted\nFX plus EUR rate minus USD rate','total to a USD investor']
vals=[local*100,cf*100,tot*100]
bars=ax.bar(range(3),vals,color=[GOOD,BAD,ACCENT],width=.55)
ax.axhline(0,color=INK,lw=1)
ax.axhline(3.0,color=MUTED,ls=':',lw=1.2)
ax.annotate('the headline everyone quotes: stock +3.00 pt',xy=(1,3.0),xytext=(0,6),
            textcoords='offset points',fontsize=7,color=MUTED,ha='center')
for b,v in zip(bars,vals):
    ax.annotate(f'{v:+.2f} pt',xy=(b.get_x()+b.get_width()/2,v),
                xytext=(0,7 if v>0 else -13),textcoords='offset points',fontsize=8.5,ha='center')
ax.set_xticks(range(3));ax.set_xticklabels(labels,fontsize=7)
ax.set_ylabel('return (points)');ax.set_ylim(-2.3,3.9)
ax.set_title('A stock up 3% and a euro up 1% can still lose a dollar investor money',loc='left')
