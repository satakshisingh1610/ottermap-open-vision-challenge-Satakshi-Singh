import os
import cv2
import numpy as np

import torch
from torch.utils.data import Dataset, DataLoader

import segmentation_models_pytorch as smp

from tqdm import tqdm

# ----------------------------
# Configuration
# ----------------------------

TRAIN_IMAGE_DIR = "data/final/train/images"
TRAIN_MASK_DIR = "data/final/train/masks"

VAL_IMAGE_DIR = "data/final/val/images"
VAL_MASK_DIR = "data/final/val/masks"

IMAGE_SIZE = 512
BATCH_SIZE = 4
EPOCHS = 15
LR = 1e-4

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print("Device :", DEVICE)

# ----------------------------
# Dataset
# ----------------------------

class TurfDataset(Dataset):

    def __init__(self, image_dir, mask_dir):

        self.image_dir = image_dir
        self.mask_dir = mask_dir

        self.images = sorted(os.listdir(image_dir))

    def __len__(self):

        return len(self.images)

    def __getitem__(self, idx):

        image_name = self.images[idx]

        image_path = os.path.join(self.image_dir, image_name)

        mask_path = os.path.join(
            self.mask_dir,
            image_name.replace(".jpg", ".png")
        )

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        image = image.astype(np.float32) / 255.0
        mask = mask.astype(np.float32) / 255.0

        image = np.transpose(image, (2, 0, 1))

        mask = np.expand_dims(mask, axis=0)

        return (
            torch.tensor(image, dtype=torch.float32),
            torch.tensor(mask, dtype=torch.float32)
        )

# ----------------------------
# Test Dataset
# ----------------------------

train_dataset = TurfDataset(
    TRAIN_IMAGE_DIR,
    TRAIN_MASK_DIR
)

print("Training Images :", len(train_dataset))

image, mask = train_dataset[0]

print("Image Shape :", image.shape)
print("Mask Shape  :", mask.shape)
# ----------------------------
# DataLoader
# ----------------------------

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_dataset = TurfDataset(
    VAL_IMAGE_DIR,
    VAL_MASK_DIR
)

val_loader = DataLoader(
    val_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("Train Batches :", len(train_loader))
print("Validation Batches :", len(val_loader))

# ----------------------------
# Model
# ----------------------------

model = smp.Unet(
    encoder_name="resnet34",
    encoder_weights="imagenet",
    in_channels=3,
    classes=1
)

model = model.to(DEVICE)

print("\nModel Loaded Successfully!")
# ----------------------------
# Loss Function & Optimizer
# ----------------------------

loss_fn = smp.losses.DiceLoss(
    mode="binary"
)

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=LR
)

best_loss = float("inf")

os.makedirs("models", exist_ok=True)

# ----------------------------
# Training Loop
# ----------------------------

for epoch in range(EPOCHS):

    model.train()

    train_loss = 0

    for images, masks in tqdm(train_loader):

        images = images.to(DEVICE)
        masks = masks.to(DEVICE)

        preds = model(images)

        loss = loss_fn(preds, masks)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        train_loss += loss.item()

    train_loss /= len(train_loader)

    # ------------------------
    # Validation
    # ------------------------

    model.eval()

    val_loss = 0

    with torch.no_grad():

        for images, masks in val_loader:

            images = images.to(DEVICE)
            masks = masks.to(DEVICE)

            preds = model(images)

            loss = loss_fn(preds, masks)

            val_loss += loss.item()

    val_loss /= len(val_loader)

    print("\n")
    print("=" * 50)
    print(f"Epoch {epoch+1}/{EPOCHS}")
    print(f"Train Loss : {train_loss:.4f}")
    print(f"Validation Loss : {val_loss:.4f}")

    if val_loss < best_loss:

        best_loss = val_loss

        torch.save(
            model.state_dict(),
            "models/best_model.pth"
        )

        print("✅ Best Model Saved")