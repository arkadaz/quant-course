h=np.logspace(-6,-1,300);sd=1/np.sqrt(h)
ax.loglog(h,sd,color=ACCENT,lw=2,label=r'$1/\sqrt{h}$')
for x in [1e-2,1e-4,1e-6]:ax.scatter(x,1/np.sqrt(x),color=BAD,s=35,zorder=4);ax.annotate(f'{1/np.sqrt(x):.0f}',(x,1/np.sqrt(x)),xytext=(5,4),textcoords='offset points',fontsize=8)
ax.invert_xaxis();ax.set_xlabel('Interval $h$ (smaller to the right)');ax.set_ylabel('SD of secant slope');ax.set_title('Brownian slopes become less stable under zoom',loc='left');ax.legend(loc='upper left')
