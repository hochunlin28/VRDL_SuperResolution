# VRDL_hw4
## Install Packages

* install pytorch from https://pytorch.org/get-started/previous-versions/

* install packages
```
pip install

```

## Data Preparation
* I use matlab to run the data/generate_train.m. Therefore, it will generate train.h5 dataset. Please put it in data/ directory.

## Training
* I use VDSR to run this homework.
```
python main_vdsr.py --cuda --gpus 0 --nEpochs 30 --lr 0.01
```

## download pretrainted model
* After we train, it will produce .pth file in checkpoint/. Please put .pth file in checkpoint/ directory. [download pretrainted model](https://drive.google.com/file/d/1TLKZehRFBav7pvuUL6kSLTtFzxGIqd3t/view?usp=sharing)
* Before executing inference.py, I convert the low resolution testing image as three times bigger than these and save in test/ directory. (e.g 100 * 100 -> 300 * 300)
* I do this for you, so just goto inference part

```
python resize_image.py
```

## Inference
* It will generate high resolution image in result/ directory.
```
python inference.py --model checkpoint/model_final.pth --scale 3
```
## Submission
* I get PSNR 27.5318 in this project.
