import matplotlib.pylab as plt
import numpy as np

col_labels=['G','A','T','C','C']
row_labels= ['G','T','G','C','C']
table_vals= [
    ['X','','','',''],
    ['','','X','',''],
    ['X','','','',''],
    ['','','','X','X'],
    ['','','','X','X']]
line = np.array([
    [0, 1, 2, 2, 3, 4],
    [0, 0, 1, 2, 3, 4]])    
ncol = len(col_labels)
nrow = len(row_labels)

# draw grid lines
plt.plot(np.tile([0, ncol+1], (nrow+2,1)).T, np.tile(np.arange(nrow+2), (2,1)),
    'k', linewidth=3)
plt.plot(np.tile(np.arange(ncol+2), (2,1)), np.tile([0, nrow+1], (ncol+2,1)).T,
    'k', linewidth=3)

# plot labels
for icol, col in enumerate(col_labels):
    plt.text(icol + 1.5, nrow + 0.5, col, ha='center', va='center')
for irow, row in enumerate(row_labels):
    plt.text(0.5, nrow - irow - 0.5, row, ha='center', va='center')

# plot table content
for irow, row in enumerate(table_vals):
    for icol, cell in enumerate(row):
        plt.text(icol + 1.5, nrow - irow - 0.5, cell, ha='center', va='center')

# plot line
plt.plot(line[0] + 1.5, nrow - line[1] - 0.5, 'r', linewidth = 5, alpha = 0.5)

plt.axis([-0.5, ncol + 1.5, -0.5, nrow+1.5])
plt.show()
