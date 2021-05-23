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
    print('Hello! Let\'s explore some US bikeshare data!\nWhich city data would you like to see? Chicago, New York City or Washington.')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
                city = input('ENTER THE CITY: ').lower()
                if city in cities:
                    print("Welcome to {} data".format(city).title())
                    break
                else:
                    print("Wrong Input!, Please choose one: chicago, new york city, washington".title())
                    continue


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
            month = input('Which month would you like to see? all, january, february, march, april, may, june (Choose one)\nENTER MONTH: ').lower()
            if month in months:
                    print("{} results loading".format(month).title())
                    break
            else:
                print("Wrong Input!, Please choose one: all, january, february, march, april, ...... , june".title())
                continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
            day = input("Finally, which date are you looking at? all, monday, tuesday, wednesday, thursday, friday, saturday, sunday (Choose one)\nENTER DAY : ").lower()
            if day in days:
                print("Welcome to {} report".format(month).title())
                break
            else:
                print("Wrong Input!, Please choose one:: all, monday, tuesday, wednesday, ...... , sunday".title())
                continue

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

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # new dataframe filter by month
        df = df[df['month'] == month]  # new dataframe filter by month

    # filter by day of the week
    if day != 'all':
        # new dataframe filter by day of the week
        df = df[df['day_of_week'] == day.title()] # new dataframe filter by day of the week


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    most_common_month = df['Start Time'].dt.month.mode()[0]
    most_common_day = df['Start Time'].dt.weekday_name.mode()[0]
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]


    # TO DO: display the most common month
    print("The most common month is {}".format(most_common_month))


    # TO DO: display the most common day of week
    print("The most common day of the week is {}".format(most_common_day))

    # TO DO: display the most common start hour
    print("The most common start hour is {}".format(most_common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    most_common_strt_station = df['Start Station'].mode()[0]
    most_common_end_station = df['End Station'].mode()[0]
    df['combination'] = df['Start Station'] + " to " +  df['End Station']
    most_frequent_comb = df['combination'].mode()[0]

    # TO DO: display most commonly used start station
    print("The most commonly used start station is {}".format(most_common_strt_station))

    # TO DO: display most commonly used end station
    print("The most commonly used end station is {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is \"{}\"".format(most_frequent_comb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()

    # TO DO: display total travel time
    print('The total travel time is {}'.format(total_travel_time))

    # TO DO: display mean travel time
    print('The mean travel time is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()


    # TO DO: Display counts of user types
    print("The number of user type counts is {}".format(user_types))

    try:
          # Display counts of gender
          gender_cnt = df['Gender'].value_counts()
          min_yob = df['Birth Year'].min()
          max_yob = df['Birth Year'].max()
          mode_yob = df['Birth Year'].mode()[0]
          print("\nThe total number of users by gender is {}".format(gender_cnt))


        # Display earliest, most recent, and most common year of birth
          print("\nThe result of the earliest, most recent and most common year of birth among users: \n")
          print(int(min_yob))
          print(int(max_yob))
          print(int(mode_yob))

    except KeyError:
          print("\nThere is no gender information in this city\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    """
    Provides option to see file's raw data, 5 lines at a time.
    User can choose between 'yes' or 'no' input.
    """
    index_from = 0
    index_to = 5
    while True:
        raw_data = input("Would you like to see some raw data?\nPlease type \'yes\' or \'no\': ").lower()
        if raw_data != 'no':
            print(df.iloc[index_from:index_to])
            index_from += 5
            index_to += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


    # descriptive commit message
