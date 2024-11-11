import cv2
import numpy as np
import pickle

def histogram_8bit(image):
    num_of_bins = 256
    intensities_array = np.zeros(num_of_bins, dtype=int)
    
    # Count pixel intensities
    for pixel in image.flatten():
        intensities_array[pixel] += 1  

    return np.arange(num_of_bins), intensities_array

def max_data(cover_image):
    if cover_image.dtype != "uint8":
        raise ValueError("Image must be an 8-bit unsigned integer.")
    
    _, intensities = histogram_8bit(cover_image)
    peak_point = np.argmax(intensities)
    return intensities[peak_point]

def hide_data(cover_image, bit_stream):
    if cover_image.dtype != "uint8":
        raise ValueError("Image must be an 8-bit unsigned integer.")
    
    _, intensities = histogram_8bit(cover_image)
    peak_point = np.argmax(intensities)
    
    if len(bit_stream) > intensities[peak_point]:
        raise ValueError("Bit stream is too long for this image.")
        
    # Shift histogram values larger than the peak point
    cover_image[cover_image > peak_point] += 1

    # Hide information
    bit_count = 0
    for i in range(cover_image.shape[0]):
        for j in range(cover_image.shape[1]):
            if bit_count < len(bit_stream):
                if cover_image[i, j] == peak_point:
                    cover_image[i, j] += int(bit_stream[bit_count])
                    bit_count += 1
            else:
                break
    return cover_image, peak_point

def reveal_data(cover_image, peak_point, size):
    if cover_image.dtype != "uint8":
        raise ValueError("Image must be an 8-bit unsigned integer.")
    
    bit_stream = []
    bit_count = 0
    for i in range(cover_image.shape[0]):
        for j in range(cover_image.shape[1]):
            if bit_count < size:
                pixel = cover_image[i, j]
                bit_stream.append('1' if pixel == peak_point + 1 else '0')
                bit_count += 1
            else:
                break
    
    return ''.join(bit_stream)

def encode_image(img_path, txt_path):
    img = cv2.imread(img_path)
    channels = cv2.split(img)

    with open(txt_path, "r") as f:
        secret_data = f.read()

    print(f'Characters to be encoded: {len(secret_data)}')

    max_data_limits = [max_data(channel) for channel in channels]
    total_limit = sum(max_data_limits)

    print(f'Total image encoding limit: {total_limit}')
    for i, color in zip(['Red', 'Green', 'Blue'], max_data_limits):
        print(f'The max data encoded in {color} channel is {color}')

    if total_limit < len(secret_data):
        print(f'The image capacity is less for the given data, less by: {len(secret_data) - total_limit} characters!')
        return

    remaining_data = secret_data
    encoded_data_info = []

    for i, channel in enumerate(channels):
        channel_limit = max_data_limits[i]
        data_to_encode = remaining_data[:channel_limit]
        remaining_data = remaining_data[channel_limit:]

        if data_to_encode:
            channel, peak_point = hide_data(channel, data_to_encode)
            encoded_data_info.append((peak_point, len(data_to_encode)))

    with open('enc_data.pkl', 'wb') as f:
        pickle.dump(encoded_data_info, f)

    merged = cv2.merge(channels)
    cv2.imwrite('enc.png', merged)
    print("Image encoding done! Encoded image saved.")

def decode_image(enc_img_path, enc_data_path):
    enc_img = cv2.imread(enc_img_path)
    channels = cv2.split(enc_img)

    try:
        with open(enc_data_path, 'rb') as f:
            data_info = pickle.load(f)
    except Exception as e:
        print("Error loading pickle file:", e)
        return

    decoded_bits = []
    for channel, (peak_point, size) in zip(channels, data_info):
        decoded_bits.append(reveal_data(channel, peak_point, size))

    with open('decoded.txt', 'w') as decoded_file:
        decoded_file.write(''.join(decoded_bits))
    print("Image decoded!")

def check_capacity(img_path):
    img = cv2.imread(img_path)
    channels = cv2.split(img)

    max_data_limits = [max_data(channel) for channel in channels]
    total_limit = sum(max_data_limits)

    print(f"The maximum data encoded in the image is {total_limit}")

def main():
    process = input("Enter 1 for Encoding, Enter 2 for Decoding, and 3 to check capacity of Cover Image: ")
    if process == '1':
        img = input("Enter cover image name in .png format: ")
        text = input("Enter text file with the binary encrypted data in .txt format: ")
        encode_image(img, text)
    elif process == '2':
        img = input("Enter name of image to be decoded in .png format: ")
        text = input("Enter file with the binary encrypted data in .pkl format: ")
        decode_image(img, text)
    elif process == '3':
        img = input("Enter name of cover image in .png format: ")
        check_capacity(img)
    else:
        print("Please enter a valid input!")

if __name__ == "__main__":
    main()
