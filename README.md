# Retro Vision

Script to apply a retro pixel art style to images.

### Usage:
```bash
python main.py [image_path] [--scale_factor SCALE] [--noise_intensity INTENSITY] [--new_colors COLORS]
```

### Arguments:
- ```[image_path]```: Path to the image to which the retro style will be applied.
- ```[--scale_factor SCALE]```: Factor used to downscale the image, a smaller value results in a more pixelated effect.
- ```[--noise_intensity INTENSITY]```: Standard deviation of gaussian generated noise, a larger value results in more noise.
- ```[--new_colors COLORS]```: A comma-separated list of hex color codes that specify the palette to apply to the image.

## Demonstration

```bash
python main.py ucl.png --scale_factor 0.2 --noise_intensity 20 --new_colors #510F21,#6F2687,#000000
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/fe91c9e3-e31d-462d-836e-c8e63e298b68" alt="ucl" width="45%" />
  <img src="https://github.com/user-attachments/assets/e96084e2-06e7-4814-be55-9366e7610ff2" alt="ucl_RV" width="45%" />
</p>
