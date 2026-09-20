rng=np.random.default_rng(0)
z=rng.normal(size=(1200,2));R=np.array([[1.0,0.4],[0.4,1.0]]);L=np.linalg.cholesky(R);r=z@L.T
left=ax.inset_axes([0.04,0.12,0.43,0.76]);right=ax.inset_axes([0.54,0.12,0.43,0.76])
left.scatter(z[:,0],z[:,1],s=6,alpha=.18,color=MUTED);left.set_title('before: independent',fontsize=8)
right.scatter(r[:,0],r[:,1],s=6,alpha=.18,color=ACCENT);right.set_title('after: correlation 0.40',fontsize=8)
for a in (left,right):a.set_xlim(-4,4);a.set_ylim(-4,4);a.tick_params(labelsize=6);a.set_aspect('equal')
ax.set_xticks([]);ax.set_yticks([]);[sp.set_visible(False) for sp in ax.spines.values()]
ax.set_title('Cholesky reshapes independent shocks',fontsize=9,loc='left')
