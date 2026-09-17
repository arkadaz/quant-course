rng=np.random.default_rng(171);a=-20e6*rng.normal(.0002,.011,250);b=-20e6*rng.normal(.0002,.011,100000)
vals=[np.quantile(a,.99,method='inverted_cdf'),np.quantile(b,.99,method='inverted_cdf'),20e6*(.011*stats.norm.ppf(.99)-.0002)]
ax.bar(['Synthetic history','Monte Carlo','Analytic'],np.array(vals)/1000,color=[WARM,ACCENT,GOOD]);ax.set_ylabel('VaR 99% (USD thousand)')
