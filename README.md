# Calculator of Messier Object sizes in pixels and percents of sensor size

### Example output

```
Showing data for Canon1200D with ED80
Sensor pitch is 4.30 horizontal and 4.31 vertical
Sensor / lens combination gives a FOV of 9200.98 x 6133.99 arcseconds
M101 will be 743 x 742 pixels, which is 14.35% x 21.52% of the sensor FOV
```

### Usage

1. Clone the project into your local machine, make sure you have Python3 installed (https://www.python.org/downloads/)
2. Add your camera and lens (telescope) information into the corresponding files, you can use the example values as templates. You can add more than one lens and sensor.
3. Run the script in the terminal: `python3 calc.py [sensor name] [lens name] [Messier object name]`
4. You can also add your own objects outside of the Messier catalogue.

### Example using the default provided values

`python3 calc.py Canon1200D ED80 M3`

### Further Reading

Calculator formulas: https://astrojolo.com/gears/pixel-scale-and-resolution/

Messier object data taken from http://www.messier.seds.org/m/mindex.html
