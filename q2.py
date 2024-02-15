import matplotlib.pyplot as plt

def graphSnowfall(t):
""" 
Create a bar graph that displays the snowfall data distribution.
Arguments: t (str): The filename containing the snowfall data.
Input: None Output: None 
"""
    with open(t, "r") as file:
        # Read snowfall data from the file, then remove numbers that are not integers.
        snowfall_data = [int(line.strip()) for line in file if line.strip().isdigit()]

# Establish upper and lower bounds for the ranges of snowfall.
    max_snowfall = max(snowfall_data)
    upper_limit = max_snowfall + 10 - max_snowfall % 10
    lower_limit = 0
    # Determine the size and number of intervals.
    num_intervals = upper_limit // 10
    interval_size = 10
    # Create a list at the beginning to record snowfall events for each interval.  
    snowfall_occurrences = [0] * num_intervals
    # Determine how much snow fell for each interval.
    for snowfall in snowfall_data:
        value = snowfall - 1 if snowfall - 1 >= 0 else 0
        index = min(value // 10, num_intervals - 1)
        snowfall_occurrences[index] += 1
    # Create labels for every interval of snowfall.
    interval_labels = [f'{start+1 if start > 0 else start}-{start + interval_size}cms'
                       for start in range(lower_limit, upper_limit, interval_size)
                       if start + interval_size <= upper_limit]
    # Draw a bar graph.
    plt.bar(interval_labels, snowfall_occurrences)
    plt.xlabel('Snowfall Ranges (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Bar Graph')
    plt.show()

# Example usage
graphSnowfall('t.txt')
