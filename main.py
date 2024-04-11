# ValueError: assignment destination is read-only

from PIL import Image

import numpy as np

img = np.array(Image.open('house.png'))

print(img.flags)

img.setflags(write=1)
