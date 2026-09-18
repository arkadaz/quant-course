h=np.linspace(0.005,0.30,300);D=95.0
for V,c,lab in ((100,ACCENT,'V = 100 (before the mark)'),(97,WARM,'V = 97 (mark -3%)'),(95,BAD,'V = 95 (mark -5%)')):
    x=np.maximum(D-(1-h)*V,0)/h;ax.plot(100*h,np.minimum(x,V),color=c,lw=1.8,label=lab)
for V,v in ((100,66.67),(97,83.67)): ax.scatter([15],[v],color=INK,s=16,zorder=3)
ax.axvline(15,color='0.5',ls=':',lw=1);ax.text(15.5,20,'haircut 15%:\n66.67 and 83.67 to sell',fontsize=7)
ax.set_xlabel('Repo haircut h (%)');ax.set_ylabel('Assets that must be sold, x_min (USD M)')
ax.set_title('A higher haircut can force a sale of most of the book',loc='left');ax.legend(fontsize=7,loc='lower right');ax.grid(alpha=.2)
