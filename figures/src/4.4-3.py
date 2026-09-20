labels=['Equal 40/40/40','60/-40/20']
vals=[np.sqrt(3*.4**2),np.sqrt(.6**2+.4**2+.2**2)]
ax.bar(labels,vals,color=[GOOD,ACCENT],width=.5)
for i,v in enumerate(vals):ax.text(i,v+.025,f'{v:.4f}',ha='center',fontsize=10,color=INK)
ax.set_ylim(0,.9);ax.set_ylabel('L2 norm; gross = 1.20')
ax.set_title('Same gross, higher concentration',loc='left')
