orig=np.array([.002,-.001,.004,-.032,.028,-.025,.003,.001,-.002,.004]);iid=orig[[3,0,5,1,8,4,2,9]];block=np.r_[orig[2:6],orig[6:10]]
for y,label,col in [(orig,'Observed',ACCENT),(iid,'Independent resample',WARM),(block,'Block resample',GOOD)]:ax.plot(np.arange(len(y)),100*y,marker='o',label=label,color=col)
ax.axhline(0,color=MUTED);ax.set_xlabel('Ordered observation');ax.set_ylabel('Return (%)');ax.legend(fontsize=7)
