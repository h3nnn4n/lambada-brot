# Lambada-brot

Uses aws lambda to parallelize and scale drawing the mandelbrot set. This is
mostly an experiment and doesn't do much. In order to make this "viable" (i.e.
better than just running it locally), it would need some kind of "load
balancer" to pick the right chunk sizes. If the image chunks are too small, we
spent a lot of time doing networking and too little doing actual computations.
If the chunk size is too big, we risk timing out the lambda function.

# LICENSE

[MIT](LICENSE)
