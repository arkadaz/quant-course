x=np.linspace(0,10,200)
y=(10-x)/2
ax.plot(x,y,color=BAD,lw=2,label='x1 + 2x2 = 10')
ax.fill_between(x,0,y,color=GOOD,alpha=0.18,label='feasible with x1, x2 ≥ 0')
ax.set_xlim(-0.5,10.8);ax.set_ylim(-0.3,5.8)
ax.set_xlabel('first hedge x1 (USD million)');ax.set_ylabel('second hedge x2 (USD million)')
ax.legend(loc='upper right');ax.set_title('Nonnegativity closes the feasible region',fontsize=9,loc='left')
