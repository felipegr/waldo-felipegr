import cv2


class CropDetector:
    def __init__(self, file1_path, file2_path, threshold=0.95):
        self.image1 = cv2.imread(file1_path)
        self.image2 = cv2.imread(file2_path)
        self.threshold = threshold

        if self.image1 is None or self.image2 is None:
            raise RuntimeError('Informed file does not exist or is not an '
                               'image')

    def verify_images_crop(self):
        res = cv2.matchTemplate(self.image1, self.image2, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x = max_loc[1]
        y = max_loc[0]
        return (True, x, y) if max_val >= self.threshold else (False, -1, -1)
