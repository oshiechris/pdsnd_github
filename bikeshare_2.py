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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

@@ -1 6,6 +1 6,1 0 @@ weekdays =
('sunday', 'monday', 'tuesday',
'wednesday', 'thursday', 'friday', def
choice(prompt, choices=('y', 'n')):
"""Return a valid input from the
user given an array of possible
answers.
+
Args:
+ (str) prompt - prompt with input
request
+ (tup) choices - tuple with
elements of possible answers """ $
git diff diff
--git a/README.md b/README.md
index 1 3a6e85..bb56def 1 00644 ---
a/README.md
+++ b/README.md @@ -5,6 +5,1 8
@@ ### Description This is a CLI
program developed to allow the
user to explore bikeshare system
database in three different states in
the US and retrieve statistics
information from the database. The
user is able to filter the information
by city, month and weekday, in
order to visualize statistics
information related to a specific
git push origin master
subset of data.
+#### Getting Started
+ +This program is structured in 2
steps.
+ +In a first moment, the user
selects the filters that are going to
be applied to the database. The
user is able to chose as many filters
as it would like.
+ +After this step, the DataFrame
for the analysis is created based on
the filters chosen by the user.
+ +In a second moment, the user is
able to chose, from a list of options,
the statistics the user would like to
calculate, based on the available
filtered data.
+ +As of April 2, 201 9 the user is
now able to chose to view raw data
and also able sort this data by
columns, in ascending or
descending order
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
