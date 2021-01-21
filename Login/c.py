
import os

import pandas as pd
import matplotlib.pyplot as plt
#from batsmen import *
#from wicketkeeping import *
#from bowlers import *
#from allrounders import *
#from datacleaning import *




#graphs for batsman
from pro1310 import *

def graph_batsmen():
    batsmen_name=list(batsmen.NAME)

    mra_listforplot=[]
    avg_listforplot=[]
    stk_listforplot=[]
    brpi_listforplot=[]
    or_listforplot=[]
    
    for i in batsmen_name:
        mra_listforplot.append(float(batsmen[batsmen.NAME==i].MRA_Rating))
        avg_listforplot.append(float(batsmen[batsmen.NAME==i].BattingAverageRating))
        stk_listforplot.append(float(batsmen[batsmen.NAME==i].StrikeRateRating))
        brpi_listforplot.append(float(batsmen[batsmen.NAME==i].BRPI_Rating))
        or_listforplot.append(float(batsmen[batsmen.NAME==i].OutRateRating))

    bar3=[]
    bar4=[]
    bar5=[]
    
    for i in range(len(mra_listforplot)):
        bar3.append(mra_listforplot[i]+avg_listforplot[i])
        bar4.append(bar3[i]+stk_listforplot[i])
        bar5.append(bar4[i]+brpi_listforplot[i])
    	
    plt.bar(batsmen_name,or_listforplot,label='Out Rate Rating',color='c',bottom=bar5)
    plt.bar(batsmen_name,brpi_listforplot,label='BRPI Rating',color='y',bottom=bar4)
    plt.bar(batsmen_name,stk_listforplot,label='Strike Rate Rating',color='g',bottom=bar3)
    plt.bar(batsmen_name,mra_listforplot,label='MRA_Rating',color='r',bottom=avg_listforplot)
    plt.bar(batsmen_name,avg_listforplot,label='Average_Rating',color='b')
    plt.title('Batsman Statistical Attributes Rating')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()


graph_batsmen()
