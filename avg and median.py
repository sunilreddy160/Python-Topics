# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
res = np.mean(np_height_in)
print(res)
# Print out the median of np_height_in
value = np.median(np_height_in)
print(value)
