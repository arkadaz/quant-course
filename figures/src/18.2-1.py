m=np.array([.25,1,2,5,10,30]);y=np.array([4.8,4.6,4.35,4.15,4.2,4.35])
ax.plot(m,y,color=ACCENT,lw=2,marker='o');ax.set_xlabel('Maturity (years)');ax.set_ylabel('Yield (%)');ax.set_title('Illustrative UST yield curve',loc='left');ax.grid(alpha=.25)
