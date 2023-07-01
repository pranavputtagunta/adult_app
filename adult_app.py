import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache_data()
def load_data():
	df = pd.read_csv("adult.csv", header=None)
	df.head()

	column_name = ['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	for i in range(df.shape[1]):
		df.rename(columns={i:column_name[i]}, inplace=True)

	df.head()

	df['native-country'] = df['native-country'].replace(' ?', np.nan)
	df['workclass'] = df['workclass'].replace(' ?', np.nan)
	df['occupation'] = df['occupation'].replace(' ?', np.nan)

	df.dropna(inplace= True)
	df.drop(columns='fnlwgt', axis=1, inplace= True)
	return df

census_df = load_data()

if st.checkbox("Display raw data"):
	st.subheader(f"Full dataset with {census_df.shape[0]} rows and {census_df.shape[1]} columns")
	st.dataframe(census_df)
