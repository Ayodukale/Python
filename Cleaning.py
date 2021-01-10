# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
# Used .describe() to print the summary statistics of the user_type column from ride_sharing.
print(ride_sharing['user_type'].describe())

# Strip duration of minutes
#Used the .strip() method to strip duration of "minutes" and stored it in the duration_trim column.
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Converted duration to integer and stored it in the duration_time column
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Wrote an assert statement that checks if duration_time's data type changed to int
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())

# Convert tire_sizes from a category data type to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27 using .loc[]
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to a categorical data type from int
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

# Convert ride_date to a datetime object and stored it in ride_dt using to_datetime()
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())

# Find duplicated rows of ride_id in the ride_sharing DataFrame while setting keep to False.
duplicates = ride_sharing.duplicated(subset = ['ride_id'], keep = False)

# Subset ride_sharing on duplicates and sort by ride_id and assign the results to duplicated_rides.
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])

# Dropped complete duplicates in ride_sharing and store the results in ride_dup.
ride_dup = ride_sharing.drop_duplicates()

# Created statistics dictionary which holds minimum aggregation for user_birth_year and mean aggregation for duration.
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Drop incomplete duplicates by grouping by ride_id and applying the aggregation in statistics.
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Found duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0