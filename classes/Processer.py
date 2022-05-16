import matplotlib.pyplot as plt, seaborn as sns, pandas as pd, gspread, os
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from classes.Utils import Utils

load_dotenv()

class Processer:
   def __init__(self):
      self.client_email = os.getenv('CLIENT_EMAIL')
      self.scope = [os.getenv('FEEDS'), os.getenv('DRIVE')]
      self.sheet_name = os.getenv('SHEET_NAME')
      self.credentials = ServiceAccountCredentials.from_json_keyfile_name('../secret/keys.json', self.scope)
      self.series = None
   
   def connection(self):
      client = gspread.authorize(self.credentials)

      sheet = client.open(self.sheet_name)
      sheet_instance = sheet.get_worksheet(0)
      series = sheet_instance.get_all_records()

      self.series = series

   def make_df(self):
      return pd.DataFrame.from_dict(self.series)

   def plot(self, serie, name):
      utils = Utils()

      plt.figure(figsize=(15, 6))

      # movements
      plt.subplot(1, 2, 1)
      sns.set_theme(style="darkgrid")
      sns.color_palette('pastel')
      plt.title(f"Movements for the 1st Cross - {name}")
      x = [i for i in range(1, 21)]
      sns.lineplot(x=x, y=serie)
      sns.lineplot(x=x, y=[7 for _ in range(1, 21)], color='red', linestyle="dashed")

      # statistics
      plt.subplot(1, 2, 2)
      legend = ['min', 'avg', 'med', 'max']
      stats = {
         "min": min(serie),
         "avg": utils.avg(serie),
         "med": utils.median(serie),
         "max": max(serie)
      }
      plt.bar(x=legend, height=list(stats.values()))
      plt.title(f"Statistics for {name}")

      plt.show()

   def make_pdf(self):
      pass