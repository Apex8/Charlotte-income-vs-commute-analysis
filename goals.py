# Pull in API data from Charlotte api website on commuting block groups and income block groups
# Merge on GEOID10 
# from household income block groups keeping total households, merging smaller groups to 50k intervals( 0-50K, 50-100, 100-150, 150-200+), Median household income, total families, families in poverty.
# from commuting block groups keeping workers 16 or older, commuters drive alone, commuters carpool, commuters public transportation, commuters walked, commuters other means.
# Block group with largest number of commuters of each of the following categories and their median income statistic: Drive Alone, Carpool, Public Transport, Walked, Other means.
# Block with the largest number of households per each 50k (0-50, 50-100, 100-150, 150-200).
# Commuters per category and that average income for every block to determine most used transport per income bracket.

