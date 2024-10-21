def uweather(t, h):
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
temperature = float(input("Enter temperature (t): "))
humidity = float(input("Enter humidity (h): "))
result = uweather(temperature, humidity)
print("Weather conditions:", result)
