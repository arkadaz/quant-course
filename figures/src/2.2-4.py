shares=[370000/461875,91875/461875]
labels=['Within-regime','Between-regime']
ax.barh(['Total'],[shares[0]],color=ACCENT,label='Within-regime')
ax.barh(['Total'],[shares[1]],left=[shares[0]],color=WARM,label='Between-regime')
ax.text(shares[0]/2,0,f'{shares[0]*100:.1f}%',ha='center',va='center',color='white',weight='bold')
ax.text(shares[0]+shares[1]/2,0,f'{shares[1]*100:.1f}%',ha='center',va='center',color='white',weight='bold')
ax.set_xlim(0,1); ax.set_xlabel('share of total variance')
ax.legend(loc='lower center',ncol=2)
ax.set_title('Variance attribution as a percentage of the risk budget',fontsize=9,loc='left')
