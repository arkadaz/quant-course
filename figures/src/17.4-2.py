lab=['PC1 level','PC2 slope','PC3 curvature','PC4-PC8']
three=[90.06,8.33,1.60,0];eight=[84.2,11.6,3.1,1.1]
x=np.arange(4);w=.36
ax.bar(x-w/2,three,w,color=ACCENT,label='3 maturities, by hand')
ax.bar(x+w/2,eight,w,color=WARM,label='all 8 maturities, from data')
for xi,a,b in zip(x,three,eight):
    if a: ax.text(xi-w/2,a+1.5,f'{a:.2f}%',ha='center',fontsize=7.3)
    ax.text(xi+w/2,b+1.5,f'{b:.1f}%',ha='center',fontsize=7.3)
ax.set_xticks(x);ax.set_xticklabels(lab,fontsize=8);ax.set_ylim(0,102)
ax.set_ylabel('Share of total variance (%)')
ax.set_title('One direction carries most of the curve risk',loc='left');ax.legend(fontsize=7.5);ax.grid(axis='y',alpha=.2)
