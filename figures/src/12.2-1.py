labels=['ordinary chain rule','Itô chain rule'];vals=[.12,.0808];ax.bar(labels,np.array(vals)*100,color=[BAD,GOOD],width=.55);ax.set_ylim(0,14.5);ax.set_ylabel('Log drift (%/year)');ax.set_title('Curvature lowers the median-growth exponent',loc='left');
for i,v in enumerate(vals):ax.text(i,v*100+.4,f'{v*100:.2f}%',ha='center',weight='bold')
