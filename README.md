Python Implementation of Apriori Algorithm 
==========================================

## Set up


[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://argaputra12-apriori-algorithm-streamlit-eqnu4t.streamlit.app/)
<a href="https://github1s.com/argaputra12/apriori-algorithm"><img src="https://cdn-icons-png.flaticon.com/512/331/331190.png" width="25"></a>


Running the Streamlit app locally
-----
To run the interactive Streamlit app with dataset  

    $ pip3 install -r requirements.txt
    $ streamlit run streamlit.py


----

CLI Usage
-----
To run the program with dataset provided and default values for *minSupport* = 0.15 and *minConfidence* = 0.6

    python main.py -f mami-tenong.csv

To run program with dataset  

    python main.py -f mami-tenong.csv -s 0.17 -c 0.68

Best results are obtained for the following values of support and confidence:  

Support     : Between 0.1 and 0.2  

Confidence  : Between 0.5 and 0.7 

----

Datasets
-------------

#### mami-tenong.csv

The dataset of items from food, drinks, and snacks that are sold in Mami Tenong.

