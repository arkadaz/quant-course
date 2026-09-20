to=np.linspace(0,.30,200);W=50e6;cost=W*(2*to)*.001
ax.plot(to*100,cost/1000,color=ACCENT,lw=2);ax.scatter([10,20],[10,20],color=GOOD,s=45);ax.set_xlabel('One-way turnover (%)');ax.set_ylabel('Linear cost (USD thousand)');ax.set_title('Counting both legs links turnover to cash cost',loc='left')
