import os
import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def load_image(image_path):
    return cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

def scale_image(image, factor):
    height, width = image.shape[:2]
    return cv2.resize(image, (int(width * factor), int(height * factor)), interpolation=cv2.INTER_AREA)

def add_noise(image, intensity):
    noise = np.random.normal(0, intensity, image.shape).astype(np.int32)
    return np.clip(image + noise, 0, 255).astype(np.uint8)

def cluster_colors(image, new_colors):
    pixels = image.reshape((-1, 3)).astype(np.float32)
    clustering = KMeans(n_clusters = len(new_colors), random_state = 42)
    clustering.fit(pixels)
    labels = clustering.labels_
    new_colors = np.array([hex_to_rgb(color) for color in new_colors], dtype=np.uint8)
    return new_colors[labels.flatten()].reshape(image.shape)

def hex_to_rgb(color):
    color = color.lstrip('#')
    return [int(color[i:i+2], 16) for i in (0, 2, 4)]

def plot_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def save_image(image, image_path):
    file_name, file_extension = os.path.splitext(image_path)
    output_path = f"{file_name}_RV{file_extension}"
    cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    print(f"RV image saved as: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, help='Path to image.')
    parser.add_argument('--scale_factor', type=float, default=0.2, help='Factor used to downscale image.')
    parser.add_argument('--noise_intensity', type=int, default=20, help='Standard deviation of Gaussian noise.')
    parser.add_argument('--new_colors', type=str, default='#510F21,#6F2687,#000000', help='Comma-separated hex colors.')
    args = parser.parse_args()
    image = load_image(args.image_path)
    image = scale_image(image, args.scale_factor)
    image = add_noise(image, args.noise_intensity)
    image = cluster_colors(image, args.new_colors.split(','))
    image = scale_image(image, 1.0 / args.scale_factor)
    save_image(image, args.image_path)