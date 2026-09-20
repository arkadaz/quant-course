rng=np.random.default_rng(651);n=65536;w=np.r_[0,np.cumsum(rng.normal(0,np.sqrt(1/n),n))]
for j,(m,off,col,label) in enumerate([(65536,4,ACCENT,'full interval'),(4096,2,WARM,'zoom 1/16'),(256,0,GOOD,'zoom 1/256')]):
    seg=w[:m+1]-w[0];scale=np.sqrt(m/n);xx=np.linspace(0,1,m+1);yy=seg/scale+off;ax.plot(xx,yy,color=col,lw=.9,label=label)
ax.set_xlabel('Rescaled time');ax.set_yticks([]);ax.set_title('Zooming changes scale, not roughness',loc='left');ax.legend(loc='upper right')
