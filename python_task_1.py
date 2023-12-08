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
