import datetime
from astral.sun import sun
from astral import LocationInfo

# set location
city = astral.LocationInfo("Charlotte", "USA", "US/Eastern")

# set start and end dates
start_date = datetime.date.today()
end_date = start_date + datetime.timedelta(days=30)

# loop through each day and calculate times
for day in range((end_date - start_date).days + 1):
    current_date = start_date + datetime.timedelta(days=day)
    s = sun(city.observer, date=current_date)
    print(f"Date: {current_date}")
    print(f"Sunrise: {s['sunrise']}")
    print(f"Sunset: {s['sunset']}")
    print(f"Dusk: {s['dusk']}")
    print(f"Dawn: {s['dawn']}")
    print("----------------------------")