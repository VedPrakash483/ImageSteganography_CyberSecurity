import sys
import subprocess

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python main.py <original_image_path> <encoded_image_path>")
    sys.exit(1)

# Get the file paths from command line arguments
original_path = sys.argv[1]
encoded_path = sys.argv[2]

# Run scripts
subprocess.call(["python3", "psnr.py", original_path, encoded_path])
subprocess.call(["python3", "ssim.py", original_path, encoded_path])
subprocess.call(["python3", "pvd.py", original_path, encoded_path])
