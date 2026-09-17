N=np.arange(1,51)
ind=1/np.sqrt(N)
rho=0.35
corr=np.sqrt(rho+(1-rho)/N)
ax.plot(N,ind,color=GOOD,lw=2,label='zero correlation')
ax.plot(N,corr,color=BAD,lw=2,label='correlation = 0.35')
ax.set_xlabel('number of equal-weight holdings, N');ax.set_ylabel('relative portfolio volatility')
ax.legend(loc='upper right');ax.set_title('Diversification removes idiosyncratic, not common, risk',fontsize=9,loc='left')
