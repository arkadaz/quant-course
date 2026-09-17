labels=['A: eig 1','A: eig 2','B: eig 1','B: eig 2'];vals=[4.162,-2.162,.890,10.110];cols=[ACCENT,BAD,GOOD,GOOD]
ax.bar(labels,vals,color=cols);ax.axhline(0,color=INK,lw=1);ax.set_ylabel('Hessian eigenvalue');ax.tick_params(axis='x',rotation=18);ax.set_title('Mixed signs expose a saddle',loc='left')
