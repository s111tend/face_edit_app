import io
import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def get_img_bits(image):
    """
    Converts PIL Image it to bits
    """
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    return bio.getvalue()


def plot_image(image, title=None):
    """
    Displays an image using matplotlib
    """
    plt.figure(figsize=(8,8))
    if title is not None:
        plt.title(title)
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    
def load_numpy(path, device):
    """
    Loads numpy array and converts it to torch tensor
    """
    # load from path
    data = np.load(path, allow_pickle=True)
    # convert to torch tensor and pass to device
    data = torch.from_numpy(data).to(device)
    return data


def convert_image(image, size):
    """
    Converts generated image to a displayable format
    @param image: a generated image of shape [N, H, W] in range [-1, 1]
    @return: postprocessed image in shape [H, W, N] in range [0, 255] (dtype=uint8)
    """
    # change the order of channels
    image = image.permute(1, 2, 0)
    # renormalize
    image = (image + 1) * 127.5
    # convert to NumPy
    image = image.cpu().numpy()
    # convert to PIL
    image = Image.fromarray(image.astype(np.uint8))
    # resize to a desired size
    image = image.resize(size)
    return image