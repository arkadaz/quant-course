gd=np.array([.300000,.253791,.242686,.240052,.239429,.239282]);nt=np.array([.300000,.239141,.239236]);root=.239236
ax.semilogy(np.arange(len(gd)),np.abs(gd-root)+1e-8,'o-',color=ACCENT,label='gradient descent');ax.semilogy(np.arange(len(nt)),np.abs(nt-root)+1e-8,'o-',color=GOOD,label='Newton')
ax.set_xlabel('Iteration');ax.set_ylabel('Absolute volatility error');ax.legend();ax.set_title('Curvature information can collapse the error faster',loc='left')
