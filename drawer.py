import json
from multiprocessing import Pool

import requests

ENDPOINT = "https://4j10ejf71g.execute-api.us-east-1.amazonaws.com/mandel"


def remote_mandel(request):
    response = requests.post(ENDPOINT, json=request)
    data = json.loads(response.content)
    ix = request["ix"]
    iy = request["iy"]
    print(f"[{ix:>3}, {iy:>3}]: {data['duration']:>4.2f}")
    return {(ix, iy): data.get("result")}


def write_ppm(filename, size, data):
    with open(filename, "wt") as f:
        f.write("P2\n")
        f.write(f"{size} {size}\n")
        f.write("256\n")

        for k, v in enumerate(data):
            f.write(f"{v} ")
            if k % size == 0 and k > 0:
                f.write("\n")


def main():
    xmin = -0.742030
    ymin = 0.125433
    xmax = -0.744030
    ymax = 0.127433

    n_threads = 64

    size = 1024
    step_size = 32
    max_iters = 1024

    dx = (xmax - xmin) / (size // step_size)
    dy = (ymax - ymin) / (size // step_size)

    request_chunks = []

    for ix in range(int(size / step_size)):
        for iy in range(int(size / step_size)):
            xmin_ = xmin + dx * ix
            ymin_ = ymin + dy * iy
            xmax_ = xmin + dx * (ix + 1)
            ymax_ = ymin + dy * (iy + 1)

            request = {
                "ix": ix,
                "iy": iy,
                "xmin": xmin_,
                "ymin": ymin_,
                "xmax": xmax_,
                "ymax": ymax_,
                "size": step_size,
                "max_iters": max_iters,
            }
            request_chunks.append(request)

    image_data = {}
    with Pool(n_threads) as p:
        for r in p.map(remote_mandel, request_chunks):
            k, v = next(iter(r.items()))
            image_data[k] = v

    image_pixels = []
    for x in range(size):
        for y in range(size):
            block_ix = int(x / step_size)
            block_iy = int(y / step_size)
            ix = x % step_size
            iy = y % step_size
            pixel_index = ix + iy * step_size
            pixel = image_data[(block_iy, block_ix)][pixel_index]
            image_pixels.append(pixel)

    max_pixel = max(image_pixels)

    for i in range(size * size):
        image_pixels[i] = int(image_pixels[i] / max_pixel * 256)

    write_ppm("mandel.ppm", size, image_pixels)


if __name__ == "__main__":
    main()
