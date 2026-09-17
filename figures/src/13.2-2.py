
from scipy.stats import norm
z=np.linspace(-3.7,3.7,500);cut=.437901642;y=norm.pdf(z)
ax.plot(z,y,color=ACCENT);ax.fill_between(z,0,y,where=z>=cut,color=WARM,alpha=.55)
ax.axvline(cut,color=BAD,ls='--',label='Exercise threshold')
ax.set_xlabel('Standard normal shock Z');ax.set_ylabel('Density');ax.legend()
