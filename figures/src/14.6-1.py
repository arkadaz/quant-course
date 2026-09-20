
S=np.linspace(65,135,400);prem={'Straddle':7.975522335,'Strangle':1.666328288,'Risk reversal':.241566496,'Butterfly':3.690805953}
curves={'Straddle':np.abs(S-100),'Strangle':np.maximum(90-S,0)+np.maximum(S-110,0),'Risk reversal':np.maximum(S-110,0)-np.maximum(90-S,0),'Butterfly':np.maximum(S-90,0)-2*np.maximum(S-100,0)+np.maximum(S-110,0)}
for (name,y),c in zip(curves.items(),[ACCENT,WARM,BAD,GOOD]): ax.plot(S,y-prem[name],label=name,color=c)
ax.axhline(0,color=INK,lw=1);ax.set_xlabel('Spot at expiry (USD)');ax.set_ylabel('P&L (USD per share)');ax.legend(ncol=2)
