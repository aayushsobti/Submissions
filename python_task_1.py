# Question 1
import pandas as pd
df=pd.read_excel(r'C:/Users/DEEPIKA/OneDrive/Desktop/MapUp-Data-Assessment-F-main/MapUp-Data-Assessment-F-main/datasets/dataset-1.csv')
def generate_car_matrix(df) -> pd.DataFrame:
    """
    Creates a DataFrame for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    matrix_df = df.pivot(index='id_1', columns='id_2', values='car')
    
   
    for id_value in matrix_df.index:
        matrix_df.at[id_value, id_value] = 0
    
    return matrix_df
print(generate_car_matrix(df))

#Question 2
import numpy as np

def get_type_count(df) -> dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame): DataFrame with a 'car' column containing numeric values.

    Returns:
        dict: A dictionary with car types as keys ('low', 'medium', 'high') and their counts as values.
    """
    def categorize(value):
        if value <= 15:
            return 'low'
        elif 15 < value <= 25:
            return 'medium'
        else:
            return 'high'
    
    df['car_type'] = df['car'].apply(categorize)

    type_counts = df['car_type'].value_counts().to_dict()

    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts


#Question 3
def get_bus_indexes(df) -> list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    mean_bus = df['bus'].mean()
    threshold = 2 * mean_bus

    indexes = df.index[df['bus'] > threshold].tolist()

    indexes.sort()

    return indexes

#Question 4
def filter_routes(df) -> list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    route_means = df.groupby('route')['truck'].mean()

    filtered_routes = route_means[route_means > 7].index.tolist()

    filtered_routes.sort()

    return filtered_routes

# Question 5
def multiply_matrix(matrix) -> pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
   
    def multiply_condition(value):
        if value > 10:
            return value * 2
        else:
            return value * 3

    return matrix.applymap(multiply_condition)

# Question 6
def time_check(df) -> pd.Series:
    """
    Verifies if each unique (id, id_2) pair in the dataset has complete time data covering a full 24-hour 
    period for each day of the week.

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: Boolean series indicating if each (id, id_2) pair has incomplete time data.
    """
    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    def covers_full_day(group):
        return group['start'].dt.time.min() == pd.Timestamp('00:00:00').time() and \
               group['end'].dt.time.max() == pd.Timestamp('23:59:59').time()

    def covers_full_week(group):
        return set(group['start'].dt.day_name()) == set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    result = df.groupby(['id', 'id_2']).apply(lambda x: not (covers_full_day(x) and covers_full_week(x)))

    return result


