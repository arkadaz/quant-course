S=np.array([[0.0004,0.00024],[0.00024,0.0009]])
vals=np.linalg.eigvalsh(S)[::-1]
labels=['Direction 1','Direction 2']
vals_bp2=vals*1e8
ax.bar(labels,vals_bp2,color=[BAD,WARM])
for i,v in enumerate(vals_bp2): ax.text(i,v+1800,f'{v:,.0f}',ha='center',fontsize=8)
ax.set_ylabel('eigenvalue ((basis points)²)')
ax.set_title('Eigenvalues rank the principal risk directions',fontsize=9,loc='left')
