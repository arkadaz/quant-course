ten=[2,7,20]
L=[('PC1 level (+ + +)',[0.566,0.599,0.566],ACCENT,.06),('PC2 slope (+ 0 -)',[0.707,0,-0.707],WARM,.08),('PC3 curvature (+ - +)',[0.423,-0.801,0.423],GOOD,-.14)]
for n,v,c,dy in L:
    ax.plot(ten,v,marker='o',color=c,lw=1.8,label=n)
    for x,y in zip(ten,v): ax.text(x+.35,y+dy,f'{y:+.3f}',fontsize=7,color=c)
ax.axhline(0,color=MUTED,lw=.9);ax.set_xticks(ten);ax.set_ylim(-1,1);ax.set_xlim(1,23)
ax.set_xlabel('Maturity (years)');ax.set_ylabel('Loading (unit length)')
ax.set_title('Correlations 0.90 next door, 0.75 end to end: three shapes',loc='left');ax.legend(fontsize=7.2,loc='lower left');ax.grid(alpha=.2)
