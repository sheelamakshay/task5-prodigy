import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Traffic Accident Dataset
np.random.seed(42)

# Generating random data for demonstration
num_accidents = 1000

accident_data = {
    'Date': pd.date_range(start='2022-01-01', periods=num_accidents, freq='D'),
    'Time': pd.to_datetime(np.random.choice(pd.date_range('00:00', '23:59', freq='15T'), num_accidents)),
    'Road_Condition': np.random.choice(['Dry', 'Wet', 'Snow', 'Ice'], num_accidents),
    'Weather': np.random.choice(['Clear', 'Rain', 'Snow'], num_accidents),
    'Latitude': np.random.uniform(35.0, 40.0, num_accidents),
    'Longitude': np.random.uniform(-120.0, -75.0, num_accidents),
    'Severity': np.random.choice(['Minor', 'Moderate', 'Major'], num_accidents)
}

accident_df = pd.DataFrame(accident_data)

# Analyze patterns
# Road Condition vs. Accident Count
plt.figure(figsize=(10, 6))
sns.countplot(x='Road_Condition', data=accident_df, palette='viridis')
plt.title('Accident Count by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Accident Count')
plt.show()

# Weather vs. Accident Count
plt.figure(figsize=(10, 6))
sns.countplot(x='Weather', data=accident_df, palette='viridis')
plt.title('Accident Count by Weather')
plt.xlabel('Weather')
plt.ylabel('Accident Count')
plt.show()

# Time of Day vs. Accident Count
accident_df['Time_Hour'] = accident_df['Time'].dt.hour
plt.figure(figsize=(10, 6))
sns.countplot(x='Time_Hour', data=accident_df, palette='viridis')
plt.title('Accident Count by Time of Day')
plt.xlabel('Time of Day (Hour)')
plt.ylabel('Accident Count')
plt.show()

# Visualize accident hotspots on the map
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Longitude', y='Latitude', hue='Severity', data=accident_df, palette='viridis', s=50)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
