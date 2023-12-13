names = eval(input("Enter the player names: "))
times = eval(input("Enter the player times: "))

lap_times = map(lambda time_tuple: time_tuple[1] - time_tuple[0], times)
lap_times = list(lap_times)

final_dict = {}

for index in range(len(names)):
    final_dict[names[index]] = lap_times[index]

print(final_dict)
