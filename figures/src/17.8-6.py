mu=np.array([.06,.02,.04]);S=np.array([[.008,-.002,.004],[-.002,.002,-.002],[.004,-.002,.008]])
mh=np.array([-.0051864,.0470574,-.0069862]);Sh=np.array([[.0056,-.0020,.0037],[-.0020,.0022,-.0022],[.0037,-.0022,.0074]])
def frontier(m,V,targets):
    Vi=np.linalg.inv(V);o=np.ones(3);A=o@Vi@o;B=o@Vi@m;C=m@Vi@m;D=A*C-B*B
    return [Vi@(((C-B*t)/D)*o+((A*t-B)/D)*m) for t in targets]
tt=np.linspace(0.03,0.075,60);te=np.linspace(0.02,0.075,60)
wt=frontier(mu,S,tt);we=frontier(mh,Sh,te)
ax.plot([100*np.sqrt(w@S@w) for w in wt],[100*w@mu for w in wt],color=GOOD,lw=2,label='true frontier (sheet 1 means)')
ax.plot([100*np.sqrt(w@Sh@w) for w in we],[100*w@mh for w in we],color=ACCENT,lw=2,ls='--',label='estimated frontier (60 months)')
ax.plot([100*np.sqrt(w@S@w) for w in we],[100*w@mu for w in we],color=BAD,lw=2,label='same portfolios, true numbers')
ax.set_xlim(0,8);ax.set_ylim(0,8)
ax.set_xlabel('Volatility (%)');ax.set_ylabel('Expected return (%)')
ax.set_title('Assignment 2: the estimated frontier promises what it cannot deliver',loc='left');ax.legend(fontsize=7.2,loc='upper left');ax.grid(alpha=.2)
