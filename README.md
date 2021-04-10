# Calculator of Messier Object sizes in pixels and percents of sensor size

### Example output

```
Showing data for Canon1200D with Vixen144
Sensor pitch is 4.30 horizontal and 4.31 vertical
Sensor / lens combination gives a FOV of 7667.48 x 5111.66 arcseconds
M3 will be 730 x 728 pixels, which will be 14.09% x 21.13% of the provided sensor size
```

### Usage

1. Clone the project into your local machine, make sure you have Python3 installed
2. Add your camera and lens (telescope) information into the corresponding files, you can use the example values as templates. You can add more than one lens and sensor.
3. Run the script in the terminal: `python3 calc.py [sensor name] [lens name] [Messier object name]`
4. You can also add your own objects outside of the Messier catalogue.

### Example using the default provided values

`python3 calc.py Canon1200D ED80 M3`

### Further Reading

Calculator formulas: https://astrojolo.com/gears/pixel-scale-and-resolution/

Messier object data taken from http://www.messier.seds.org/m/mindex.html
