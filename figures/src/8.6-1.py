labels=['SPY','AGG','QQQ'];u=np.array([.307692,.854701,-.162393]);k=np.array([.125,.875,0]);x=np.arange(3);bw=.36
ax.bar(x-bw/2,u*100,bw,color=WARM,label='equality only');ax.bar(x+bw/2,k*100,bw,color=GOOD,label='long-only KKT');ax.axhline(0,color=INK,lw=1);ax.set_xticks(x,labels);ax.set_ylabel('Weight (%)');ax.legend();ax.set_title('The mandate changes the active set',loc='left')
