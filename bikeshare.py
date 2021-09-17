import time
import pandas as pd
import numpy as np

#dictinay of data sets
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
    
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input('Which you like to see data for chicago, new york city or washington?\n').lower().strip()
        if city not in CITY_DATA.keys():
            print('Please, Enter city name correctly.\n')
            continue
        else:
            break
    
    
    filter_list=['month','day','both','none']
    # ask for filter type
    while True:
        filter_type=input('Would you like to filter data by month, day, both or not at all? Type "none" for no time filter.\n').lower().strip()
        if filter_type not in filter_list:
            print('Please, Enter filter type correctly.\n')
            continue
        else:
            break
    
    # Check List of months
    month='all'
    month_check_list = ['january', 'february', 'march', 'april', 'may', 'june','all']
    # Check List of days
    day='all'
    day_check_list = ['monday','tuesday','wednesday', 'thursday', 'friday', 'saturday','sunday','all']
    
    # filter by month only
    if filter_type.lower() == 'month':
        # TO DO: get user input for month
        while True:
            month = input('Enter the Month/all if you search in all monthes.\n').lower().strip()
            if month not in month_check_list:
                print('Please, Enter month correctly.\n')
                continue
            else:
                break
            
    # filter by day only 
    elif filter_type.lower() == 'day':
        # TO DO: get user input for day 
        while True:
            day = input('Enter the Day name/all if you search in all days.\n').lower().strip()
            if day not in day_check_list:
                print('Please, Enter day correctly.\n')
                continue
            else:
                break
    
    # filter by both 
    elif filter_type.lower() == 'both':
        # TO DO: get user input for both
        while True:
            month = input('Enter the Month/all if you search in all monthes.\n').lower().strip()
            if month not in month_check_list:
                print('Please, Enter month name correctly.\n')
                continue
            else:
                break
                
        while True:
            day = input('Enter the Day name/all if you search in all days.\n').lower().strip()
            if day not in day_check_list:
                print('Please, Enter day name correctly.\n')
                continue
            else:
                break

    print('-'*40)
    return city, month, day


def load_data(city, month, day ):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #read data from csv in dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # user to datetime to tranform start time column to date type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # add three colums month, weekday_name and hour using Start Time column
    df['month'] = df['Start Time'].dt.month
    df['weekday_name'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month= months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day
    if day != 'all':
        df = df[df['weekday_name'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most Frequent Month:',months[df['month'].mode()[0]-1].title(),'..Count: ',df['month'][df['month'] == df['month'].mode()[0]].count())

    # display the most common day of week
    print('Most Frequent Day:',df['weekday_name'].mode()[0],'..Count: ',df['weekday_name'][df['weekday_name'] == df['weekday_name'].mode()[0]].count())

    # display the most common start hour
    print('Most Frequent Hour:',df['hour'].mode()[0],'..Count: ',df['hour'][df['hour'] == df['hour'].mode()[0]].count())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most Frequent start station:',df['Start Station'].mode()[0],'..Count: ',df['Start Station'].groupby(df['Start Station']).count().max())

    #display most commonly used end station
    print('Most Frequent End station:',df['End Station'].mode()[0],'..Count: ',df['End Station'].groupby(df['End Station']).count().max())
    
    # display most frequent combination of start station and end station trip
    df['Start Station & End Station']=df['Start Station']+' -> '+df['End Station']
    print('Most Frequent combination of start station and end station:',df['Start Station & End Station'].mode()[0],'..Count: ',df['Start Station & End Station'].groupby(df['Start Station & End Station']).count().max())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ',df['Trip Duration'].sum()/(3600),'Hours')

    # display mean travel time
    print('Average travel time: ',df['Trip Duration'].mean()/(60),'Minutes')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types: \n',df['User Type'].value_counts(),'\n')

    # Display counts of gender
    print('Counts of gender types: \n',df['Gender'].value_counts(),'\n')

    # Display earliest, most recent, and most common year of birth
    print('Most common year of birth:',int(df['Birth Year'].mode()),'..Count: ',df['Birth Year'].value_counts().max())
    print('Most recent year of birth:',int(df['Birth Year'].max()))
    print('Most earliest year of birth:',int(df['Birth Year'].min()))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_rows(df):
    '''Display 5 rows'''
    '''
    input: data Frame Object
    output: print the rows needed    
    '''
    # take response from user
    res = input('To view the first 5 rows in avalibale data please enter ["yes","no"].\n').lower().strip()
    if res == 'yes':
        x=5
        # print first 5 rows
        print(df.head())
        while True:
            # take response from user
            res2 = input('To view more 5 rows in avalibale data please enter ["yes","no"].\n').lower().strip()
            if res2 == 'yes'and x+5 <= df.count()[0]:
                print(df[x:x+5])
                x+=5
            else:
                print('End Veiw.')
                break
                
    
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        # washington dont have user columns
        if city != 'washington':
            user_stats(df)
        
        view_rows(df)
        
        restart_list=['yes','no']
        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n').strip()
            if restart in restart_list:
                break
        
        
        if restart.lower() == 'no':
                break

if __name__ == "__main__":
	main()