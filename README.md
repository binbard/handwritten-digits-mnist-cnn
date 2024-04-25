# handwritten-digits-mnist-cnn-lstm
Creating a CNN Model for Digit Recognition based on MNIST Dataset and benchmarking it.

## Introduction
This project is to create a model of Convolutional Neural Network (CNN) for recognizing handwritten digits. The model is trained on the MNIST dataset and tested on the test set. The model is implemented using the Keras library in Python.

## Dataset
The dataset used in this project is the MNIST dataset. The MNIST dataset consists of 60,000 training images and 10,000 test images. Each image is a 28x28 pixel image of a handwritten digit.

## Development
#### -> Create a virtual environment

Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### -> Install the required libraries
```bash
pip install -r requirements.txt
```

#### -> Train the model (Optional)
```bash
python training/train_cnn.py
```

#### -> Run the interface
```bash
python main.py
```

## Interface
The interface is a simple GUI application that allows the user to draw a digit on the canvas and recognize it using the trained model. The interface is implemented using the Tkinter library in Python.

## Results
The model achieved an accuracy of 99.05% on the test set.