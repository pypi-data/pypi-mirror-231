from collections import defaultdict
from math import ceil
from typing import Any, Tuple, Union

import cv2
from a_cv_imwrite_imread_plus import open_image_in_cv
import numpy as np
from a_cv2_easy_resize import add_easy_resize_to_cv2
from intersection_grouper import group_lists_with_intersections

add_easy_resize_to_cv2()


def are_numbers_equal(number1, number2, allowed_difference=100):
    return abs(number1 - number2) < allowed_difference


def change_contrast(img, alpha=1.1, beta=0):
    return cv2.convertScaleAbs(img.copy(), alpha=alpha, beta=beta)


def add_border_right(
    image,
    target_width,
    border_color=(0, 0, 0),
    border_top=0,
    border_bottom=20,
    border_left=0,
    border_right=0,
):
    current_height, current_width, _ = image.shape
    border_width = target_width - current_width + border_right
    border = cv2.copyMakeBorder(
        image,
        border_top,
        border_bottom,
        border_left,
        border_width,
        cv2.BORDER_CONSTANT,
        value=border_color,
    )
    return border


def join_close_parts_and_get_contours(
    img,
    adaptiveThreshold_max_value=255,
    adaptiveTreshold_method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    adaptiveThreshold_block_size=11,
    adaptiveThreshold_C=2,
    rect_kernel_size=(10, 10),
):
    img_thresh = cv2.adaptiveThreshold(
        img,
        adaptiveThreshold_max_value,
        adaptiveTreshold_method,
        cv2.THRESH_BINARY_INV,
        adaptiveThreshold_block_size,
        adaptiveThreshold_C,
    )
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, rect_kernel_size)
    threshed = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, rect_kernel)
    cnts = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return cnts[0] if len(cnts) == 2 else cnts[1]


def crop_image(cnts, img):
    allpics = []
    for c, num in zip(cnts, range(len(cnts))):
        x, y, w, h = cv2.boundingRect(c)
        ROI = img[y : y + h, x : x + w]
        allpics.append([x, y, w, h, ROI.copy()])
    return allpics


def align_wrily_text(
    i: Any,
    blured_kernel: Tuple[int, int] = (5, 5),
    blured_dst: int = 0,
    adaptiveThreshold_max_value: int = 255,
    adaptiveTreshold_method: int = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    adaptiveThreshold_block_size: int = 11,
    adaptiveThreshold_C: int = 2,
    rect_kernel_size: Tuple[int, int] = (10, 10),
    otsu_threshold: int = 0,
    otsu_max_value: int = 255,
    max_line_join_distance: int = 30,
    border_color_letters: Tuple[int, int, int] = (255, 255, 255),
    letter_border_top: int = 10,
    letter_border_bottom: int = 10,
    letter_border_right: int = 10,
    letter_border_left: int = 10,
    line_border_top: int = 10,
    line_border_bottom: int = 10,
    line_border_right: int = 10,
    line_border_left: int = 10,
    image2crop: Union[None, np.ndarray] = None,
) -> list:
    r"""
    Aligns text lines and characters within an image.

    Args:
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

    Returns:
        list: A list of aligned and processed images containing handwritten text lines and characters.

    Example:

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

    """
    img2 = open_image_in_cv(i, channels_in_output=3)
    img = open_image_in_cv(img2.copy(), channels_in_output=2)
    try:
        len(image2crop)
    except Exception:
        image2crop = img2
    _, imgbw = cv2.threshold(
        img, otsu_threshold, otsu_max_value, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    imgbw = open_image_in_cv(imgbw, channels_in_output=3)
    gray = open_image_in_cv(imgbw.copy(), channels_in_output=2)
    blured = cv2.blur(gray, blured_kernel, blured_dst)
    cnts = join_close_parts_and_get_contours(
        blured,
        adaptiveThreshold_max_value=adaptiveThreshold_max_value,
        adaptiveTreshold_method=adaptiveTreshold_method,
        adaptiveThreshold_block_size=adaptiveThreshold_block_size,
        adaptiveThreshold_C=adaptiveThreshold_C,
        rect_kernel_size=rect_kernel_size,
    )

    allpics_data = crop_image(cnts, image2crop)
    allydata = [p[1] for p in allpics_data]
    joindist = int(max_line_join_distance)
    allydatamax = ceil(max(allydata) / joindist) * joindist
    resultsdefaultdict = defaultdict(list)
    for ycoord in range(0, allydatamax + 1, joindist):
        for p in allpics_data:
            if are_numbers_equal(
                number1=p[1], number2=ycoord, allowed_difference=joindist
            ):
                resultsdefaultdict[ycoord].append(p[1])

    groupedlines_y_coords = sorted(
        group_lists_with_intersections(
            list(resultsdefaultdict.values()), keep_duplicates=False
        ),
        key=lambda q: q[0],
    )
    linedict = defaultdict(list)
    for letter in allpics_data:
        for ini, yco in enumerate(groupedlines_y_coords):
            if letter[1] in yco:
                linedict[ini].append(letter)

    lineinorderdict = {k: linedict[k] for k in sorted(linedict.keys())}

    allinesnp = []
    allinesheight = []
    allineswidth = []
    for orderedlinekey, orderedlineitem in lineinorderdict.items():
        allpics = [xx[-1] for xx in sorted(orderedlineitem, key=lambda x: x[0])]
        dim = allpics[0].shape[:2]
        newpics = []
        for pic in allpics:
            resized = cv2.easy_resize_image(
                pic.copy(),
                width=None,
                height=dim[0],
                percent=None,
                interpolation=cv2.INTER_AREA,
            )
            resized = cv2.copyMakeBorder(
                resized,
                letter_border_top,
                letter_border_bottom,
                letter_border_left,
                letter_border_right,
                cv2.BORDER_CONSTANT,
                None,
                border_color_letters,
            )
            newpics.append(resized.copy())
        newarray = open_image_in_cv(np.hstack(newpics), channels_in_output=3)
        height1, width1, _ = newarray.shape

        allinesnp.append(newarray.copy())
        allinesheight.append(height1)
        allineswidth.append(width1)

    max_width = max(allineswidth)

    newarrayadjusted = []
    for image in allinesnp:
        newarrayadjusted.append(
            add_border_right(
                image,
                max_width,
                border_color=border_color_letters,
                border_top=line_border_top,
                border_bottom=line_border_bottom,
                border_left=line_border_left,
                border_right=line_border_right,
            )
        )
    return newarrayadjusted


