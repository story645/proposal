import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6,10))
l, = ax.plot([1,2,3], [1,2,3], label="hello")
ax.legend(bbox_to_anchor=(1, 1))
plt.show()