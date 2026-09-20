
terms=np.array([-8.91134085,1.47087462,7.53610130,-.09563508]);labels=[r'$\Theta$', r'$r S \Delta$', r'$0.5\,\sigma^2 S^2 \Gamma$', r'$-r C$']
ax.bar(labels,terms,color=[BAD,WARM,ACCENT,MUTED]);ax.axhline(0,color=INK,lw=1)
ax.set_ylabel('PDE contribution (USD/year)');ax.tick_params(axis='x',rotation=13)
