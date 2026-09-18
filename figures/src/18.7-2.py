a=np.linspace(1,6500,500);net=.006-.001-.0002*np.sqrt(a/10);d=a*net
ax.plot(a,d,color=GOOD,lw=2,label='net alpha dollars per month')
ax.axhline(0,color=INK,lw=.8)
ax.axvline(6250,color=BAD,lw=1,ls=(0,(4,3)));ax.text(6150,0.4,'capacity 6.25B',fontsize=7.5,color=BAD,ha='right')
ax.scatter([2777.8],[4.63],color=INK,zorder=3,s=28);ax.annotate('peak at 4/9 of capacity:\n2.78B, 4.63M a month',xy=(2777.8,4.63),xytext=(3300,3.4),fontsize=7.5,arrowprops=dict(arrowstyle='->',lw=.8,color=INK))
ax.set_xlabel('AUM (USD millions)');ax.set_ylabel('USD millions per month')
ax.set_title('The rate falls all the way; the dollars peak and turn',loc='left');ax.legend(fontsize=7.5,loc='upper left');ax.grid(alpha=.25)
