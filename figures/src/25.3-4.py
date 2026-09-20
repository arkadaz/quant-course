k=np.linspace(0.02,8,400)
K=lambda kk:(0.5*(1+np.sqrt((2*kk)**2+1)))/((0.5*(1+np.sqrt((2*kk)**2+1)))+kk**2)
ax.plot(k,K(k),color=ACCENT,lw=2.3)
for kk,lab in [(0.46875,'this topic: 0.469 -> 0.844'),(5.0,'illiquid stock: 5.0 -> 0.180')]:
    ax.plot(kk,K(kk),'o',color=WARM,ms=7)
    ax.annotate(lab,xy=(kk,K(kk)),xytext=(14,10),textcoords='offset points',fontsize=8,color=WARM,
                arrowprops=dict(arrowstyle='->',color=WARM,lw=.8))
ax.annotate('trust the newest price',xy=(0.35,0.95),fontsize=7.5,color=MUTED)
ax.annotate('average many prices instead',xy=(4.2,0.55),fontsize=7.5,color=MUTED)
ax.set_xlabel('noise divided by true move, per interval');ax.set_ylabel('weight given to the newest price')
ax.set_ylim(0,1.05)
ax.set_title('The noisier the print, the more you have to average',loc='left')
