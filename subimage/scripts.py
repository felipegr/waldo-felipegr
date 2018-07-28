import click

from subimage.crop_detector import CropDetector


@click.command()
@click.argument('file1_path', type=click.Path(exists=True))
@click.argument('file2_path', type=click.Path(exists=True))
def cli(file1_path, file2_path):
    try:
        detector = CropDetector(file1_path, file2_path)
        is_crop, x, y = detector.verify_images_crop()
        result = 'One of the images is not a cropped part of the other one'
        if is_crop:
            result = ('One of the images is a cropped part of the other one.\n'
                      'Position of top-left corner of the cropped image within '
                      f'the original image: ({x}, {y})')

        print(result)
    except RuntimeError as exc:
        print(f'Error: {exc}')
    except Exception as exc:
        print(f'An unknown exception occurred: {exc}')
