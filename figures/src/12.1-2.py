n=np.array([8,16,32,64,128,256,512,1024]);sd=np.sqrt(2/n)
ax.loglog(n,sd,color=WARM,lw=2,marker='o');ax.set_xlabel('Partition count n');ax.set_ylabel('SD of $Q_n$ (years)');ax.set_title('Quadratic-variation noise shrinks as $n^{-1/2}$',loc='left');ax.grid(True,which='both',alpha=.25)
