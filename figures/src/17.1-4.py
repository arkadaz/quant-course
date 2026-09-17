k=np.arange(3);prob=stats.binom.pmf(k,2,.04)
ax.bar(k*100,prob,color=[ACCENT,WARM,BAD],width=35)
for x,y in zip(k*100,prob):ax.text(x,y+.015,f'{100*y:.2f}%',ha='center')
ax.set_ylim(0,1.05);ax.set_xticks(k*100);ax.set_xlabel('Combined loss (USD thousand)');ax.set_ylabel('Probability')
