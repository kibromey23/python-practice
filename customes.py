import sys
from PIL import Image

images = []

# check if images are provided
if len(sys.argv) < 2:
    print("Usage: python script.py image1 image2 ...")
    sys.exit()

for arg in sys.argv[1:]:
    try:
        image = Image.open(arg)
        images.append(image)
    except FileNotFoundError:
        print(f"File not found: {arg}")
        sys.exit()

# create GIF
images[0].save(
    "animated.gif",
    save_all=True,
    append_images=images[1:],
    loop=0,
    duration=500  # controls speed (ms)
)

print("GIF created successfully!")