tenor = np.array([0, 0.25, 0.5, 0.75, 1.0])
S0 = 100
r = 0.05
div = 1.0
t_div = 0.25
cash = S0*np.exp(r*tenor) - div*np.exp(r*(tenor-t_div))*(tenor >= t_div)
curves = {'No dividend': S0*np.exp(r*tenor), 'Dividend yield q=2%': S0*np.exp((r-0.02)*tenor), 'Cash dividend at 0.25y': cash}
term_structure(ax, tenor, curves, title='Dividend income lowers the forward curve', ylabel='Forward price (USD)')
