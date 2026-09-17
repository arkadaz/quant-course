labels=['Base','Within variance -50%']
within=[370000,185000]
between=[91875,91875]
x=np.arange(len(labels))
ax.bar(x,within,color=ACCENT,label='Within-regime')
ax.bar(x,between,bottom=within,color=WARM,label='Between-regime')
ax.set_xticks(x,labels)
ax.set_ylabel('variance (USD²/day²)')
ax.legend(loc='upper right')
ax.set_title('A control must match the variance component',fontsize=9,loc='left')
