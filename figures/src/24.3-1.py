from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
ax.axis('off')
nodes = [(.03, .42, 'Investor', ACCENT), (.27, .68, 'Broker', WARM), (.27, .18, 'Routing engine', WARM),
         (.54, .78, 'NYSE / NASDAQ', GOOD), (.54, .47, 'ATS', GOOD), (.54, .16, 'Dealer / maker', GOOD), (.81, .47, 'Fill + data', ACCENT)]
for x, y, label, col in nodes:
    ax.add_patch(FancyBboxPatch((x, y), .16, .12, boxstyle='round,pad=.02', facecolor=col, alpha=.17, edgecolor=col))
    ax.text(x + .08, y + .06, label, ha='center', va='center', fontsize=8)
edges = [((.19, .48), (.27, .73)), ((.19, .48), (.27, .23)), ((.43, .23), (.54, .22)), ((.43, .73), (.54, .82)),
         ((.43, .23), (.54, .52)), ((.70, .84), (.81, .53)), ((.70, .53), (.81, .53)), ((.70, .22), (.81, .53))]
for a, b in edges:
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='->', mutation_scale=12, color=INK, lw=1))
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.set_title('Illustrative US equity order route', loc='left')
