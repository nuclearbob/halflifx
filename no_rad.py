import sys
import vlc

from lifxlan import LifxLAN

from halflifx import gradient


lan = LifxLAN()
file = sys.argv[1]
start = [0, 65535, 0, 5500]
end = [0, 65535, 32767, 5500]
steps = 300
player = vlc.MediaPlayer(file)
lan.set_color_all_lights(start)
player.play()
while player.get_position() < 1:
    pass
gradient(start, end, 10, 100, lan.set_color_all_lights)
