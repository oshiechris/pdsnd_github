Data: US Bikeshare Data (https://www.motivateco.com/use-our-data/)

Story: Comparing the system usage between three large cities: New York City, Chicago, and Washington, DC. What kinds of information would we want to know about in order to make smarter business decisions? If we were a user of the bike-share service, what factors might influence how we would want to use the service?

Investigation: Any differences within each system by those users that are registered, regular users VS short-term, casual users? It is possible that users who are subscribed to a bike-share system will have different patterns of use compared to users who only have temporary passes.

(Any other relationships? Where do bikers ride? When do they ride? How far do they go? Which stations are most popular? What days of the week are most rides taken on? Where are the most commonly used docks? What are the most common routes? Weather has potential to have a large impact on daily ridership? How much is ridership impacted when there is rain or snow? Are subscribers or customers affected more by changes in weather?)

|Data Wrangling|
package: csv, datetime, pprint

func: datetime.date(), csv.DictReader(), csv.DictWriter(), .next(), .list(), .whiteheader(), .whiterow(), .strftime(%A), .replace(':','')

issue: We obtain 3 csv files, but (a)The size of each dataset is too huge to get to the intuitive exploration.(b)There are inconsistencies. Each file has a different way of delivering its data. Even where the information is the same, the column names and formats are sometimes different (Chicago updates with new data twice a year, Washington DC is quarterly, and New York City is monthly).

approach: (a)Using DictReader object, starting off by looking at one row from each of the dataset.(b)Making sure that the data formats across the cities are consistent, and trimming focusing only on the parts of the data we are most interested in - 1)trip duration, 2)starting month, 3)starting hour, 4)day of the week, and 5)user type.

columns to extract from :

Duration: Given to us in seconds (New York, Chicago) or milliseconds (Washington). Need to be given in terms of minutes.
Month, Hour, Day of Week: Ridership volume is likely to change based on the season, time of day, and whether it is a weekday or weekend. We use the start time of the trip to obtain these values. The New York City data includes the seconds in their timestamps, while Washington and Chicago do not.
User Type: Washington divides its users into two types: 'Registered'(annual, monthly) and 'Casual'(24-hour, 3-day, other short-term passes). The New York and Chicago data uses 'Subscriber' and 'Customer' for these groups, respectively. For consistency, we convert the Washington labels to match the other two. There are some missing 'user-type' values in the New York city dataset. Since we don't have enough information to fill these values in, we leave them as-is.
[CODE]

Planning_01.(Data Collecting): Define a function that prints the name of the city and returns(extracts) the 'first data point'(second row) from the large csv files (DictReader object) that includes a 'header row'. It prints the city names and the first data point to check now so that the first trip is parsed in the form of a dictionary. And it also returns those values to use when we create a 'dictionary-nesting dictionary' later on....which is important because it's a provided data file to iterate through later.

DictReader object: When we set up a DictReader object, the first row of the data file is normally interpreted as column names. Every other row in the data file will use those column names as keys, as a dictionary is generated for each row.
next(): Return the next row of the reader’s iterable object as a list
pprint():
def print_first_point(filename):
    city = filename.split('-')[2].split('/')[-1]
    print('\nCity: {}'.format(city))
    
    with open(filename, 'r') as f_in:
        trip_reader = csv.DictReader(f_in) 
        first_trip = next(trip_reader) 
        pprint(first_trip)
    return (city, first_trip)

#testing------------------------------------------------------------------------------------------------------------
data_files = ['C:/Users/Minkun/Desktop/classes_1/NanoDeg/1.Data_AN/L2/bike-share-analysis/data/NYC-CitiBike-2016.csv',
              'C:/Users/Minkun/Desktop/classes_1/NanoDeg/1.Data_AN/L2/bike-share-analysis/data/Chicago-Divvy-2016.csv',
              'C:/Users/Minkun/Desktop/classes_1/NanoDeg/1.Data_AN/L2/bike-share-analysis/data/Washington-CapitalBikeshare-2016.csv',]

example_trips = {} ###there we go!###
for i in data_files:
    ct, ftrip = print_first_point(i)
    example_trips[ct] = ftrip 

example_trips['NYC']['tripduration']
example_trips['Washington']['user_type']
example_trips['Chicago']['starttime']


