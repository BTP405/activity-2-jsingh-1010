# Define the statistics_decorator function
def statistics_decorator(func):
    # Define the wrapper function inside the decorator
    def wrapper(numbers):
        # Calculate statistics
        count = len(numbers)
        total = sum(numbers)
        average = total / count if count > 0 else 0
        maximum = max(numbers) if numbers else None
        
        # Print statistics
        print("Numbers:", numbers)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maximum)
    
    return wrapper

# Apply the statistics_decorator to calculate_statistics function
@statistics_decorator
def calculate_statistics(numbers):
    pass

# Define a function to read the file and calculate statistics
def printStats(t):
    # Open the file
    with open(file_path, 'r') as file:
        # Read each line
        for line in file:
            # Convert line to list of floats
            numbers = [float(num) for num in line.strip().split()]
            # Calculate statistics for each line
            calculate_statistics(numbers)

# Main function to execute the program
if __name__ == "__main__":
    # File path
    file_path = "t.txt"  # Update with the path to your file
    # Process the file and calculate statistics
    printStats(file_path)
