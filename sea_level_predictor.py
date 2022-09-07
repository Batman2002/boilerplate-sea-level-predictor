import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")
    plt.rcParams["figure.figsize"] = (20,10)
    fig,ax=plt.subplots()
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    res=linregress(x,y)
    ax.scatter(x,y)
    # x_fit=np.linspace(df['Year'].min(),2050,1)
    x_fit=list(range(1880,2051))
    y_fit=[]
    for j in x_fit:
      y_fit.append(j*res.slope + res.intercept)
    # y_fit=x_fit*res.slope + res.intercept
    ax.plot(x_fit,y_fit)
    a=df.loc[df['Year']>=2000]
    x2=a['Year']
    y2=a['CSIRO Adjusted Sea Level']
    res2=linregress(x2,y2)
    x_fit2=list(range(2000,2051))
    y_fit2=[]
    for i in x_fit2:
      y_fit2.append(i*res2.slope + res2.intercept)
    ax.plot(x_fit2,y_fit2)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
# x_fit2
    # Create scatter plot


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()