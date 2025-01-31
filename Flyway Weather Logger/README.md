# Flyway Weather Tracker
Those who know me, know that I am an avid outdoorsman, with waterfowl hunting being my drink of choice. Those that know me even better, know that I am a data nerd.

This of course leads to the conclusion that I _**need**_ to schedule a python script to help me track weather data for duck hunting.

### So what is the significance of weather data and duck hunting?
As most of us probably know, waterfowl are migratory birds. During the warmer months in North America, these waterfowl live in the far northern reaches of the United States, Canada, and even Russia; where they will raise their young. As the weather turns colder, these birds will prepare to migrate south to all areas of the United States, Mexico, and further south. There are several known and suspected triggers that tell waterfowl is time to migrate, many of those being related to the weather. These can be things such as temperature, wind direction, wind speed, barometric pressure, and even the moon phase.

Most hunters, myself included, watch the weather of territories to the north of them, but that can become cumbersome. Living as far south as I do, I have lots of weather to keep up with. That is what ultimately lead me to write this Flyway Weather Logging script.

### Python Modules used
- Datetime
- Pandas
- pytz
- openpyxl
- astral
- requests

### Data source
For weather data, I utilized the [open weather map API](https://openweathermap.org/api), as they offer a free use as long as you make less than 1,000 API calls per day.

For the lunar cycle data, I utilized a python package called [Astral](https://astral.readthedocs.io/en/latest/). This is also a good source for free lunar data.

### End product
Ultimately I used this data to create a an excel workbook, where I record relevant weather information for location in the central fly way.
![North American Flyway Map](https://www.onxmaps.com/wp-content/uploads/sites/15/2021/10/Artboard-1-100.jpg) "North American Flyway Map")

