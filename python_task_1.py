import pandas as pd

def generate_car_matrix():
    # Read the dataset-1.csv file into a DataFrame
    df = pd.read_csv('dataset-1.csv')

    # Pivot the DataFrame to create a matrix using id_1 as index, id_2 as columns, and car as values
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')

    # Fill NaN values with 0 (for cells with no corresponding car value)
    car_matrix = car_matrix.fillna(0)

    # Set diagonal values to 0
    car_matrix.values[[range(len(car_matrix))]*2] = 0

    return car_matrix

# Example usage:
result_matrix = generate_car_matrix()
print(result_matrix)

#Question 2
import pandas as pd

def get_type_count(df):
    # Add a new categorical column 'car_type' based on values of the column 'car'
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    # Calculate the count of occurrences for each 'car_type' category
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts

# Example usage:
# Assuming df is your DataFrame loaded from dataset-1.csv
# df = pd.read_csv('dataset-1.csv')

result = get_type_count(df)
print(result)

#question 3
import pandas as pd

def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    mean_bus_value = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean value
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

# Example usage:
# Assuming df is your DataFrame loaded from dataset-1.csv
# df = pd.read_csv('dataset-1.csv')

result = get_bus_indexes(df)
print(result)

#Question 4
import pandas as pd

def filter_routes(df):
    # Group by 'route' and calculate the average of the 'truck' column for each route
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' values is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    selected_routes.sort()

    return selected_routes

result = filter_routes(df)
print(result)

#question 5
def multiply_matrix(input_matrix):
    # Create a deep copy of the input matrix to avoid modifying the original DataFrame
    modified_matrix = input_matrix.copy()

    # Apply the specified logic to modify values
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix


modified_result = multiply_matrix(result_matrix)
print(modified_result)
 
 #Question 6
 import pandas as pd

def verify_timestamps_completeness(df):
    # Combine 'startDay' and 'startTime' columns to create a datetime column 'start_timestamp'
    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])

    # Combine 'endDay' and 'endTime' columns to create a datetime column 'end_timestamp'
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    # Calculate the duration for each row
    df['duration'] = df['end_timestamp'] - df['start_timestamp']

    # Define the expected full 24-hour duration
    full_24_hours = pd.Timedelta(days=1)

    # Group by (id, id_2) and check if each pair covers a full 24-hour period and spans all 7 days
    completeness_check = df.groupby(['id', 'id_2']).apply(lambda group: (
        group['duration'].sum() >= full_24_hours * 7 and
        group['start_timestamp'].dt.hour.min() == 0 and
        group['end_timestamp'].dt.hour.max() == 23
    )).droplevel(level=[0, 1])

    return completeness_check

# Example usage:
# Assuming df is your DataFrame loaded from dataset-2.csv
# df = pd.read_csv('dataset-2.csv')

result = verify_timestamps_completeness(df)
print(result)



