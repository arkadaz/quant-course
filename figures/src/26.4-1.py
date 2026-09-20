v=np.array([40_000.,70_000.,50_000.,120_000.])
C=np.array([[1,.25,.45,0],[.25,1,-.15,0],[.45,-.15,1,0],[0,0,0,1]])
Om=np.outer(v,v)*C
p=Om.sum(axis=1)/Om.sum()*100
naive=v**2/(v**2).sum()*100
x=np.arange(4)
ax.bar(x-0.19,naive,width=.36,color=GRID,edgecolor=MUTED,label='ignoring the cross terms')
ax.bar(x+0.19,p,width=.36,color=ACCENT,label='counting them (the right answer)')
for i in range(4):
    ax.annotate(f'{naive[i]:.2f}',xy=(i-0.19,naive[i]),xytext=(0,4),textcoords='offset points',
                fontsize=7,ha='center',color=MUTED)
    ax.annotate(f'{p[i]:.2f}',xy=(i+0.19,p[i]),xytext=(0,4),textcoords='offset points',
                fontsize=7.5,ha='center',color=ACCENT)
ax.annotate('market nearly doubles:\nit amplifies the other groups',xy=(0.19,12.52),xytext=(0.5,33),
            fontsize=8,color=ACCENT,arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.9))
ax.set_xticks(x);ax.set_xticklabels(['market','style','industry','idio'])
ax.set_ylabel('share of total variance (%)')
ax.set_ylim(0,70)
ax.set_title('Cross terms are 0.2% of the total and still move the answer',loc='left')
ax.legend(fontsize=7,loc='upper left')
