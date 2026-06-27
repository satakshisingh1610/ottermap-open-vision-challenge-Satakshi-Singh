import argparse
import cv2
import numpy as np
import torch
import segmentation_models_pytorch as smp
import os

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Load model
model = smp.Unet(
    encoder_name="resnet34",
    encoder_weights=None,
    in_channels=3,
    classes=1
)

model.load_state_dict(torch.load("models/best_model.pth", map_location=DEVICE))
model.to(DEVICE)
model.eval()

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--image", required=True)
args = parser.parse_args()

# Read image
image = cv2.imread(args.image)

if image is None:
    raise ValueError("Image not found.")

original = image.copy()

# Preprocess
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.astype(np.float32) / 255.0
image = np.transpose(image, (2, 0, 1))

image = torch.tensor(image, dtype=torch.float32).unsqueeze(0).to(DEVICE)

# Prediction
with torch.no_grad():
    pred = model(image)
    pred = torch.sigmoid(pred)

pred = pred.squeeze().cpu().numpy()

# Binary mask
pred = (pred > 0.5).astype(np.uint8) * 255

# Save prediction mask
cv2.imwrite("outputs/prediction.png", pred)
print("Prediction saved to outputs/prediction.png")

# ----------------------------
# Create Overlay
# ----------------------------

# Convert mask to 3 channels
mask_color = np.zeros_like(original)
mask_color[:, :, 1] = pred      # Green mask

# Blend original image + mask
overlay = cv2.addWeighted(
    original,
    0.7,
    mask_color,
    0.3,
    0
)

cv2.imwrite("outputs/overlay.png", overlay)

print("Overlay saved to outputs/overlay.png")