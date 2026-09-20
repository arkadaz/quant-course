labels=['One asset','Two duplicate assets','Three duplicate assets']
cols=[1,2,3]; ranks=[1,1,1]
ax.bar(labels,cols,color=ACCENT,label='columns')
ax.plot(labels,ranks,color=BAD,marker='o',lw=2,label='rank')
ax.set_ylabel('count');ax.legend(loc='upper left')
ax.set_title('More columns do not guarantee more information',fontsize=9,loc='left')
