

# Channel Manager Data Analysis with Streamlit and Plotly

This code analyzes the number of systems associated with each channel in a Red Hat Network (RHN) Satellite Server using the Satellite API. 

## Requirements

- Python 3.7+
- `requests` module
- `streamlit` module
- `pandas` module
- `plotly` module

## Installation

To install the required modules, run the following command:

```
pip install requests streamlit pandas plotly
```

## Usage

Before running this code, you should modify the `MANAGER_URL`, `MANAGER_LOGIN`, and `MANAGER_PASSWORD` variables to match your Satellite Server credentials.

After that, you can run the code with:

```
streamlit run <filename.py>
```

Once the app is running, you will see a table displaying the channel labels and the number of systems associated with each channel. Additionally, you will see a bar chart showing the number of systems per channel.

## Authors

- Created by: [Nisha]

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [Plotly](https://plotly.com/python/)
