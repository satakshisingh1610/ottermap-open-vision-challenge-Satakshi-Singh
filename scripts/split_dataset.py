import os
import shutil
import random

random.seed(42)

IMAGE_DIR = "data/tiles/images"
MASK_DIR = "data/tiles/masks"

TRAIN_IMG = "data/final/train/images"
TRAIN_MASK = "data/final/train/masks"

VAL_IMG = "data/final/val/images"
VAL_MASK = "data/final/val/masks"

for folder in [TRAIN_IMG, TRAIN_MASK, VAL_IMG, VAL_MASK]:
    os.makedirs(folder, exist_ok=True)

images = sorted(os.listdir(IMAGE_DIR))

random.shuffle(images)

split = int(len(images) * 0.8)

train = images[:split]
val = images[split:]

for img in train:

    shutil.copy(
        os.path.join(IMAGE_DIR, img),
        os.path.join(TRAIN_IMG, img)
    )

    shutil.copy(
        os.path.join(MASK_DIR, img.replace(".jpg", ".png")),
        os.path.join(TRAIN_MASK, img.replace(".jpg", ".png"))
    )

for img in val:

    shutil.copy(
        os.path.join(IMAGE_DIR, img),
        os.path.join(VAL_IMG, img)
    )

    shutil.copy(
        os.path.join(MASK_DIR, img.replace(".jpg", ".png")),
        os.path.join(VAL_MASK, img.replace(".jpg", ".png"))
    )

print("Train Images:", len(train))
print("Validation Images:", len(val))