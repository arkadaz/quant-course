b=np.linspace(1,30,300);nu=6/(b+2);ax.plot(b,nu,color=ACCENT,lw=2);ax.scatter([12],[3/7],color=BAD,s=45)
ax.set_xlabel('Budget, $b$ (USD million)');ax.set_ylabel('Shadow price (USD million/year per USD million)');ax.set_title('More capacity is worth less at the margin',loc='left')
