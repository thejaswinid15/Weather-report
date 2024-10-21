def fileweather(t, h):
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
    with open("values.txt", "r") as file:
        temperature = float(file.readline().strip())
        humidity = float(file.readline().strip())
    result = fileweather(temperature, humidity)
    print("Weather conditions:", result)

except FileNotFoundError:
    print("File not found. Make sure the file 'values.txt' exists.")
except ValueError:
    print("Invalid data in the file. Make sure the file contains valid numerical values for temperature and humidity.")
except Exception as e:
    print(f"An error occurred: {e}")
