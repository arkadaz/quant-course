mats=np.arange(1,11);N=10e6;c=.05;r=.045;la=.018;R=.4
def price(T,l): return sum(N*c*np.exp(-(r+l)*i) for i in range(1,T+1))+N*np.exp(-(r+l)*T)+N*R*l/(r+l)*(1-np.exp(-(r+l)*T))
c01=np.array([price(int(T),la+.0001)-price(int(T),la) for T in mats]);ax.bar(mats,-c01/1000,color=ACCENT);ax.set_xlabel('Bond maturity (years)');ax.set_ylabel('Loss for +1 bp hazard (USD thousands)');ax.set_title('Longer bonds carry more hazard sensitivity')
