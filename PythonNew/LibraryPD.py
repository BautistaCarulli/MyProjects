import pandas as pd

# Build a DataFrame with false info 
data = {'Nameofteam': ['Boca', 'Flamengo', 'Marsella', 'Roma'],
        'Partners': [1000000,10, 20,50, ],
        'Country': ['Argentina', 'Brasil', "Francia", 'Italia']}

df = pd.DataFrame(data)
print(df.head())
