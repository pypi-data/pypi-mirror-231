# cognite-ai

A set of AI tools for working with CDF in Python. 

## Smart data frames
Chat with your data using LLMs. Built on top of [PandasAI](https://docs.pandas-ai.com/en/latest/) If you have loaded data into a Pandas dataframe, you can run

Install the package
```
%pip install cognite-ai
```

Chat with your data
```
from cognite.ai import load_smartdataframe
SmartDataframe = await load_smartdataframe()
import pandas as pd

df = pd.read_csv('workorders.csv')

from cognite.client import CogniteClient
client = CogniteClient()

s_df = SmartDataframe(df, cognite_client=client)
s_df.chat('Which 5 work orders are the longest?')
```
