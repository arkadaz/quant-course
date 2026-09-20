
flows=np.array([300.,-235.,-4962.640274,4900.993367]);labels=['Short call','Long put','Long prepaid','Short bond']
ax.bar(labels,flows,color=[GOOD,BAD,BAD,GOOD]);ax.axhline(0,color=INK,lw=1);ax.scatter([3.7],[flows.sum()],color=ACCENT,s=70,label=f'Net {flows.sum():.4f}')
ax.set_ylabel('Initial cash flow (SPX points)');ax.set_xlim(-.6,4.2);ax.tick_params(axis='x',rotation=12);ax.legend()
