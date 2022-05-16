import matplotlib.pyplot as plt, seaborn as sns, pandas as pd, statistics, gspread, os
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()

client_email = os.getenv('CLIENT_EMAIL')
scope = [os.getenv('FEEDS'), os.getenv('DRIVE')]
creds = ServiceAccountCredentials.from_json_keyfile_name('./keys.json', scope)
client = gspread.authorize(creds)

sheet = client.open(os.getenv('SHEET_NAME'))
sheet_instance = sheet.get_worksheet(0)
series = sheet_instance.get_all_records()

df = pd.DataFrame.from_dict(series)

# print(df.head())

def avg(li):
   return sum(li)/len(li)

def median(li):
   return round(statistics.median(li), 2)

def plot(serie, name):
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
      "avg": avg(serie),
      "med": median(serie),
      "max": max(serie)
   }
   plt.bar(x=legend, height=list(stats.values()))
   plt.title(f"Statistics for {name}")

   plt.show()

for col in df:
   plot(df[col], col)