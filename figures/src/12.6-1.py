labels=['Stocks','Bonds','Tech'];u=np.array([.171392,.893041,-.064433]);k=np.array([.105263,.894737,0]);x=np.arange(3);bw=.36
ax.bar(x-bw/2,u*100,bw,color=WARM,label='shorting allowed');ax.bar(x+bw/2,k*100,bw,color=GOOD,label='long-only KKT');ax.axhline(0,color=INK,lw=1)
ax.annotate('tech -6.44%',xy=(2-bw/2,-6.44),xytext=(1.35,-20),arrowprops=dict(arrowstyle='->',color=WARM),color=WARM)
ax.set_xticks(x,labels);ax.set_ylabel('Weight (%)');ax.set_ylim(-28,100);ax.legend();ax.set_title('The mandate changes the active set',loc='left')
