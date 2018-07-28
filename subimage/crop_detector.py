import cv2


class CropDetector:
    """
    Class used to check if an image is a cropped part of another image
    """
    def __init__(self, file1_path, file2_path, threshold=0.95):
        """
        Initializes the class with a default threshold
        
        :param file1_path: Path of an image file
        :param file2_path: Path of an image file
        :param threshold: Float number used as threshold of comparison
        
        :raises
            RuntimeError: if at least one of the paths points to a file that
            doesn't exist or it's not an image
        """
        self.image1 = cv2.imread(file1_path)
        self.image2 = cv2.imread(file2_path)
        self.threshold = threshold

        if self.image1 is None or self.image2 is None:
            raise RuntimeError('Informed file does not exist or is not an '
                               'image')

    def verify_images_crop(self):
        """
        Verifies if one of the images of the class instance is a cropped part
        of the other image.
        
        :return:
            `boolean` indicating if one image is a cropped part of the other;
            `int` indicating the X coordinate of the point where the upper
                left corner of the cropped image is located in the original
                image, -1 if the image is not cropped;
            `int` indicating the Y coordinate of the point where the upper
                left corner of the cropped image is located in the original
                image, -1 if the image is not cropped
        """
        res = cv2.matchTemplate(self.image1, self.image2, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x = max_loc[1]
        y = max_loc[0]
        return (True, x, y) if max_val >= self.threshold else (False, -1, -1)
