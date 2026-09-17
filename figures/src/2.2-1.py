within=370000
between=91875
ax.bar(['Total variance'],[within],color=ACCENT,label='Expected within-regime variance')
ax.bar(['Total variance'],[between],bottom=[within],color=WARM,label='Between-regime variance')
ax.text(0,within/2,'370,000',ha='center',va='center',color='white',weight='bold')
ax.text(0,within+between/2,'91,875',ha='center',va='center',color='white',weight='bold')
ax.set_ylabel('variance (USD²/day²)')
ax.set_ylim(0,510000)
ax.legend(loc='upper right')
ax.set_title('Total variance = within regimes + between regimes',fontsize=9,loc='left')
