# CSS-IA1-Steganography

## Steganography
**Steganography** is the process of hiding a secret message within a larger one in such a way that someone can not know the presence or contents of the hidden message. The purpose of Steganography is to maintain secret communication between two parties. Unlike cryptography, which conceals the contents of a secret message, steganography conceals the very fact that a message is communicated.

### Image Steganography
Image Steganography is the method of hiding secret data in an image. In a nutshell, the main motive of steganography is to hide the intended information within any image that doesn’t appear to be secret just by looking at it.

### How It works?
The idea behind **image-based** Steganography is very simple. Images are composed of digital data (pixels), which describes what’s inside the picture, usually the colors of all the pixels. Since we know every image is made up of pixels and every pixel contains 3-values (red, green, blue). Therefore, an image is represented as an N x M (in case of greyscale images) or N x M x 3 (in case of color images) matrix in memory, with each entry representing the intensity value of a pixel. In image steganography, a message is embedded into an image by altering the values of some pixels, which are chosen by an encryption algorithm. The recipient of the image must be aware of the same algorithm in order to know which pixels he or she must select to extract the message.


## Our Application - Image Steganography using Python
This is a web application capable of Encoding data (text) into the image and Decoding data from an existing image.

### Functionalities:
#### 1. Encode
- Lets user to provide text input (data to be encoded) or upload a text file.
- User can then upload an image in which the data will be encoded.
- After clicking on Encode, the data will be encoded into the image and the image with encoded data can be downloaded.

#### 2. Decode
- Lets user to upload an image with the encoded data.
- After clicking on Decode, the decoded data will be shown to the user.

## Steps to set up:
- Set up Python virtual environment in your project directory
  Use cmd: `python -m venv <Name of venv>`
- Clone this repository in above directory
- Activate your virtual environment using 
  cmd: `venv> Scripts\activate` 
- If using VScode simply select the python interpreter from this directory and open new terminal
- Install Flask using `pip install flask`
- Run app using cmd: `flask run`
- Project will then run on localhost (http://127.0.0.1:5000/)
