names=['start','grid','Nelder-Mead','BFGS']
k=np.array([2.30,1.80,1.9524,3.6941]);th=np.array([0.046,0.046,0.0469,0.0478]);sv=np.array([0.0825,0.0925,0.1159,0.6059])
lhs=2*k*th;rhs=sv**2;x=np.arange(4)
ax.bar(x-.18,lhs,.34,color=GOOD,label='2 kappa theta')
ax.bar(x+.18,rhs,.34,color=BAD,label='sigma_v squared')
for xi,a,b in zip(x,lhs,rhs):
    ax.text(xi-.18,a+.006,f'{a:.4f}',ha='center',fontsize=7);ax.text(xi+.18,b+.006,f'{b:.4f}',ha='center',fontsize=7)
ax.set_xticks(x);ax.set_xticklabels(names);ax.set_ylim(0,.42)
ax.set_ylabel('Feller terms');ax.text(1.55,.30,'BFGS fails: 0.3532 < 0.3671',fontsize=7.5,color=BAD)
ax.set_title('Feller check on the four parameter sets',loc='left');ax.legend(fontsize=7.5,loc='upper left');ax.grid(axis='y',alpha=.2)
