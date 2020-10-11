from sys import stdin
from math import ceil

if __name__ == '__main__':
    screen_width = 0  # screen width in pixels
    screen_height = 0  # screen height in pixels
    glass_width = 0   # glass width including walls
    glass_height = 0  # glass width including bottom
    water_units = 0  # number of water pixels

    for i, line in enumerate(stdin):
        line = line.strip()
        if len(line) == 0:
            continue
        screen_height += 1
        if i == 0:
            screen_width = len(line)
        if '#' in line:
            if glass_width == 0:
                glass_width = line.rfind('#') - line.find('#') + 1
            glass_height += 1
            water_units += line.count('*')

    water_level = ceil(water_units / screen_width)

    for i in range(screen_height):
        if i >= screen_height - water_level:
            # water
            print(''.ljust(screen_width, '*'))
        elif i == screen_height - 1:
            # right glass wall
            print(''.ljust(glass_height, '#').ljust(screen_width, '.'))
        elif i == screen_height - glass_width:
            # left glass wall
            print(''.ljust(glass_height, '#').ljust(screen_width, '.'))
        elif i > screen_height - glass_width:
            # glass bottom without water
            print('#'.ljust(screen_width, '.'))
        else:
            # empty space
            print(''.ljust(screen_width, '.'))
