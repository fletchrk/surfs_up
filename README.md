# surfs_up

## Project Overview
W. Avy, an investor, wants to see more information regarding the temperature trends before he will support opening a surf and ice cream shop in Oahu. W. Avy is interested in knowing the temperature data specifically for the months of June and December to ensure that the business would be sustainable all year long.

## Resources
Data Sources: Surfsup_Challenge.ipynb, hawaii.sqlite, June_temps.png, Dec_temps.png

## Results
The average temperature in June is 75 degrees, which occurred at least 50% during the month. The maximum temperature in June was 85 degrees, while the minimum temperature in June was 64 degrees. At least 75% of the month the temperature was 77 degrees.

### June Statistics for Temperature in Oahu, Hawaii

![June_temps](https://github.com/fletchrk/surfs_up/blob/main/Resources/June_temps.png)

### Plot for June Statistics in Oahu, Hawaii

![June_temps_plot](https://github.com/fletchrk/surfs_up/blob/main/Resources/June_temps_plot.png)

The average temperature in December is 71 degrees, which occurred at least 50% during the month. The maximum temperature in December was 83 degrees while the minimum temperature was 56 degrees. At least 75% of the month the temperature was 74 degrees.

### December Statistics for Temperature in Oahu, Hawaii

![Dec_temps](https://github.com/fletchrk/surfs_up/blob/main/Resources/Dec_temps.png)

### Plot for December Statistics in Oahu, Hawaii

![Dec_temps_plot](https://github.com/fletchrk/surfs_up/blob/main/Resources/Dec_temps_plot.png)

## Summary
The analysis that was performed to determine the temperatures for June and December in Oahu, Hawaii was done in 4 steps. Step 1 was a query was written that filters the date column for the measurement table to retrieve all the temperatures for June. Step 2 was to convert June temperatures to a list while Step 3 was to create a DataFrame from the list of temperatures that was created in Step 2. The final step was to generate a summary of statistics for the June temperatures DataFrame. After the table was confirmed to be correct all four steps were created and ran for the month of December. 

After reviewing the statistics in June and December, I recommend that W. Avy invests in the surf and ice cream shop in Oahu, Hawaii. One recommendation is to run statistics for a couple more months to determine what the weather patterns are like for Oahu, Hawaii. A second recommendation is to run statistics on how many days in June and December is it raining versus just doing the temperature.

