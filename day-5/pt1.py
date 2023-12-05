def convert(conversions, input) -> int:
    for conversion in conversions:
        if input >= conversion[0] and input < conversion[0] + conversion[2]:
            return conversion[1] + (input - conversion[0])
    return input


file = open('pt1.txt', 'r')
lines = file.readlines()
file.close()

seeds = lines.pop(0).split(':')[1].split()

curr_map_name = ''
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

for line in lines:
    line = line.strip()
    if line != '':
        if 'seed-to-soil' in line:
            curr_map = 'seed-to-soil'
        elif 'soil-to-fertilizer' in line:
            curr_map = 'soil-to-fertilizer'
        elif 'fertilizer-to-water' in line:
            curr_map = 'fertilizer-to-water'
        elif 'water-to-light' in line:
            curr_map = 'water-to-light'
        elif 'light-to-temperature' in line:
            curr_map = 'light-to-temperature'
        elif 'temperature-to-humidity' in line:
            curr_map = 'temperature-to-humidity'
        elif 'humidity-to-location' in line:
            curr_map = 'humidity-to-location'
        else:
            conversion = line.split()
            dest_start = int(conversion[0])
            source_start = int(conversion[1])
            range_len = int(conversion[2])

            if curr_map == 'seed-to-soil':
                seed_to_soil.append([source_start, dest_start, range_len])
            elif curr_map == 'soil-to-fertilizer':
                soil_to_fertilizer.append([source_start, dest_start, range_len])
            elif curr_map == 'fertilizer-to-water':
                fertilizer_to_water.append([source_start, dest_start, range_len])
            elif curr_map == 'water-to-light':
                water_to_light.append([source_start, dest_start, range_len])
            elif curr_map == 'light-to-temperature':
                light_to_temperature.append([source_start, dest_start, range_len])
            elif curr_map == 'temperature-to-humidity':
                temperature_to_humidity.append([source_start, dest_start, range_len])
            elif curr_map == 'humidity-to-location':
                humidity_to_location.append([source_start, dest_start, range_len])

closest = None

for seed in seeds:
    seed = int(seed)

    soil = convert(seed_to_soil, seed)
    fertilizer = convert(soil_to_fertilizer, soil)
    water = convert(fertilizer_to_water, fertilizer)
    light = convert(water_to_light, water)
    temperature = convert(light_to_temperature, light)
    humidity = convert(temperature_to_humidity, temperature)
    location = convert(humidity_to_location, humidity)

    if closest is None or location < closest:
        closest = location

print(closest)