import matplotlib.pyplot as plt

def graphSnowfall(t):
    with open(t, "r") as file:
        snowfall_data = [int(line.strip()) for line in file if line.strip().isdigit()]

    max_snowfall = max(snowfall_data)
    upper_limit = max_snowfall + 10 - max_snowfall % 10
    lower_limit = 0
    num_intervals = upper_limit // 10
    interval_size = 10
    
    snowfall_occurrences = [0] * num_intervals
    for snowfall in snowfall_data:
        value = snowfall - 1 if snowfall - 1 >= 0 else 0
        index = min(value // 10, num_intervals - 1)
        snowfall_occurrences[index] += 1
        
    interval_labels = [f'{start+1 if start > 0 else start}-{start + interval_size}cms'
                       for start in range(lower_limit, upper_limit, interval_size)
                       if start + interval_size <= upper_limit]
    
    plt.bar(interval_labels, snowfall_occurrences)
    plt.xlabel('Snowfall Ranges (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Bar Graph')
    plt.show()

graphSnowfall('t.txt')
