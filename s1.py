import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title = "Used Car Analysis",
    layout = "wide",
    page_icon = "🚗"
)

df = pd.read_csv('project/clean_vehicle_data.csv')
# st.dataframe(df)

with st.sidebar:

    opt = option_menu("Menu",['🏠 Home','🧾 Dataset','🧹 Preprocessing','📊 Visulaization','About'])
    selected_state=st.multiselect("Select State",options = df["State"].unique())


if selected_state :
    filtered = df[df['State'].isin(selected_state)]
else:
    filtered = df


if opt=='🏠 Home':
    st.title('Used Car Dashbord')
    st.markdown('### Explore the cleaned used vehicle dataset with interactive analytics.')

    Vehicles = filtered['Brand'].nunique()
    total_brand = filtered['Brand'].nunique()
    avg_price = filtered['Price'].mean()
