labels=['Parent','Marketable A','Passive B']
values=[20,12,8]
ax.bar(labels,values,color=[ACCENT,GOOD,WARM])
for i,v in enumerate(values): ax.text(i,v+0.7,f'{v} orders/min',ha='center',fontsize=8)
ax.set_ylabel('arrival rate (orders/minute)')
ax.set_ylim(0,24)
ax.set_title('Thinning reallocates rate; it does not create arrivals',fontsize=9,loc='left')
