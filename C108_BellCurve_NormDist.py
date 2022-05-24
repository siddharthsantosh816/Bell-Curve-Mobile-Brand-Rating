from turtle import pd
import plotly.figure_factory as ff
import pandas as pd

Rating_file=pd.read_csv('C:/Users/w/Desktop/Python/csv/Amazon_mobile.csv')
Rating=Rating_file['Avg Rating'].tolist()
Brand=Rating_file['Mobile Brand'].tolist()
fig=ff.create_distplot([Rating],['Amazon Brand Rating Distribution Curve'],show_hist=False)
fig.show() 
