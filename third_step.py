from IPython.display import display
import pandas as pd
data = {'Name': ["John", "Anna", "Peter", "Linda"],
        'Location': ["New York", "Paris", "Berlin", "london"],
        'Age': [24, 13, 53, 33]
        }
data_pandas = pd.DataFrame(data)
display(data_pandas[data_pandas.Age > 30])