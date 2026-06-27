# 🛰️ Ottermap Open Vision / ML Engineer Technical Challenge

## 📌 Project Overview

This project implements an end-to-end computer vision pipeline for detecting **Turf / Grass** regions from aerial imagery using Deep Learning. The solution trains a semantic segmentation model on annotated aerial images and generates GIS-compatible outputs for unseen imagery.

The pipeline includes:

- Data preprocessing
- GeoJSON processing
- Mask generation
- Image tiling
- Model training
- Inference
- GeoJSON generation
- Overlay visualization

---

# 🏗️ Project Pipeline

```
GeoJSON Annotations
        │
        ▼
Mask Generation
        │
        ▼
Image Tiling
        │
        ▼
Train / Validation Split
        │
        ▼
U-Net (ResNet34 Encoder)
        │
        ▼
Prediction
        │
        ▼
Binary Mask
        │
        ▼
Overlay Image
        │
        ▼
GeoJSON Output
```

---

# 📂 Project Structure

```
Ottermap-Challenge/

│
├── data/
│   ├── images/
│   ├── annotations/
│   ├── masks/
│   ├── tiles/
│   └── final/
│
├── models/
│   └── best_model.pth
│
├── outputs/
│   ├── prediction.png
│   ├── overlay.png
│   └── prediction.geojson
│
├── scripts/
│   ├── create_masks.py
│   ├── geo_to_pixel.py
│   ├── tile_dataset.py
│   ├── split_dataset.py
│   └── check_image_metadata.py
│
├── train.py
├── inference.py
├── polygonize.py
├── requirements.txt
├── validation_report.json
└── README.md
```

---

# 📊 Dataset

The provided dataset consists of:

- High-resolution aerial imagery
- GeoJSON annotations
- Turf / Grass feature polygons

The preprocessing pipeline converts GeoJSON annotations into binary segmentation masks and prepares image tiles for training.

---

# 🤖 Model

Model Architecture:

- U-Net
- Encoder: ResNet34 (ImageNet pretrained)

Framework:

- PyTorch
- segmentation-models-pytorch

Loss Function:

- Dice Loss

Optimizer:

- Adam

Training Parameters:

| Parameter | Value |
|-----------|-------|
| Epochs | 15 |
| Batch Size | 4 |
| Learning Rate | 0.0001 |

---

# ⚙️ Installation

Clone the repository

```bash
git clone <git clone https://github.com/satakshisingh1610/ottermap-open-vision-challenge-Satakshi-Singh.git>
cd Ottermap-Challenge
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Training

Run

```bash
python train.py
```

The trained model is saved in

```
models/best_model.pth
```

---

# 🔍 Inference

Run inference on any aerial image

```bash
python inference.py --image data/images/1.jpg
```

Outputs generated:

```
outputs/
    prediction.png
    overlay.png
```

---

# 🌍 Generate GIS Output

Convert prediction masks into GeoJSON

```bash
python polygonize.py
```

Output

```
outputs/prediction.geojson
```

---

# 📈 Results

The model successfully learns to identify Turf / Grass regions from aerial imagery and generates:

- Binary segmentation masks
- Overlay visualizations
- GIS-compatible GeoJSON outputs

The solution demonstrates an end-to-end semantic segmentation workflow suitable for geospatial applications.

---

# ⚠️ Limitations

- Training dataset is limited to three annotated aerial images.
- Generalization performance may vary across different aerial imagery providers.
- Current implementation focuses on Turf / Grass segmentation.



---

# 🛠️ Technologies Used

- Python
- PyTorch
- segmentation-models-pytorch
- OpenCV
- GeoPandas
- NumPy
- Shapely

---

# 👩‍💻 Author

**Satakshi Singh**

B.Tech Computer Science (Data Science)

Machine Learning | Computer Vision | Full Stack Development
