import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your data (replace with actual path or data source)
data = pd.read_csv("./nlp_results/rev_topic.csv")

# Exclude unwanted source
data = data[data['source'] != 'www.hostelworld.com']

# Streamlit app
st.title("Hotel Classification Results Viewer")

# Dropdown for selecting classif_result
classif_options = data['classif_result'].unique()
selected_classif = st.selectbox("Select a classification result:", classif_options)

# Filter data by the selected classif_result
filtered_data = data[data['classif_result'] == selected_classif]

# Calculate the mean score for each unique title (hotel name)
mean_scores = filtered_data.groupby('source')['score'].mean().reset_index()

# Find the best hotel based on mean score
best_hotel = mean_scores.loc[mean_scores['score'].idxmax()]

# Display results
st.subheader("Best Hotel for Selected Category")
st.write(f"**Hotel Name:** {best_hotel['source']}")
st.write(f"**Mean Score:** {best_hotel['score']:.2f}")

# Plot mean scores for hotels in the selected category
st.subheader("Mean Scores for Each Hotel")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(mean_scores['source'], mean_scores['score'], color='skyblue')
ax.set_title(f"Mean Scores by Hotel for Category: {selected_classif}")
ax.set_xlabel("Hotel")
ax.set_ylabel("Mean Score")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability

# Display the plot
st.pyplot(fig)
