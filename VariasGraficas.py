# I'll write a Python program that reads the financial data from a CSV and plots line charts for Alphabet Inc.
import matplotlib.pyplot as plt
import Excerscie  as np
import pandas as pd
import matplotlib.dates as mdates


Open = np.array([774.25, 776.030029, 779.309998, 779, 779.659973])
High = np.array([776.065002, 778.710022, 782.070007, 780.47998, 779.659973])
Low = np.array([769.5, 772.890015, 775.650024, 775.539978, 770.75])
Close = np.array([772.559998, 776.429993, 776.469971, 776.859985, 775.080017])
Date = np.array(['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16'])


# Plot the financial data
plt.figure(figsize=(10, 6))
plt.plot(Open, label="Open")
plt.plot(Low, label="High")
plt.plot(High, label="Low") 
plt.plot(Close, label="Close")

# Convertir los datos en un DataFrame de pandas
df = pd.DataFrame(Date)

# Convertir la columna 'Date' al formato de fecha
df[Date] = pd.to_datetime(df[Date])

ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d\n%b\n%Y'))  # Mostrar día, mes, año en el formato que quieres
ax.xaxis.set_major_locator(mdates.DayLocator())  # Usar cada día como un tic


# Add title and labels
plt.title("Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
