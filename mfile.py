def determine_weather_conditions(t, h):
    w=0
    w = 0.5 * t**2 - 0.2 * h - 0.1 * w - 15
    if w > 300:
        conditions = "Sunny"
    elif 200 < w <= 300:
        conditions = "Cloudy"
    elif 100 < w <= 200:
        conditions = "Rainy"
    else:
        conditions = "Stormy"

    return conditions
try:
    with open("values1.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            temperature = float(lines[i].strip())
            humidity = float(lines[i + 1].strip())
            result = determine_weather_conditions(temperature, humidity)
            print(f"Weather conditions for Set {i//2 + 1}: {result}")

except FileNotFoundError:
    print("File not found. Make sure the file 'values1.txt' exists.")
except ValueError:
    print("Invalid data in the file. Make sure the file contains valid numerical values for temperature and humidity.")
except Exception as e:
    print(f"An error occurred: {e}")
