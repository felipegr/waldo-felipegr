# waldo-felipegr
Application that takes two images as arguments and checks if one of the images
 is a cropped part of the other one. If yes, it returns the position of top-left
 corner of the cropped image within the original image.

## Installation
The application requires **Python 3.6**.

Usually a virtualenv is created:
```sh
$ python3 -m venv env
$ source env/bin/activate
```

To install the requirements:
```sh
$ pip install -e .
```

## Running the application
```sh
$ subimage ./images/image1.jpeg ./images/image2.jpeg
```

## Running the tests
To install the tests' requirements:
```sh
$ pip install -e .[testing]
```

To run all the tests:
```sh
$ pytest -v
```

## Important considerations
For the cropped image to be considered part of the original image by the application
 it must not have been transformed in any way - the application takes into account even
 if the colors match. It won't be considered a cropped image some that was extracted
 from the original one but was rotated, enlarged, diminished, etc.
 
 The assumption made by the author is that an image is considered a cropped image
 of another only if the earlier was "copied" from the later and saved as another
 image, even if some lossy compression was applied.
