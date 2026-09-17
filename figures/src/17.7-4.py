k=np.arange(13);pr=stats.binom.pmf(k,250,.01);ax.bar(k,pr,color=[WARM if j==5 else ACCENT for j in k]);ax.set_xlabel('Exceptions in 250 forecasts');ax.set_ylabel('Null probability');ax.set_xticks(k)
