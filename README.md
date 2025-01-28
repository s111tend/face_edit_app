# Face Edit App

## Description
This is an application in which you can create an image using style-based generative NN or project your own image. You can then use this application to edit various facial parameters in the image such as age, degree of smile, etc.

Used papers:
- [A Style-Based Generator Architecture for Generative Adversarial Networks](https://arxiv.org/abs/1812.04948)
- [Unsupervised Discovery of Interpretable Directions in the GAN Latent Space](https://arxiv.org/abs/2002.03754)

## Installation
Firstly, you need to install libraries from `requirements.txt` file:

```
pip install -r requirements.txt
```

Note, that `dlib` package needs installed [CMake](https://cmake.org/) on your computer.

The next step will be downloading the model and it's weights using the following commands:
```
git clone https://github.com/NVlabs/stylegan2-ada-pytorch.git
cd models
wget https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/ffhq.pkl
cd ..
```

To edit faces you will need to download learned vectors for the model. Archived vectors are in `vectors` folder. You just need to unzip `stylegan2directions.zip`.

The final step is to download the landmark detection model. Since the generator is trained on the [FFHQ](https://www.kaggle.com/datasets/arnaud58/flickrfaceshq-dataset-ffhq) dataset, our own images should be aligned to be as similar as possible to the training data. To load the model, run the following commands:

```
cd models
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
bzip2 -dv shape_predictor_68_face_landmarks.dat.bz2
cd ..
```

That's all. Now you can run the application.

## Running App
To run the application, you need to launch `run.py` file:

```
python run.py
```