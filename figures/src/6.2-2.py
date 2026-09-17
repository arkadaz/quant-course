x=np.linspace(-10,10,400);sx,sy=2.5,3.0
fx=stats.norm.pdf(x,0,sx);fy=stats.norm.pdf(x,0,sy)
ax.plot(x,fx,color=ACCENT,lw=2,label='AAPL marginal PDF')
ax.plot(x,fy,color=WARM,lw=2,label='MSFT marginal PDF')
ax.set_xlabel('daily return (%)');ax.set_ylabel('density per percentage point')
ax.legend(loc='upper left');ax.set_title('Two normalized marginal PDFs from one joint model',fontsize=9,loc='left')
