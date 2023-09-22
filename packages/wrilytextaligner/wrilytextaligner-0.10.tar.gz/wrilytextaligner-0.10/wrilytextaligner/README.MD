# Aligns text lines and characters within an image

## Tested against Windows 10 / Python 3.11 / Anaconda

## pip install wrilytextaligner

## Original
<img src="https://github.com/hansalemaos/screenshots/raw/main/16_2.png"/>


## Aligned
<img src="https://github.com/hansalemaos/screenshots/raw/main/16_3.png"/>



```python

i (Any): The input image or file path.
blured_kernel (Tuple[int, int], optional): The kernel size for blurring the input image. Defaults to (5, 5).
blured_dst (int, optional): The destination for the blurred image. Defaults to 0.
adaptiveThreshold_max_value (int, optional): The maximum pixel value for the adaptive thresholding. Defaults to 255.
adaptiveTreshold_method (int, optional): The adaptive thresholding method. Defaults to cv2.ADAPTIVE_THRESH_GAUSSIAN_C.
adaptiveThreshold_block_size (int, optional): The block size for adaptive thresholding. Defaults to 11.
adaptiveThreshold_C (int, optional): The constant subtracted from the mean in adaptive thresholding. Defaults to 2.
rect_kernel_size (Tuple[int, int], optional): The kernel size for morphological operations. Defaults to (10, 10).
otsu_threshold (int, optional): The threshold value for Otsu's thresholding. Defaults to 0.
otsu_max_value (int, optional): The maximum pixel value for Otsu's thresholding. Defaults to 255.
max_line_join_distance (int, optional): The maximum distance for joining lines. Defaults to 30.
border_color_letters (Tuple[int, int, int], optional): The color of borders around characters. Defaults to (255, 255, 255).
letter_border_top (int, optional): The top border size for characters. Defaults to 10.
letter_border_bottom (int, optional): The bottom border size for characters. Defaults to 10.
letter_border_right (int, optional): The right border size for characters. Defaults to 10.
letter_border_left (int, optional): The left border size for characters. Defaults to 10.
line_border_top (int, optional): The top border size for lines. Defaults to 10.
line_border_bottom (int, optional): The bottom border size for lines. Defaults to 10.
line_border_right (int, optional): The right border size for lines. Defaults to 10.
line_border_left (int, optional): The left border size for lines. Defaults to 10.
image2crop (Union[None, np.ndarray], optional): An optional image to be cropped instead of the input image. Defaults to None.



import os, cv2
import numpy as np
from wrilytextaligner import align_wrily_text

outputfolder = r"C:\readx2"
if not os.path.exists(outputfolder):
	os.makedirs(outputfolder)
for ini, fi in enumerate(
	[r"https://github.com/hansalemaos/screenshots/raw/main/16_2.png"]
):
	allines = align_wrily_text(
		i=fi,
		blured_kernel=(5, 5),
		blured_dst=0,
		adaptiveThreshold_max_value=255,
		adaptiveTreshold_method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		adaptiveThreshold_block_size=11,
		adaptiveThreshold_C=2,
		rect_kernel_size=(8, 8),
		otsu_threshold=0,
		otsu_max_value=255,
		max_line_join_distance=30,
		border_color_letters=(255, 255, 255),
		letter_border_top=10,
		letter_border_bottom=10,
		letter_border_right=10,
		letter_border_left=10,
		line_border_top=10,
		line_border_bottom=10,
		line_border_right=10,
		line_border_left=10,
		image2crop=None,
	)

	vstacked = np.vstack(allines)
	cv2.imwrite(rf"{outputfolder}\{ini}.png", vstacked)

```