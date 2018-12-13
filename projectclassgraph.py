

import matplotlib.pyplot as plt
import pandas as pd
import requests
import sys


class graph_data():
   #List


        def display_artist_and_region(country code, ranking):
                """
                Scatter plot comparing the artist verse region
                """
                plt.style.use('seaborn')
                fig = plt.figure()
                df.plot( x='Artist', y='Region', kind='scatter', marker = '.')
                plt.title('Artist and Region')
                plt.xlabel('Artist')
                plt.ylabel('Region')
                plt.show()

        def compilelist():
            my_df = pd.DataFrame(data=[], index=range(0,), columns=[])

    if __name__ == '__main__':
        def display_artist_and_region(country code, ranking)
