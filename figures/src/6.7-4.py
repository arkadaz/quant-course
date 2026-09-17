S=np.array([[0.0004,0.00008,0.00012],[0.00008,0.0009,0.00018],[0.00012,0.00018,0.0006]])*1e8
upper=np.triu(S,1);lower=np.tril(S,-1)
ax.bar(['upper triangle','lower triangle'],[np.abs(upper).sum(),np.abs(lower).sum()],color=[ACCENT,GOOD])
ax.set_ylabel('absolute off-diagonal covariance sum (bp²)')
ax.set_title('Symmetry is a cheap covariance data check',fontsize=9,loc='left')
