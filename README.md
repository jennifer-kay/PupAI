# Image Classifier

This repository contains an image classification project using pre-trained deep learning models from PyTorch. The project leverages models like ResNet, AlexNet, and VGG to classify images into categories based on the ImageNet dataset.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Models Supported](#models-supported)
- [Results](#results)
- [Files](#files)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Introduction

This project demonstrates how to use pre-trained models for image classification tasks. The models are trained on the ImageNet dataset, which consists of over 1,000 classes, including various dog breeds, animals, objects, and more. The classifier can predict the label of a given image using one of the pre-trained models.

## Installation

### Prerequisites

- Python 3.x
- PyTorch
- torchvision
- Pillow

### Steps

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/img-classifier.git
    cd img-classifier
    ```

2. Install the required Python packages:
    ```bash
    pip install torch torchvision pillow
    ```

3. Ensure you have the ImageNet class labels file in JSON format:
    ```bash
    wget https://raw.githubusercontent.com/pytorch/hub/master/imagenet_class_index.json
    ```

## Usage

To classify an image, you can use the `classifier.py` script provided in the repository. The script allows you to choose between different models (ResNet, AlexNet, VGG) to classify your images.

### Command-Line Usage

```bash
python classifier.py --image_path path/to/your/image.jpg --model_name resnet
```

### Parameters

- `image_path`: The file path to the image you want to classify.
- `model_name`: The name of the pre-trained model to use (`resnet`, `alexnet`, `vgg`).

### Example

```bash
python classifier.py --image_path examples/dog.jpg --model_name vgg
```

The script will output the predicted label for the image.

## Models Supported

The following models are supported:

- **ResNet**: ResNet50 pre-trained on ImageNet.
- **AlexNet**: AlexNet pre-trained on ImageNet.
- **VGG**: VGG16 pre-trained on ImageNet.

These models are loaded with their respective pre-trained weights and are used for image classification tasks.

## Results

Below are example results obtained using the models:

### VGG16

- **Accuracy**: 87.5%
- **Correct Dog Breeds**: 93.3%
- **Correct Non-Dog Classification**: 100%

### AlexNet

- **Accuracy**: 75.0%
- **Correct Dog Breeds**: 80.0%
- **Correct Non-Dog Classification**: 100%

### ResNet50

- **Accuracy**: 82.5%
- **Correct Dog Breeds**: 90.0%
- **Correct Non-Dog Classification**: 90.0%

**Note**: The accuracy and classification results can vary depending on the dataset used.

## Files

- `classifier.py`: The main script for classifying images using pre-trained models.
- `imagenet_class_index.json`: A JSON file containing the mapping of class indices to human-readable labels.
- `README.md`: This file providing an overview of the project.
- `examples/`: A directory containing example images to test the classifier.

## Acknowledgments

This project uses pre-trained models provided by [PyTorch](https://pytorch.org/). The models are trained on the ImageNet dataset, which is widely used in the deep learning community for benchmarking.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this `README.md` to better fit your specific project needs!
