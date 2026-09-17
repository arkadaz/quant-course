labels=['Direct E[Y]','E[E[Y|X]]']
values=[-40,-40]
ax.bar(labels,values,color=[ACCENT,GOOD],width=0.55)
ax.axhline(0,color=MUTED,lw=0.8)
for i,v in enumerate(values): ax.text(i,v-12,f'{v:.0f} USD/day',ha='center',va='top',color=INK,weight='bold')
ax.set_ylabel('expected daily P&L (USD/day)')
ax.set_ylim(-80,20)
ax.set_title('Two computation paths must agree',fontsize=9,loc='left')
