c1=np.array([1.0,2.0,3.0]); c2=2*c1
ax.scatter(c1,c2,color=ACCENT,s=35)
line=np.linspace(0,3.5,100); ax.plot(line,2*line,color=BAD,ls='--')
ax.set_xlabel('column 1 value');ax.set_ylabel('column 2 value')
ax.set_title('Collinear columns reveal rank deficiency',fontsize=9,loc='left')
