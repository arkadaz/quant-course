vals=[2/(1+11/3),4/(1+25/3)];ax.bar(['Desk 1','Desk 2'],vals,color=[ACCENT,GOOD],width=.55);ax.axhline(3/7,color=WARM,ls='--',label='shadow price')
ax.set_ylim(0,.55);ax.set_ylabel('Marginal profit per USD million');ax.legend();ax.set_title('Optimal allocation equalises marginal value',loc='left')
