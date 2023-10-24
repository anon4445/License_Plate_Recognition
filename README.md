# Bengali License Plate Recognition

This Streamlit application is designed to recognize and extract Bengali license plate numbers from images. It utilizes computer vision techniques with OpenCV, EasyOCR for optical character recognition, and the Python Imaging Library (PIL) to process and display the results.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. Clone the repository to your local machine:


2. Change the directory to the project folder:


3. Install the required Python libraries using pip:


4. Run the Streamlit app:


## Usage

1. Once you've launched the Streamlit app, you can upload an image containing a Bengali license plate.

2. The app will process the image and display it on the left side of the screen.

3. On the right side, you will see a "Detecting..." message along with a spinner, indicating that the application is working.

4. After processing, the recognized Bengali license plate number will be displayed on the right side of the screen.

5. If no license plate is detected, the app will display a "License Plate Not Detected!" message.

## Dependencies

This application relies on the following Python libraries:

- [Streamlit](https://streamlit.io/): For building the web-based user interface.
- [OpenCV](https://opencv.org/): For computer vision and image processing.
- [NumPy](https://numpy.org/): For numerical operations on image data.
- [Imutils](https://github.com/jrosebr1/imutils): For convenience functions for OpenCV.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR): For Optical Character Recognition (OCR) of Bengali text.
- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/en/stable/index.html): For image manipulation.

Make sure to install these libraries as described in the [Installation](#installation) section.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
