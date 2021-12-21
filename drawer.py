import json

import png
import requests


def main():
    endpoint = "https://4j10ejf71g.execute-api.us-east-1.amazonaws.com/mandel"

    xmin = -0.742030
    ymin = 0.125433
    xmax = -0.744030
    ymax = 0.127433

    xmin = -2.0
    ymin = -1.5
    xmax = 1.5
    ymax = 1.5

    size = 64
    step_size = 16
    max_iters = 256

    dx = (xmax - xmin) / step_size
    dy = (ymax - ymin) / step_size

    image_data = {}

    for ix in range(int(size / step_size)):
        for iy in range(int(size / step_size)):
            xmin_ = xmin + dx * ix
            ymin_ = ymin + dy * iy
            xmax_ = xmax + dx * (ix + 1)
            ymax_ = ymax + dy * (iy + 1)

            request = {
                "xmin": xmin_,
                "ymin": ymin_,
                "xmax": xmax_,
                "ymax": ymax_,
                "size": step_size,
                "max_iters": max_iters,
            }

            response = requests.post(endpoint, json=request)
            data = json.loads(response.content)
            image_data[(ix, iy)] = data.get("result")
            print(data.get("duration"))

    image_pixels = []
    for x in range(size):
        for y in range(size):
            block_ix = int(x / step_size)
            block_iy = int(y / step_size)
            ix = x % step_size
            iy = y % step_size
            pixel_index = ix + iy * step_size
            pixel = image_data[(block_ix, block_iy)][pixel_index]
            image_pixels.append(pixel)

    max_pixel = max(image_pixels)

    for i in range(size * size):
        image_pixels[i] = int(image_pixels[i] / max_pixel * 256)

    square_image = [image_pixels[i * size:(i + 1) * size] for i in range(size)]

    with open("mandel.ppm", "wt") as f:
        f.write("P2\n")
        f.write(f"{size} {size}\n")
        f.write("256\n")

        for k, v in enumerate(image_pixels):
            f.write(f"{v} ")
            if k % size == 0 and k > 0:
                f.write("\n")

    with open("mandel.png", "wb") as f:
        w = png.Writer(size, size, bitdepth=16)
        w.write(f, square_image)


if __name__ == "__main__":
    main()
