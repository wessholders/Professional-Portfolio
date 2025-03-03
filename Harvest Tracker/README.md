# Harvest Tracker
This is a harvest tracker I use to track the waterfowl harvest of my group every year. It has various columns for tracking hunters, species, sex ratio of harvest, and other meteorlogical variables. It has a second sheet that provides a roll-up of relevant metrics. The below link includes some dummy rows to demonstrate how it functions. Feel free to make a copy and track your own harvest stats.

**Link to project:** [Harvest Tracker](https://docs.google.com/spreadsheets/d/1CZLxa8DK2NTA8w0svw1aet9t8DRr7mdFRAylNr3ZQXM/edit?usp=sharing)
![Alt text](/relative/path/to/img.jpg?raw=true "Optional Title")



## How It's Made:

**Tech used:** Google sheets

This is a strightforward process that anyone could replicate with success, I just find it useful so I included it here. As I mentioned earlier, this will track species harvested, the sex of the harvest, who the hunter was, and several meteorological variables such as temperature, wind speed/direction, cloud cover, lunar cycle, etc. I also include coordinates for my hunts and later create a heat map so I can determine what areas produced the most productive hunts.

The roll-up in the other sheet will track metrics including total birds by hunter, total hunts by hunter, skunks, and some averages among other things. Personally, the average harvest per hunt is my favorite aspect about this tracker because it reminds me of doing fisheries statistics in college. We track a metric called Catch per Unit of Effort (CPUE) that gives a standardized way of tracking success of a trip. In this case our "Catch" is the number of birds harvested and our "Unit of Effort" is number of hunts. The effort could be many units such as hours spent hunting, miles walked, _* number of mosquito bites recieved*_... You get the idea. In my group the person who has the highest CPUE at the end of the season has ultimate bragging rights until the next season.


## Optimizations
The real speed saver of this are the automatic calculations in the stats roll-up. All you need to do is add a name to the table and drag down the relevant equations and everything will automatically calculate.


## Lessons Learned:
I originally had the roll-up grouped by statistic, but changed it to be grouped by hunter. This allows for a better experience when sorting the metrics.


## Future work:
Ultimately I would love to incorportae this sort of data into an Esri Survey123 and use to build out a dashboard displaying geographical location, or building out a dataset in QGIS with this data.
