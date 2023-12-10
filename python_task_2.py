#Question 1
import pandas as pd
from geopy.distance import geodesic

def calculate_distance_matrix(csv_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(csv_path)

    # Create an empty DataFrame for distance matrix
    num_locations = len(df)
    distance_matrix = pd.DataFrame(index=df['ID'], columns=df['ID'])

    # Calculate distances and fill in the matrix
    for i in range(num_locations):
        for j in range(i+1, num_locations):
            # Assuming the dataset has 'Latitude' and 'Longitude' columns
            coord_i = (df.at[i, 'Latitude'], df.at[i, 'Longitude'])
            coord_j = (df.at[j, 'Latitude'], df.at[j, 'Longitude'])

            # Calculate distance using geodesic
            distance_ij = geodesic(coord_i, coord_j).kilometers

            # Fill in the matrix symmetrically
            distance_matrix.at[df.at[i, 'ID'], df.at[j, 'ID']] = distance_ij
            distance_matrix.at[df.at[j, 'ID'], df.at[i, 'ID']] = distance_ij

    # Set diagonal values to 0
    distance_matrix.values[[range(num_locations)], [range(num_locations)]] = 0

    return distance_matrix

# Example usage:
csv_path = 'dataset-3.csv'
result_matrix = calculate_distance_matrix(csv_path)
print(result_matrix)

#Question 2
import pandas as pd

def unroll_distance_matrix(distance_matrix):
    # Create an empty DataFrame to store unrolled distances
    unrolled_distances = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])

    # Iterate over the rows of the distance_matrix
    for id_start, row in distance_matrix.iterrows():
        for id_end, distance in row.iteritems():
            # Exclude same id_start to id_end
            if id_start != id_end:
             
#Question 3
import pandas as pd

def find_ids_within_ten_percentage_threshold(unrolled_distances, reference_value):
    # Filter rows for the given reference_value
    reference_rows = unrolled_distances[unrolled_distances['id_start'] == reference_value]

    # Calculate the average distance for the reference_value
    average_distance = reference_rows['distance'].mean()

    # Calculate the threshold range (10% of the average distance)
    threshold_range = 0.1 * average_distance

    # Filter rows within the threshold range
    within_threshold = unrolled_distances[
        (unrolled_distances['distance'] >= (average_distance - threshold_range)) &
        (unrolled_distances['distance'] <= (average_distance + threshold_range))
    ]

    # Get unique values from the 'id_start' column and sort them
    result_ids = sorted(within_threshold['id_start'].unique())

    return result_ids

# Example usage:
# Assuming 'result_unrolled' is the DataFrame from the previous question and 'reference_value' is an integer
reference_value = 1  # Replace with the desired reference value
result_within_threshold = find_ids_within_ten_percentage_threshold(result_unrolled, reference_value)
print(result_within_threshold)

#Question 4
import pandas as pd

def calculate_toll_rate(unrolled_distances):
    # Define rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Create new columns for each vehicle type
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        unrolled_distances[vehicle_type] = unrolled_distances['distance'] * rate_coefficient

    return unrolled_distances

# Example usage:
# Assuming 'result_unrolled' is the DataFrame from the previous question
result_with_toll_rates = calculate_toll_rate(result_unrolled)
print(result_with_toll_rates)

