labels=['SPY','AGG','QQQ'];slack=np.array([.125,.875,0]);mult=np.array([0,0,.0095]);x=np.arange(3)
ax.bar(x-.18,slack,.36,color=ACCENT,label='weight / slack');ax.bar(x+.18,mult,.36,color=BAD,label='multiplier');ax.set_xticks(x,labels);ax.legend();ax.set_title('Only a binding lower bound carries a price',loc='left')
