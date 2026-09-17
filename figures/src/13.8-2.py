
k=np.linspace(3000,7000,401);w=1/k**2
ax.plot(k,w/w[np.argmin(abs(k-5000))],color=ACCENT)
ax.axvline(5000,color=INK,ls='--',label='Forward 5,000')
ax.set_xlabel('Strike (SPX points)');ax.set_ylabel('Weight relative to K=5,000');ax.legend()
