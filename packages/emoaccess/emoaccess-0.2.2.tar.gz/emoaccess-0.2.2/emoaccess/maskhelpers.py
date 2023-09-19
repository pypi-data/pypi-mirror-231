def convert_rect_to_poly(roi_coord):
    """
    Converts roi coordinates to polygon-style data structure if it is rectangle style.

    Args:
        roi_coord: 2xN numpy array of roi coordinates in either poly or rectangle format.

    Returns:
        A 2xN numpy array of roi coordinates with polygon data structure.
    """

    pass


def roi_to_mask(roi_coord, image_shape):
    """
    Converts roi coordinates to binary mask.
    From, https://gist.github.com/hadim/fa89b50bbd240c486c61787d205d28a6

    Args:
        roi_coord: 2xN numpy array of roi coordinates.
        image_shape: a tuple of image shape.

    Returns:
        A binary mask with area enclosed in roi set to True.
    """

    pass


def scale_verticies(vertices, img_shape):
    pass


def roi_df_to_mask_dict(roi_df):
    pass
