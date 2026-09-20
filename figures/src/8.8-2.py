w=np.linspace(0,1,120)
own=w*w*4+(1-w)**2*9
cross=2*w*(1-w)*2.4
ax.plot(w,own,color=MUTED,lw=2,label='own variances only')
ax.plot(w,own+cross,color=BAD,lw=2,label='full variance with covariance')
ax.set_xlabel('weight in SPX');ax.set_ylabel(r'Variance $((	ext{percentage points})^2/	ext{day})$');ax.legend(loc='upper right',fontsize=8)
ax.set_title('Positive covariance adds the missing cross-term',fontsize=9,loc='left')
