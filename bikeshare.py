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
    print('\n Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
       city=input("\n Please choose a city (chicago, new york city, washington) to start exploring its data : \n").strip().lower()
       if city in CITY_DATA:
            break
       else:
            print("\n that’s not a valid input, please stick to the mentioned cities\n")


    # get user input for month 0, 1, 2, ... , 6)
    while True:
        month=int(input("\n would you like your data to be filtered by month, if so choose an integer from 1 to 6, eg: january = 1, if not type 0 : \n"))
        if month in [0,1,2,3,4,5,6]:
            break
        else:
            print("\n please make sure to enter an integer from the specified range\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("\n would you like your data to be filtered by day, if so type name of the day if not type 'all': \n").strip().lower()
        if day in ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']:
            break
        else:
            print("\n please make sure to enter a valid day name\n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 0 to apply no month filter
        (str) day - name of the day of week to filter by, or 0 to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data into the dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert start time column into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract the month and day_of_week coulumns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #filter by month
    if month != 0:
        df = df[df['month'] == month]
    #filter by day
    if day != "all" :
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()[0]
    print("most popular month:",common_month)

    # display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('most common day:',common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most Popular Start Hour:", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_sstation = df['Start Station'].mode()[0]
    print('most commonly used start station:',most_sstation)

    # display most commonly used end station
    most_estation = df['End Station'].mode()[0]
    print('most commonly used end station:',most_estation)

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station']+'>>>>>'+df['End Station']
    most_trip = df['trip'].mode()[0]
    print('the most popular trip from start to end:',most_trip)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel=round((df['Trip Duration'].sum() / 3600))
    print('total travel time is {} hours '.format(total_travel))


    # display mean travel time
    avg_travel = round((df['Trip Duration'].mean() / 60))
    print('average travel time per trip is {} minutes'.format(avg_travel))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    gender_type = df['Gender'].value_counts()
    print(gender_type)

    # Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    recent = int(df['Birth Year'].max())
    common_y = int(df['Birth Year'].mode()[0])
    print('\n earliest year of birth is {}\n most recent year of birth is {}\n most common year of birth is {}\n'.format(earliest,recent,common_y))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        n = 0
        m=5
        while input('\nWould you like to see 5 rows of your data ? Enter yes or no.\n').lower() == 'yes':
            print(df.iloc[n:m, :])
            n=m
            m+=5
        else:
            break


if __name__ == "__main__":
	main()
