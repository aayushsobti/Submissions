#Question 1
import pandas as pd
def calculate_distance_matrix(df) -> pd.DataFrame:
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    distance_matrix = df.pivot(index='id_1', columns='id_2', values='car')

    
    for id_value in distance_matrix.index:
        if id_value in distance_matrix.columns:
            distance_matrix.at[id_value, id_value] = 0

    return distance_matrix

import pandas as pd

import pandas as pd

# Question2
import pandas as pd

def calculate_distance_matrix(df) -> pd.DataFrame:
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    distance_matrix = df.pivot(index='id_1', columns='id_2', values='car')

    for id_value in distance_matrix.index:
        if id_value in distance_matrix.columns:
            distance_matrix.at[id_value, id_value] = 0

    return distance_matrix

def unroll_distance_matrix(df) -> pd.DataFrame:
    """
    Unroll a distance matrix to a DataFrame with columns 'id_start', 'id_end', and 'distance'.

    Args:
        df (pandas.DataFrame): Input distance matrix DataFrame.

    Returns:
        pd.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    unrolled_data = []

    for id_start in df.index:
        for id_end in df.columns:
            if id_start != id_end: 
                unrolled_data.append({
                    'id_start': id_start,
                    'id_end': id_end,
                    'distance': df.at[id_start, id_end]
                })

    unrolled_df = pd.DataFrame(unrolled_data)
    return unrolled_df

# Question 3
import pandas as pd

def find_ids_within_ten_percentage_threshold(df, reference_id) -> list:
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        list: Sorted list of IDs whose average distance is within the specified percentage threshold
              of the reference ID's average distance.
    """
    reference_avg_distance = df[df['id_start'] == reference_id]['distance'].mean()

    lower_threshold = reference_avg_distance * 0.9
    upper_threshold = reference_avg_distance * 1.1

    avg_distances = df.groupby('id_start')['distance'].mean()

    within_threshold = avg_distances[(avg_distances >= lower_threshold) & (avg_distances <= upper_threshold)]

    return within_threshold.sort_values().index.tolist()





# Question 4
def calculate_toll_rate(df) -> pd.DataFrame:
    """
    Calculates toll rates for different vehicle types based on the distance.

    Args:
        df (pandas.DataFrame): Input DataFrame with columns 'id_start', 'id_end', and 'distance'.

    Returns:
        pd.DataFrame: DataFrame with added columns for toll rates for each vehicle type.
    """
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle_type, coefficient in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * coefficient

    return df




# Question 5
import pandas as pd

def calculate_toll_rate(df) -> pd.DataFrame:
    """
    Calculates toll rates for different vehicle types based on the distance.

    Args:
        df (pandas.DataFrame): Input DataFrame with columns 'id_start', 'id_end', and 'distance'.

    Returns:
        pd.DataFrame: DataFrame with added columns for toll rates for each vehicle type.
    """
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle_type, coefficient in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * coefficient

    return df

