#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\arjun\Desktop\infolimpioavanzadoTarget.csv\infolimpioavanzadoTarget.csv")
df


# In[5]:


selected_col= ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume','ticker']
drop_col=[]
for col in df.columns:
    if col not in selected_col:
        drop_col.append(col)
df.drop(columns=drop_col, inplace=True)
print(drop_col)


# In[6]:


df
import pandas as pd


unique_tickers = df['ticker'].value_counts()

print("Unique tickers and their counts:\n", unique_tickers)

num_unique_tickers = len(unique_tickers)

print("\nNumber of unique tickers:", num_unique_tickers)


# In[7]:


import pandas as pd


unique_tickers = df['ticker'].value_counts()

print("Unique tickers and their counts:\n", unique_tickers)

num_unique_tickers = len(unique_tickers)

print("\nNumber of unique tickers:", num_unique_tickers)


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

asle_data = df[df['ticker'] == 'ASLE']
asle_data = asle_data.set_index('date') 
asle_data['close'].plot()

plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('ASLE Close Price')

plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt


tickers_to_plot = ['ASLE', 'ASUR', 'ATLCP', 'ATLCL', 'ATLC', 'ATIF', 'ATHX', 'ATHE', 'ATHA', 'ATEX',
                   'ATER', 'ATEC', 'ATCOL', 'ATAI', 'ASYS', 'ASTS', 'ASLN', 'ASTR', 'ASTL', 'ASTE',
                   'ASTC', 'ASRV', 'ASRT', 'ASPS', 'ASPAU', 'ASPA', 'ASO', 'ASND', 'ASML', 'ASMB', 'ATLO']


fig, axs = plt.subplots(6, 6, figsize=(20, 15))


axs = axs.flatten()

for i, ticker in enumerate(tickers_to_plot):
    if i < len(axs):
        ticker_data = df[df['ticker'] == ticker]
        if not ticker_data.empty:
            ticker_data = ticker_data.set_index('date')
            
            axs[i].plot(ticker_data['close'])
            axs[i].set_xlabel('Date')
            axs[i].set_ylabel('Close Price')
            axs[i].set_title(f'{ticker} Close Price')
            axs[i].grid(True)
        else:
            fig.delaxes(axs[i])
    else:
        break

plt.tight_layout()
plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

tickers_to_plot = ['ASLE', 'ASUR', 'ATLCP', 'ATLCL', 'ATLC', 'ATIF', 'ATHX', 'ATHE', 'ATHA', 'ATEX',
                   'ATER', 'ATEC', 'ATCOL', 'ATAI', 'ASYS', 'ASTS', 'ASLN', 'ASTR', 'ASTL', 'ASTE',
                   'ASTC', 'ASRV', 'ASRT', 'ASPS', 'ASPAU', 'ASPA', 'ASO', 'ASND', 'ASML', 'ASMB', 'ATLO']

ticker_sets = [tickers_to_plot[i:i+11] for i in range(0, len(tickers_to_plot), 11)]


for i, ticker_set in enumerate(ticker_sets):
    fig, ax = plt.subplots(figsize=(15, 7))

    for ticker in ticker_set:
        ticker_data = df[df['ticker'] == ticker]
        ticker_data = ticker_data.set_index('date')  
        ax.plot(ticker_data['open'], label=ticker)  

    ax.set_ylabel('Stock Prices')
    ax.set_title(f'Open Prices for Tickers {i*10+1} to {i*10+11}')
    ax.legend()
    plt.tight_layout()
    plt.show()


# In[12]:


fig, ax = plt.subplots(figsize=(15, 7))

for ticker in tickers_to_plot:
    ticker_data = df[df['ticker'] == ticker]
    ticker_data = ticker_data.set_index('date')
    ax.plot(ticker_data['volume'], label=ticker)

ax.set_ylabel('Volume Traded')
ax.set_title('Volume for All Tickers')
plt.legend()
plt.show()



# In[19]:


num_rows = 6
num_cols = int(len(tickers_to_plot) / num_rows) + 1
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 25))
axes = axes.flatten()

for i, ticker in enumerate(tickers_to_plot):
    ticker_data = df[df['ticker'] == ticker]
    ticker_data = ticker_data.set_index('date') 
    ticker_data['volume'].plot(ax=axes[i])

    axes[i].set_ylabel('Volume Traded')
    axes[i].set_title(f'Volume for {ticker}')


for j in range(len(tickers_to_plot), num_rows * num_cols):
    fig.delaxes(axes[j])


plt.tight_layout()
plt.show()


# In[40]:


import pandas as pd
import matplotlib.pyplot as plt


tickers_to_plot = ['ASLE', 'ASUR', 'ATLCP', 'ATLCL', 'ATLC', 'ATIF', 'ATHX', 'ATHE', 'ATHA', 'ATEX',
                   'ATER', 'ATEC', 'ATCOL', 'ATAI', 'ASYS', 'ASTS', 'ASLN', 'ASTR', 'ASTL', 'ASTE',
                   'ASTC', 'ASRV', 'ASRT', 'ASPS', 'ASPAU', 'ASPA', 'ASO', 'ASND', 'ASML', 'ASMB', 'ATLO']


num_rows = int(len(tickers_to_plot) / 6) + 1


fig, axes = plt.subplots(num_rows, 6, figsize=(20, 15)) 
axes = axes.flatten() 

for i, ticker in enumerate(tickers_to_plot):
    ticker_data = df[df['ticker'] == ticker]
    if not ticker_data.empty:
        axes[i].boxplot(ticker_data['close'])
        axes[i].set_ylabel('Close Price')
        axes[i].set_title(f'{ticker}\'s Close Price')

for j in range(len(tickers_to_plot), num_rows * 6):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

tickers_to_plot = ['ASLE', 'ASUR', 'ATLCP', 'ATLCL', 'ATLC', 'ATIF', 'ATHX', 'ATHE', 'ATHA', 'ATEX',
                   'ATER', 'ATEC', 'ATCOL', 'ATAI', 'ASYS', 'ASTS', 'ASLN', 'ASTR', 'ASTL', 'ASTE',
                   'ASTC', 'ASRV', 'ASRT', 'ASPS', 'ASPAU', 'ASPA', 'ASO', 'ASND', 'ASML', 'ASMB', 'ATLO']

num_rows = int(len(tickers_to_plot) / 6) + 1

for i, ticker in enumerate(tickers_to_plot):
    company_data = df[df['ticker'] == ticker]
    if not company_data.empty:
        plt.figure(figsize=(6, 6))
        pd.plotting.scatter_matrix(company_data, alpha=0.3)  
        plt.suptitle(f'Pairwise Scatter Plot of {ticker}')
        plt.show()


# In[ ]:


df


# In[ ]:




