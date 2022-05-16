# Rubik's Cube Tracker

## Personal need
By learning Fridrich method to solve the 3x3 Rubik's Cube, I also try to solve the white cross with a maximum of 7 movements. So, I train myself by doing 20 repetitions series until the white cross. Once this done, I rearrange the cube and I restart. To have a progressive training, I enter all my data into a Google Sheet file. But, to have a better idea on my progression, I needed to easily access to some indicators on one side: 

```
- minimum number of movements
- mean number of movements
- median number of movements
- maximum number of movements
```

And on the other side, a graph plotting my number of movements for each repetition.

## Process
For each serie, I enter my results in a new column on my Google Sheet file. This file is linked to a Python script using a Google Cloud Platform. This allows me to make dynamic analysis of my results using a simple Python script.

I transform the json returned object to a pandas DataFrame, to make it easier to manipulate. I built a parameterized function, which take a single serie in parameter and which will return one figure composed of two graphs:

```
- Lineplot
- Barplot
```

## Future upgrades
I will create PDF files with a clean presentation allowing me to easily observe the trend of my progression.