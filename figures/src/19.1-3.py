tenor = np.array([0, 0.25, 0.5, 0.75, 1.0])
term_structure(ax, tenor, {'Contango': np.array([5000, 5065, 5127, 5190, 5256]), 'Backwardation': np.array([5000, 4940, 4885, 4830, 4780])}, title='Curve shape is not the same as arbitrage', ylabel='Futures level (points)')
