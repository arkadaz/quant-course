
K=np.array([4900,5000,5100]);C=np.array([112,80,47]);ax.plot(K,C,'o-',color=BAD,label='Quoted calls')
mid=.5*(C[0]+C[2]);ax.scatter([5000],[mid],color=GOOD,s=70,label=f'Convex upper limit {mid:.1f}')
ax.vlines(5000,C[1],mid,color=MUTED,ls='--');ax.set_xlabel('Strike (SPX points)');ax.set_ylabel('Call price (points)');ax.legend()
