import random
import pandas as pd

ex_data = pd.read_excel(r"D:\project_1\Book1.xlsx")

mailList = ex_data["mail_ids"].values.tolist()
totalParticipants = len(mailList)
winner = random.randint(0,totalParticipants)
print("wi nner is:",mailList[winner])