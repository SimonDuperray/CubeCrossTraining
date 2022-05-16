from classes.Utils import Utils
from classes.Processer import Processer

processer = Processer()
processer.connection()

df = processer.make_df()

for col in df:
   processer.plot(df[col], col)
