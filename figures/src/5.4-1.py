fig=ax.figure;ax.remove();ax=fig.add_subplot(111,projection='3d')
xq,xs=np.meshgrid(np.linspace(0,6,35),np.linspace(0,6,35));L=1134+24*xq+5*xs
ax.plot_surface(xq,xs,L,cmap='viridis',alpha=.82,linewidth=0)
ax.scatter([4],[6],[1260],color=BAD,s=42,label='primal optimum')
ax.scatter([0],[0],[1134],color=GOOD,s=38,label='dual lower bound')
ax.set_box_aspect((1.25,1,.62));ax.view_init(elev=24,azim=-58)
ax.set_xlabel(r'$x_Q$ (USD million)',labelpad=-3);ax.set_ylabel(r'$x_S$ (USD million)',labelpad=-3);ax.set_zlabel(r'$\mathcal{L}$ (USD)',labelpad=1);ax.tick_params(labelsize=7,pad=-1)
ax.legend(loc='upper left',fontsize=6.8);ax.set_title('Dual-feasible Lagrangian surface',loc='left',pad=2)
