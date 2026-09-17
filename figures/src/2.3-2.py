counts=np.array([5,12,20])
means=counts*75
ax.bar(counts.astype(str),means,color=ACCENT)
for i,v in enumerate(means): ax.text(i,v+35,f'{v:.0f}',ha='center',fontsize=8)
ax.set_xlabel('number of fills, n')
ax.set_ylabel('conditional expected sum (USD/day)')
ax.set_title('Given n fills, expected sum is n × 75 USD',fontsize=9,loc='left')
