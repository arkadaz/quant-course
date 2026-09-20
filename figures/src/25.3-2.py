se,sn,P0,M,D=0.0256,0.012,50.0,390,251
q=np.arange(1,121)
meas=np.sqrt(q*se**2+2*sn**2)/P0*np.sqrt(M/q*D)*100
truth=se/P0*np.sqrt(M*D)*100
ax.plot(q,meas,color=ACCENT,lw=2.2,label='volatility you would measure')
ax.axhline(truth,color=BAD,ls='--',lw=1.8,label=f'the truth, {truth:.2f}%')
for qq in (1,5,30):
    v=np.sqrt(qq*se**2+2*sn**2)/P0*np.sqrt(M/qq*D)*100
    ax.plot(qq,v,'o',color=WARM,ms=6)
    ax.annotate(f'{qq} min: {v:.2f}%',xy=(qq,v),xytext=(10,4),textcoords='offset points',fontsize=7.5,color=WARM)
ax.set_xlabel('minutes per sampled interval');ax.set_ylabel('annualised volatility (%)')
ax.set_ylim(15.6,20.0)
ax.set_title('Sample too often and you measure the spread, not the stock',loc='left')
ax.legend(fontsize=7,loc='upper right')
