from PIL import Image

# converting encoding data into 8-bit binary codes
def convertEncodingData(data):
    '''Takes in the text data and returns 
    8-bit binary code for each character'''
    binary_codes = []
    
    for ch in data:
        binary_codes.append(format(ord(ch), '08b'))
    
    return binary_codes

# modifying the pixels according to the 8-bit binary data
def modifyPixels(pixels, data):
    '''Takes the pixels of image and data to be encoded
    and modify the pixels of image according to data'''

    converted_data = convertEncodingData(data)
    data_length = len(converted_data)
    image_data = iter(pixels)

    # enocoding logic
    for i in range(data_length):
        pixel_values = [pixel for pixel in 
        image_data.__next__()[:3] + 
        image_data.__next__()[:3] + 
        image_data.__next__()[:3]]
    
        for j in range(0, 8):
            if converted_data[i][j] == '0' and pixel_values[j]%2 != 0:
                pixel_values[j] =- 1
            elif converted_data[i][j] == '1' and pixel_values[j]%2 == 0:
                if pixel_values[j] != 0:
                    pixel_values[j] -= 1
                else:
                    pixel_values[j] += 1

        if i == data_length - 1:
            if pixel_values[-1] % 2 == 0:
                if pixel_values[-1] != 0:
                    pixel_values[-1] -= 1
                else:
                    pixel_values[-1] += 1

        else:
            if pixel_values[-1] % 2 != 0:
                pixel_values[-1] -= 1

        pixels = tuple(pixel_values)
        yield pixels[0:3]
        yield pixels[3:6]
        yield pixels[6:9]

# encoding the data into the image
def encodeInImage(newimg, data):
    '''Encoding data into the image'''
    wid = newimg.size[0]
    (X, Y) = (0, 0)

    for pixel in modifyPixels(newimg.getdata(), data):
        newimg.putpixel((X, Y), pixel)
        if X == wid - 1:
            X = 0
            Y += 1
        else:
            X += 1

# encode function
def encode():
    '''Takes input of the image, data or text 
    to be encoded and apply encoding'''

    img = "static/images/encode.png" # image for encoding
    image = Image.open(img, 'r')

    data = "This is the message to be encoded"
    if len(data) == 0:
        raise ValueError('Data is empty!')

    newimg = image.copy()
    encodeInImage(newimg, data)

    encoded_img = "static/images/encoded.png"
    newimg.save(encoded_img, str(encoded_img.split(".")[1].upper()))


def decode():
    img = "static/images/decode.png" # image for decoding
    image = Image.open(img, 'r')

    decoded_data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [pixel for pixel in 
        imgdata.__next__()[:3] + 
        imgdata.__next__()[:3] + 
        imgdata.__next__()[:3]]

        binary_data = ''
        # reading pixel values to obtain binary data
        for i in pixels[:8]:
            if i % 2 == 0:
                binary_data += '0'
            else:
                binary_data += '1'
        # decoding data from binary data
        decoded_data += chr(int(binary_data, 2))
        if pixels[-1] % 2 != 0:
            return decoded_data

opt = input("Opt (E)/(D): ")
if opt == 'E':
    encode()
elif opt == 'D':
    decoded_data = decode()
    print(f"Decoded data: {decoded_data}")
else:
    raise Exception("Invalid Input!")
