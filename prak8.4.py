
import mahotas as mh
import numpy as np
import matplotlib.pyplot as plt

regions = np.zeros((8, 8), bool)
regions[:3, :3] = 1
regions[6:, 6:] = 1

labeled, nr_objects = mh.label(regions)

plt.imshow(labeled, interpolation='nearest')
plt.show()

labeled, nr_objects = mh.label(regions, np.ones((3, 3), bool))

sizes = mh.labeled.labeled_size(labeled)
print('Background size:', sizes[0])
print('Size of first region:', sizes[1])

array = np.random.random_sample(regions.shape)
sums = mh.labeled_sum(array, labeled)
print('Sum of first region:', sums[1])