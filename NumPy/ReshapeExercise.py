"""
We have a NumPy array like this: [[1, 2 , 3], [1, 2 , 3], [1, 2 , 3]]. 
Transform this two-dimensional array into a one-dimensional sequence.

So the result should be like this: [1, 2, 3, 1, 2, 3, 1, 2, 3]

There may be multiple solutions of course,
"""

import numpy as np

numpy_array = np.array([[1, 2 , 3], [1, 2 , 3], [1, 2 , 3]])

print('previous shape: %s' % str(numpy_array.shape))

numpy_array = numpy_array.reshape(1, -1)

print('new shape: %s' % str(numpy_array.shape))