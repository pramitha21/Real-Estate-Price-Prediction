import streamlit as st
import util

# Load the saved artifacts when the app starts
util.load_saved_artifacts()

# Streamlit app title
st.title("Home Price Prediction App")

# Sidebar inputs
st.sidebar.header("Input Features")

# Dropdown for location
locations = util.get_location_names()
location = st.sidebar.selectbox("Select Location", locations)

# Input for total square feet
total_sqft = st.sidebar.number_input("Total Square Feet", min_value=500.0, step=10.0, value=1000.0)

# Input for BHK
bhk = st.sidebar.number_input("Number of BHK", min_value=1, max_value=10, step=1, value=2)

# Input for bathrooms
bath = st.sidebar.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1, value=2)

# Predict button
if st.sidebar.button("Predict Price"):
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    st.success(f"Estimated Price: ₹ {estimated_price:,.2f} Lakhs")

# Optional: Show data sources or any additional information
st.sidebar.markdown("---")
st.sidebar.info("This app predicts the home price based on the selected parameters.")

