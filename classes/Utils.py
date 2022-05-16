import statistics, matplotlib.pyplot as plt, seaborn as sns, os, gspread
import statistics

class Utils:
   def __init__(self):
      pass

   def avg(self, li):
      return sum(li)/len(li)

   def median(self, li):
      return round(statistics.median(li), 2)
   