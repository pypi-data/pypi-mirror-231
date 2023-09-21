# cv2.putText with new lines 

## Tested against Windows 10 / Python 3.11 / Anaconda

### pip install cv2multilinewrite

Code from: https://stackoverflow.com/a/73471951/15096247


![](https://i.stack.imgur.com/2egap.png)

```python
import cv2
import numpy as np

image = 200 * np.ones((550, 410, 3), dtype=np.uint8)

image = add_text_to_image(
    image,
    "New line\nDouble new line\n\nLine too longggggggggggggggggggggg",
    top_left_xy=(0, 10),
)
image = add_text_to_image(
    image,
    "Different font scale",
    font_scale=0.5,
    font_color_rgb=(0, 255, 0),
    top_left_xy=(0, 150),
)
image = add_text_to_image(
    image,
    "New line with bg\nDouble new line\n\nLine too longggggggggggggggggggggg",
    bg_color_rgb=(255, 255, 255),
    font_color_rgb=(255, 0, 0),
    top_left_xy=(0, 200),
)
image = add_text_to_image(
    image,
    "Different line specing,\noutline and font face",
    font_color_rgb=(0, 255, 255),
    outline_color_rgb=(0, 0, 0),
    top_left_xy=(0, 350),
    line_spacing=1.5,
    font_face=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
)
import matplotlib.pyplot as plt

plt.imshow(image)
plt.show()
```