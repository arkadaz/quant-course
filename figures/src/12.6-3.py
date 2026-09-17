labels=['Spot today','Q mean at 1Y','Discounted Q mean'];vals=[200,200*np.exp(.04),200];ax.bar(labels,vals,color=[ACCENT,WARM,GOOD],width=.55);ax.set_ylabel('USD/share');ax.set_ylim(0,235);ax.set_title('Risk-neutral growth cancels discounting',loc='left');
for i,v in enumerate(vals):ax.text(i,v+3,f'USD {v:.2f}',ha='center',fontsize=8,weight='bold')
