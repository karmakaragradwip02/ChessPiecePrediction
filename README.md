# Chess Piece Prediction
## Creating new conda environment
![alt text](datasets/artifacts/data_preparation/train/images/0b4ba28f0c759a11750a6430649b52e3_jpg.rf.711771a2d93077f33a4e16b6cd6df047.jpg)
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

## Change the config.yaml, dvc.yaml, params.yaml as well as the data.yaml files for the yolo dataset

## Then run the dvc.yaml file 

```bash
dvc init
dvc repro
```