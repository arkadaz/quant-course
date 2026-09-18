names=['start','grid search','Nelder-Mead','BFGS'];rmse=[0.8659,0.3670,0.2790,0.2661];kap=[2.30,1.80,1.9524,3.6941];sv=[0.0825,0.0925,0.1159,0.6059]
ax.bar(range(4),rmse,color=[MUTED,WARM,GOOD,ACCENT],width=.55)
for i,(v,k,s) in enumerate(zip(rmse,kap,sv)):
    ax.text(i,v+.02,f'RMSE {v:.4f}\nkappa {k:g}\nsigma_v {s:g}',ha='center',fontsize=7.3)
ax.set_xticks(range(4));ax.set_xticklabels(names);ax.set_ylim(0,1.1)
ax.set_ylabel('RMSE on the Apple call surface (USD)')
ax.set_title('Lower error, very different parameters',loc='left');ax.grid(axis='y',alpha=.2)
