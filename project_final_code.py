import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ["chicago", "new york city", "washington"]

    months = ["january", "february", "march", "april", "may", "june", "all"]

    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]


    while True:
        city = input("Would you like to see data for chicago, new york city or washington?\n").lower()
        print(city)
        if city in cities:
            break
        else:
            print("Invalid input. Please select chicago, new york or washington.")

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Would you like to see data for the months january, february, march, april, may, june or all?\n").lower()
        print(month)
        if month in months:
            break
        else:
            print("Invalid input. Please select all or january, february, march, april, may, june.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Would you like to see data for the weekdays monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n").lower()
        print(day)
        if day in days_of_week:
            break
        else:
            print("Invalid input. Please select all or monday, tuesday, wednesday, thursday, friday, saturday, sunday.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['days_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['days_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# TO DO: display the most common month
    if df['month'].to_string() !=month:
		popular_month = df['month'].mode()[0]
		print('Most common month:', popular_month)
	else:
		print('Most common month not available since you've selected a specific month.')

    # TO DO: display the most common day of week
    if df['days_of_week'].to_string() !=month:
		popular_weekday = df['days_of_week'].mode()[0]
		print('Most common day of week:', popular_weekday)
	else:
		print('Most common day not available since you've selected a specific day.')
	

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common hour of day:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['station_combination']= df['Start Station'] + ':' + df['End Station']
    popular_station_combination = df['station_combination'].mode()[0]
    print('Most commonly used combination of stations:', popular_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_travel_time = df['Trip Duration'].sum() / 60 / 60
    print('total travel time:', sum_travel_time, 'hours')


    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean() / 60
    print('average travel time:', avg_travel_time, 'minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print('Distribution of user types:', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
       gender_count = df['Gender'].value_counts().to_frame()
       print('Distribution of gender:', gender_count)
    else:
       print("No gender data to share.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent_birthyear = df['Birth Year'].max()
        print('Most recent birth year:', int(most_recent_birthyear))
        earliest_birthyear = df['Birth Year'].min()
        print('Earliest birth year:', int(earliest_birthyear))
        most_common_birthyear = df['Birth Year'].mode()[0]
        print('Most common birth year:', int(most_common_birthyear))
    else:
        print("No birth year data to share.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        raw = input("Would you like to see the first 5 rows of raw data? Type 'yes' or 'no'.\n").lower()
        pd.set_option('display.max_columns', 200)

        while True:
          if raw == 'no':
            break
          print(df[i:i+5])
          raw = input("Would you like to see the next 5 rows of raw data?\n").lower()
          i +=5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
