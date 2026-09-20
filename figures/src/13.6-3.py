labels=['Spot today','Q mean at 1Y','Discounted Q mean','P mean at 1Y'];vals=[100,100*np.exp(.02),100,100*np.exp(.12)];ax.bar(labels,vals,color=[ACCENT,WARM,GOOD,MUTED],width=.55);ax.set_ylabel('USD/share');ax.set_ylim(0,128);ax.set_title('Risk-neutral growth cancels discounting',loc='left');
for i,v in enumerate(vals):ax.text(i,v+2,f'USD {v:.2f}',ha='center',fontsize=8,weight='bold')
