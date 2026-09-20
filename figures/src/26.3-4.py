B=np.array([[1,1.2,1],[1,-0.4,1],[1,0.6,0],[1,-1.4,0]],float)
raw=np.array([0.5,-1.5,1.0,0.0])
new=(np.eye(4)-B@np.linalg.pinv(B))@raw
old=raw-new
x=np.arange(4)
ax.bar(x-0.26,raw,width=.25,color=MUTED,label='the raw characteristic')
ax.bar(x,old,width=.25,color=ACCENT,label='part the model already had')
ax.bar(x+0.26,new,width=.25,color=WARM,label='what is genuinely new')
ax.axhline(0,color=INK,lw=.9)
ax.set_xticks(x);ax.set_xticklabels(['A','B','C','D'])
ax.set_ylabel('loading')
ax.annotate('length 1.871',xy=(1-0.26,-1.5),xytext=(-4,-16),textcoords='offset points',fontsize=7.5,color=MUTED,ha='center')
ax.annotate('length 0.663\nonly 35.4% survives',xy=(1+0.26,new[1]),xytext=(1.55,-1.15),fontsize=8,color=WARM,
            arrowprops=dict(arrowstyle='->',color=WARM,lw=.9))
ax.annotate('the new column sums to zero,\nso it is orthogonal to market',xy=(2.6,0.75),fontsize=7.5,color=INK)
ax.set_ylim(-1.95,1.35)
ax.set_title('Most of a new idea is usually an old idea',loc='left')
ax.legend(fontsize=7,loc='lower left')
