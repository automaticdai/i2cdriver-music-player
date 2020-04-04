import time
from i2cdriver import I2CDriver
from supermario import notes, tempo, stop


def map_value(x, x1, x2, y1, y2):
    if x1 == x2 or y1 == y2:
        raise ValueError
    return (y2 - y1) / (x2 - x1) * (x - x1) + y1


if __name__ == '__main__':
    i2c = I2CDriver("/dev/ttyUSB0", True)

    for i in range(len(notes)):
        for j in range(len(notes[i])):
            # fetch the next note
            this_note = notes[i][j]
            print(this_note)

            if (this_note == 12):
                time.sleep(stop / 1000.0)
            else:
                # flash the LED
                # R, G, B
                intensity = map_value(this_note, 1, 127, 1, 256)

                fade = 10
                i2c.start(0x08, 0)
                i2c.write([0x00, intensity, intensity, intensity, fade])
                i2c.stop()

                # play the main buzzer
                i2c.start(0x30, 0)
                i2c.write([tempo, this_note])
                i2c.stop()

                # play the co buzzer
                i2c.start(0x31, 0)
                i2c.write([tempo, this_note])
                i2c.stop()

                # compensate time as iic communication introduces some delay
                time.sleep((tempo - 80) / 1000.0)
