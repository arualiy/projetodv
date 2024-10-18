import streamlit as st

# Streamlit Title
st.title('Olympic Medalists Data Visualization')

# 1. Medals by Country (Bar Graph)
st.subheader('Medals Won by Country')
medals_by_country = df['country_medal'].value_counts()

fig1, ax1 = plt.subplots()
medals_by_country.plot(kind='bar', color='gold', edgecolor='black', ax=ax1)
ax1.set_title('Medals Won by Country')
ax1.set_xlabel('Country')
ax1.set_ylabel('Number of Medals')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
st.pyplot(fig1)