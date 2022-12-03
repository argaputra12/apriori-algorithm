import streamlit as st
import pandas as pd
import numpy as np

from main import runApriori, dataFromFile, resultsToSring

st.markdown("# Apriori Streamlit for Data Mining")

used_csv = st.selectbox("Select a CSV file", ['mami-tenong.csv'])

st.markdown('The dataset is a food, beverage, and drinks dataset contain frequently purchased Mami Tenong')

st.markdown('Here are some sample rows from the dataset')
csv_file = pd.read_csv(used_csv, nrows=2, header=None)
st.write(csv_file.head())

st.markdown('## Apriori Algorithm')
st.markdown('Apriori is an algorithm for frequent item set mining and association rule learning over transactional databases. It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets as long as those item sets appear sufficiently often in the database.')

st.markdown('---')
st.markdown('## Inputs')
st.markdown('''
    **Minimum Support** is the minimum number of transactions that contain the itemset.

    **Minimum Confidence** is the minimum confidence that the rule has to have.
''')

st.markdown('Support and Confidence for Itemsets A and B can be represented by formulas')

support_helper = ''' > Support(A) = (Number of transactions in which A appears)/(Total Number of Transactions') '''
confidence_helper = ''' > Confidence(A->B) = Support(AUB)/Support(A)') '''
st.markdown('---')

support = st.slider("Enter the Minimum Support Value", min_value=0.1,
                    max_value=0.9, value=0.15,
                    help=support_helper)

confidence = st.slider("Enter the Minimum Confidence Value", min_value=0.1,
                       max_value=0.9, value=0.6, help=confidence_helper)

inFile = dataFromFile(used_csv)

items, rules = runApriori(inFile, support, confidence)

i, r = resultsToSring(items, rules)

st.markdown("## Results")

st.markdown("### Frequent Itemsets")
st.write(i)

st.markdown("### Frequent Rules")
st.write(r)