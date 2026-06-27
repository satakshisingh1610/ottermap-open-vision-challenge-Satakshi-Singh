import os
import cv2

IMAGE_FOLDER = "data/images"
MASK_FOLDER = "data/masks"

OUT_IMAGE = "data/tiles/images"
OUT_MASK = "data/tiles/masks"

os.makedirs(OUT_IMAGE, exist_ok=True)
os.makedirs(OUT_MASK, exist_ok=True)

TILE_SIZE = 512

for image_file in os.listdir(IMAGE_FOLDER):

    base = os.path.splitext(image_file)[0]

    image = cv2.imread(os.path.join(IMAGE_FOLDER, image_file))
    mask = cv2.imread(
        os.path.join(MASK_FOLDER, base + "_mask.png"),
        cv2.IMREAD_GRAYSCALE
    )

    if image is None or mask is None:
        continue

    h, w = image.shape[:2]

    tile_num = 0

    for y in range(0, h, TILE_SIZE):
        for x in range(0, w, TILE_SIZE):

            img_tile = image[y:y+TILE_SIZE, x:x+TILE_SIZE]
            mask_tile = mask[y:y+TILE_SIZE, x:x+TILE_SIZE]

            if img_tile.shape[0] != TILE_SIZE or img_tile.shape[1] != TILE_SIZE:
                continue

            cv2.imwrite(
                os.path.join(
                    OUT_IMAGE,
                    f"{base}_{tile_num}.jpg"
                ),
                img_tile
            )

            cv2.imwrite(
                os.path.join(
                    OUT_MASK,
                    f"{base}_{tile_num}.png"
                ),
                mask_tile
            )

            tile_num += 1

print("Done!")