v=np.array([81,9,1])/91*100;ax.bar(['Level','Slope','Curvature'],v,color=[ACCENT,WARM,GOOD]);ax.set_ylabel('Explained variance (%)')
for i,y in enumerate(v):ax.text(i,y+2,f'{y:.2f}%',ha='center')
ax.set_ylim(0,102)
