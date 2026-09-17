w=np.linspace(0,1,240);mu=0.0004*w+0.0003*(1-w)
var=w*w*0.0004+(1-w)**2*0.0009+2*w*(1-w)*0.00024
ax.plot(np.sqrt(var)*100,mu*100,color=ACCENT,lw=2)
ax.scatter([np.sqrt(var[0])*100,np.sqrt(var[-1])*100],[mu[0]*100,mu[-1]*100],color=[WARM,ACCENT])
w60=0.6;v60=w60*w60*0.0004+(1-w60)**2*0.0009+2*w60*(1-w60)*0.00024;m60=0.0004*w60+0.0003*(1-w60)
ax.scatter([np.sqrt(v60)*100],[m60*100],color=BAD,s=35,label='60/40: 2.008% vol, 0.036% mean')
ax.set_xlabel('portfolio volatility (%/day)');ax.set_ylabel('expected return (%/day)');ax.legend(loc='best',fontsize=7)
ax.set_title('Weights trace a risk-return curve',fontsize=9,loc='left')
