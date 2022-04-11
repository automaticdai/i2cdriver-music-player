# I2CDriver Music Player

This project plays simply music notes using buzzers and the I2CDriver from ExCamera Labs. It supports play two tracks simultaneously. 

![](iicdriver-music.png)

Current supported songs:

- `music/supermario.py`: Super Mario Bro. theme song
- `music/march_of_steel_torrent.py`: March of Steel Torrent (Chinese name: 钢铁洪流进行曲)

You can find demo video from: 
- YouTube: https://youtu.be/3MocEkK7n_Y
- Bilibili: https://www.bilibili.com/video/BV1uE411u7Ju

To switch the songs, change the first few lines in the `main.py`. You can extent this code by adding more songs using a separate python script in the `/music` folder.

The buzzers extension board is from: https://electricdollarstore.com, which has a on-board microncontroller with I2C interface.

The I2CDriver is a usb-to-I2C bridge and debugger from ExCamera Labs (https://i2cdriver.com/).

## How to use

Connect the hardware and then run the following command:`$ python3 main.py`


## Notes on I2CDriver

To speedup the I2CDriver, use `setserial` to change the USB port speed:

```
$ sudo setserial /dev/ttyUSB0 low_latency
```

This sets the USB latency to its minimal (1 ms) and can increase the speed of two-way communication by up to 10x.


## Limitation
The two tracks are not totally separated and independent, as they can only use same tempos. Hence the second track is only ideal for playing chords.


## License
MIT License
