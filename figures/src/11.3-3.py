labels=['Beta floor','QQQ cap','SPY cap'];binding=np.array([1,0,1]);priced=np.array([1,0,1]);i=np.arange(3)
ax.bar(i-.18,binding,.36,color=ACCENT,label='Binding constraint')
ax.bar(i+.18,priced,.36,color=GOOD,label='Positive shadow price')
notes=['slack 0 | price 150','slack 2 | price 0','slack 0 | price 60']
for j,note in enumerate(notes):ax.text(j,1.08,note,ha='center',fontsize=7.5)
ax.set_xticks(i,labels);ax.set_yticks([0,1],['No','Yes']);ax.set_ylim(0,1.28);ax.set_ylabel('Condition met');ax.legend(loc='lower center',fontsize=7)
ax.set_title('Complementary slackness pairs activity with price',loc='left')
