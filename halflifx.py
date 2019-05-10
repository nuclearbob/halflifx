import time


def gradient(start, end, duration, steps, method):
    start_red = float(start[0])
    start_green = float(start[1])
    start_blue = float(start[2])
    start_k = float(start[3])
    end_red = float(end[0])
    end_green = float(end[1])
    end_blue = float(end[2])
    end_k = float(end[3])
    duration = float(duration)
    steps = int(steps)
    step_red = (end_red - start_red)/steps
    step_green = (end_green - start_green)/steps
    step_blue = (end_blue - start_blue)/steps
    step_k = (end_k - start_k)/steps
    red = start_red
    green = start_green
    blue = start_blue
    k = start_k
    wait = duration/steps
    for _ in range(steps):
        send_int_color([red, green, blue, k], method)
        red += step_red
        green += step_green
        blue += step_blue
        k += step_k
        time.sleep(wait)


def send_int_color(color, method):
    color = tuple(int(x) for x in color)
    method(color, rapid=True)
