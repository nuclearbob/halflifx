import sys
import vlc

from lifxlan import LifxLAN

from halflifx import gradient


def up_and_down(cycles, length, start, end, steps, method):
    duration = float(cycles)*2/float(length)
    for _ in range(cycles):
        gradient(start, end, duration, steps, method)
        gradient(end, start, duration, steps, method)


def once(lan, file, start, end, steps):
    player = vlc.MediaPlayer(file)
    player.play()
    while player.get_length() == 0:
        pass
    length = player.get_length()
    up_and_down(1, float(length) / 1000, start, end, steps,
                lan.set_color_all_lights)


lan = LifxLAN()
file = sys.argv[1]
start = [0, 65535, 0, 5500]
end = [0, 65535, 65535, 5500]
steps = 300
while True:
    once(lan, file, start, end, steps)
