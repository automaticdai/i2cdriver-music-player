#!/usr/bin/python3

import time
from i2cdriver import I2CDriver
#from music.supermario import *
from music.march_of_steel_torrent import *

# speed up / slow down the music by a factor; default value is 1.0
speedup_factor = 1.0


def map_value(x, x1, x2, y1, y2):
    if x1 == x2 or y1 == y2 or x < x1 or x > x2:
        raise ValueError
    return (y2 - y1) / (x2 - x1) * (x - x1) + y1


if __name__ == '__main__':
    # create a new I2CDriver object
    i2c = I2CDriver("/dev/ttyUSB0", True)
    i2c.setspeed(400)

    for i in range(len(notes)):
        for j in range(len(notes[i])):
            # fetch the next note
            this_note = notes[i][j]

            if tracks == 2:
                this_note_c = notes_c[i][j]

            this_tempo = int(tempo[i][j] / speedup_factor)

            print((this_note, this_tempo))

            if (this_note < 55 or this_note > 127):
                time.sleep(this_tempo / 1000.0)
            else:
                # flash the LED
                intensity = int(map_value(this_note, 55, 127, 1, 256))
                fade = 10
                i2c.start(0x08, 0)
                # [0x00, R, G, B, fade]
                i2c.write([0x00, intensity, intensity, intensity, fade])
                i2c.stop()

                #this_tempo = this_tempo - 1;

                while this_tempo > 0:
                    # play the main buzzer
                    i2c.start(0x30, 0)
                    i2c.write([this_tempo % 256, this_note])
                    i2c.stop()

                    # play the co buzzer
                    if tracks == 2:
                        i2c.start(0x31, 0)
                        i2c.write([this_tempo % 256, this_note_c])
                        i2c.stop()

                    this_delay = this_tempo % 256
                    this_tempo = this_tempo - 256

                    # compensate time as iic communication introduces some delay
                    time.sleep(max((this_delay - 10), 1) / 1000.0)

                # end of a note
                time.sleep(10 / 1000.0)

        # end of a section
        time.sleep(20 / 1000.0)
