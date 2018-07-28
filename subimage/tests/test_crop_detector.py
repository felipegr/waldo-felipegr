import os

import pytest

from subimage.crop_detector import CropDetector


class TestCropDetector:
    fixtures = os.path.join('subimage', 'tests', 'fixtures')
    not_an_image_path = os.path.join(fixtures, 'not_an_image.txt')
    non_existing_path = os.path.join(fixtures, 'some_image.jpg')
    mario_path = os.path.join(fixtures, 'mario.jpg')
    mario_bw_path = os.path.join(fixtures, 'mario_bw.jpg')
    mario_crop_jpg_path = os.path.join(fixtures, 'mario_crop.jpg')
    mario_crop_png_path = os.path.join(fixtures, 'mario_crop.png')
    mario_crop_bw_png_path = os.path.join(fixtures, 'mario_crop_bw.png')
    media_path = os.path.join(fixtures, 'media.png')
    media_crop_jpg_path = os.path.join(fixtures, 'media_crop.jpg')
    media_crop_png_path = os.path.join(fixtures, 'media_crop.png')

    def test_initializes_correctly(self):
        detector = CropDetector(self.mario_path, self.mario_crop_jpg_path)
        assert detector.threshold == 0.95

        detector = CropDetector(self.mario_path, self.mario_crop_jpg_path, 0.8)
        assert detector.threshold == 0.8

    def test_initialization_raises_runtime_error_if_some_image_is_invalid(self):
        with pytest.raises(RuntimeError) as exc:
            CropDetector(self.not_an_image_path, self.mario_crop_jpg_path)

        assert 'Informed file does not exist or is not an image' in \
               str(exc.value)

        with pytest.raises(RuntimeError) as exc:
            CropDetector(self.mario_bw_path, self.non_existing_path)

        assert 'Informed file does not exist or is not an image' in \
               str(exc.value)

        with pytest.raises(RuntimeError) as exc:
            CropDetector(self.non_existing_path, self.not_an_image_path)

        assert 'Informed file does not exist or is not an image' in \
               str(exc.value)

    def test_correctly_detects_cropped_and_not_cropped_images(self):
        # Cropped images test cases
        detector = CropDetector(self.mario_path, self.mario_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is True
        assert x == 0
        assert y == 0

        detector = CropDetector(self.mario_path, self.mario_crop_jpg_path)
        detector_2 = CropDetector(self.mario_crop_jpg_path, self.mario_path)

        is_crop, x, y = detector.verify_images_crop()
        is_crop_2, x_2, y_2 = detector_2.verify_images_crop()

        assert is_crop == is_crop_2
        assert x == x_2
        assert y == y_2
        assert is_crop is True
        assert x == 76
        assert y == 147

        detector = CropDetector(self.mario_path, self.mario_crop_png_path)

        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is True
        assert x == 135
        assert y == 157

        detector = CropDetector(self.mario_bw_path, self.mario_crop_bw_png_path)

        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is True
        assert x == 135
        assert y == 157

        detector = CropDetector(self.media_path, self.media_crop_jpg_path)

        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is True
        assert x == 131
        assert y == 468

        detector = CropDetector(self.media_path, self.media_crop_png_path)

        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is True
        assert x == 461
        assert y == 517

        # Non cropped images test cases
        detector = CropDetector(self.mario_path, self.mario_bw_path)
        detector_2 = CropDetector(self.mario_path, self.mario_bw_path)
        is_crop, x, y = detector.verify_images_crop()
        is_crop_2, x_2, y_2 = detector_2.verify_images_crop()

        assert is_crop == is_crop_2
        assert x == x_2
        assert y == y_2
        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.mario_path, self.mario_crop_bw_png_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.mario_path, self.media_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.mario_path, self.media_crop_png_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.mario_path, self.media_crop_jpg_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.media_path, self.mario_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.media_path, self.mario_bw_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.media_path, self.mario_crop_jpg_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.media_path, self.mario_crop_png_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1

        detector = CropDetector(self.media_path, self.mario_crop_bw_png_path)
        is_crop, x, y = detector.verify_images_crop()

        assert is_crop is False
        assert x == -1
        assert y == -1
