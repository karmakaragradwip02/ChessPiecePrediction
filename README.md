# Chess Piece Prediction
## Creating new conda environment

```bash
conda create -n yolo_od python>=3.8 -y
conda activate yolo_od
```

## Installing dependencies

```bash
pip install -r requirements.txt # It will install the requirements and automatically run setup.py file
```

## Installing the pytorch for gpu

```bash
# Installation for windows
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  # for CUDA 11.8
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121  # for CUDA 12.1
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124  # for CUDA 12.4
```