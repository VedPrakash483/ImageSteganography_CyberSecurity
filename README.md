
## Getting Start


### Prerequisites

What things you need to install the software and how to install them

Python3.x
Windows, Linux or any other OS supporting python3.x

### Installing

Run the following command to update PIP
```
pip install --upgrade pip
```
Then, Run command to install all the dependecy library in the parent directory
```
pip install -r requirements.txt
```
And you are all set with the required setup!

## Working

This section covers step by step instructions to run the given python files
### A. huffman.py
The huffman.py file included in this project is responsible for creating a frequency table for the input text file, and then using a priority queue to generate a Huffman tree. This tree is then used to encode the given secret text into binary format.
In addition to encoding, the huffman.py file is also capable of decoding an encoded binary back into plain text. This is accomplished using the frequency provided to the code during encoding.
Overall, the huffman.py file is a crucial component of this project, responsible for the core encoding and decoding functionality of the Huffman Encoding and Compression algorithm.

huffman.py on execution gives us two options:
#### 1. Encoding:
parameters : the text file containig the secret message that needs to be encoded.

return : saves the encoded binary in a .txt file and also saves the frequency table which is needed for decoding.
#### 2. Decoding:
parameters : the encoded binary in a .txt file and the frequency table which is needed for decoding.

return :saves the decoded data in a (.txt) file.


output of a successful encoded and compressed data

### B. histo-shift.py
The histo-shift.py file included in this project is responsible for encoding a given binary string .txt file into a cover image. The image can be in any format, but .png is recommended for optimal encoding capacity and desired output.
Once the binary string and cover image are provided, the histo-shift.py program generates an encoded image in .png format. Additionally, it saves the enc_data.pkl file, which is necessary for decoding the given encoded image.
The histo-shift.py file is also capable of decoding a given encoded image, along with the provided enc_data.pkl file. Upon decoding, it returns a .txt file containing the binary encoded text that was retrieved from the image.
Overall, the histo-shift.py file is a key component of this project, responsible for encoding and decoding binary data into and from cover images, using the Histogram Shifting Steganography technique.

histo-shift.py on execution gives us three options:
#### 1. Encoding:
parameters : the text file containig the binary string that needs to be encoded and the cover image.

return : encoded image and enc_fre.pkl file which contains the data necesssary to decode
#### 2. Decoding:
parameters : encoded image and enc_fre.pkl file which contains the data necesssary to decode

return : saves the decoded binary in a .txt file.



output of a successful encoding of binary text file into a cover image

#### 3. Capacity:
parameters : Image you wish to use as a cover image in any format

return : encoding capacity of the image in bit.


output of testing capacity of different cover images

### C. main.py
The main.py file included in Analysis folder is used to find and analysis parameter for the encoded image. The main.py takes the origninal and encoded image an a command line argument. It runs three codes 1. pnsr.py, 2. pvd.py and 3.ssid.py which gives Peak Signal to Noise ratio, Mean Square Error and Stuctural Similarity respectively for the given original and encoded image. We can run the 3 tests individually too.


output main.py for given original and cover image

