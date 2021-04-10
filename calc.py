import argparse
import json
import sys


def calculate(sensor_name, lens_name, object_name):
    with open("sensors.json", "r") as sensor_file:
        file_contents = sensor_file.read()
        sensors = json.loads(file_contents)

    with open("lenses.json", "r") as lenses_file:
        file_contents = lenses_file.read()
        lenses = json.loads(file_contents)

    with open("objects.json", "r") as objects_file:
        file_contents = objects_file.read()
        objects = json.loads(file_contents)

    sensor = next(filter(lambda s: s["name"] == sensor_name, sensors), None)
    if not sensor:
        print("Could not find provided sensor in the sensors file!")
        exit()
    lens = next(filter(lambda s: s["name"] == lens_name, lenses), None)
    if not lens:
        print("Could not find provided lens in the lenses file!")
        exit()
    messier_object = next(filter(lambda s: s["name"] == object_name, objects), None)
    if not messier_object:
        print("Could not find provided Messier object in the objects file!")
        exit()

    # first calculate pixel pitch, the physical size of the pixel
    # we need to convert it to um (micrometers) for later

    pixel_pitch_x = (sensor["sizeX"] / sensor["resolutionX"]) * 1000
    pixel_pitch_y = (sensor["sizeY"] / sensor["resolutionY"]) * 1000

    # second calculate image scale
    # scale is arcseconds per pixel for our particular sensor / lens combination

    scale_x = 206.3 * pixel_pitch_x / lens["focalLength"]
    scale_y = 206.3 * pixel_pitch_y / lens["focalLength"]

    # third calculate how many arcseconds will fit into our sensor

    field_x = scale_x * sensor["resolutionX"]

    field_y = scale_x * sensor["resolutionY"]

    # now let's take a Messier Object and convert its dimensions to arcseconds

    messier_object_x = float(messier_object["dim_x"]) * 60
    messier_object_y = float(messier_object["dim_y"]) * 60

    object_size_x_in_pixels = int(messier_object_x / scale_x)
    object_size_y_in_pixels = int(messier_object_y / scale_y)

    object_size_x_on_sensor = (messier_object_x / field_x) * 100
    object_size_y_on_sensor = (messier_object_y / field_y) * 100

    # summary

    print(f"Showing data for {sensor['name']} with {lens['name']}")

    print(
        f"Sensor pitch is {pixel_pitch_x:.2f} horizontal and {pixel_pitch_y:.2f} vertical"
    )

    print(
        f"Sensor / lens combination gives a FOV of {field_x:.2f} x {field_y:.2f} arcseconds"
    )

    print(
        f"{messier_object['name']} will be {object_size_x_in_pixels} x {object_size_y_in_pixels} pixels, which is {object_size_x_on_sensor:.2f}% x {object_size_y_on_sensor:.2f}% of the sensor FOV"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate Messier Objects size on a sensor/lens combination"
    )
    parser.add_argument("sensor", help="sensor")
    parser.add_argument("lens", help="lens")
    parser.add_argument("object", help="Messier object")
    args = parser.parse_args()

    calculate(args.sensor, args.lens, args.object)
