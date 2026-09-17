mins=np.array([1/60,1/12,1/6,.5,1,2,5,10,15,30,60]);signal=1.44;noise=.18/np.sqrt(mins);smoothing=.00055*mins**1.35;rv=signal+noise+smoothing
ax.plot(mins,rv,color=ACCENT,lw=2,marker='o',ms=4);ax.axhline(signal,color=GOOD,ls='--',lw=1.2,label='integrated variance target')
ax.axvspan(5,15,color=GOOD,alpha=.10,label='stable sampling region');ax.set_xscale('log');ax.set_xlabel('Sampling interval (minutes)');ax.set_ylabel('Realized variance (% points squared)');ax.set_title('Microstructure noise creates a high-frequency bias',loc='left');ax.legend(loc='upper right')
