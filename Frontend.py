import streamlit as st
import pickle
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import os 

# Change the working directory to your project folder
os.chdir(r'C:\Users\91939\Desktop\AI&DS\Data science projects\BodyMetricsAnalyzer')

# Load the saved model from the file
filename = 'final_model.pkl'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Function to read and encode the image file
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Set the background image using CSS
def set_background(image_base64):
    page_bg_img = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }}
    .css-1g8v9l0 {{
        background: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }}
    .stButton > button {{
        background-color: #4C4C6D;
        color: white;
    }}
    .stButton > button:hover {{
        background-color: #6A5ACD;
        color: white;
    }}
    .stSlider > div {{
        background-color: transparent;
    }}
    .stSelectbox div {{
        color: white;
    }}
    .stSubheader {{
        color: white;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the function with the uploaded background image
image_base64 = get_base64_image("image.jpg")  # Path to your uploaded image
set_background(image_base64)

# Create the Streamlit web app
st.title('Body Metrics Analyzer 🔍')
st.subheader('Description: ')
st.write('The **Body Metrics Analyzer** app predicts a person’s weight based on their height. Users can input their height, and the app provides an accurate weight prediction. This tool is useful for personal fitness tracking, healthcare assessments, or other applications that require an estimation of weight based on height.')

# Display the dataset
st.subheader('📄 Dataset Preview')
df = pd.read_csv('SOCR-HeightWeight.csv')
df['Height(Feet.Inches)'] = df['Height(Inches)'] // 12 + (df['Height(Inches)'] % 12) / 10
df['Weight_kg'] = df['Weight(Pounds)'] * 0.453592  
df = df.drop(columns = ['Index','Height(Inches)','Weight(Pounds)'])
st.dataframe(df.head())

st.info("ℹ️ **Note:** The weight predictions are based on a machine learning model that was trained using the dataset shown above.")

# Input fields for height
st.subheader('🔢 Input Feature: Height')

# User enters the height in "feet.inches" format
height_input = st.text_input("📏 Enter height in feet.inches (e.g., 5.10 for 5 feet 10 inches):", value="5.4")

# Function to convert feet.inches format to a float value
def convert_height_to_float(height_str):
    if "." in height_str:
        feet, inches = height_str.split(".")
        feet = int(feet)
        inches = int(inches)
        return feet + (inches / 12)  # Convert inches to a fraction of a foot
    else:
        return float(height_str)  # If no inches part, return as is

# Convert the user input to a proper float value
height_in_feet = convert_height_to_float(height_input)

# Prediction button
if st.button('🔮 Predict'):
    # Reshape the input height to match the shape expected by the model (2D array)
    height_input_2d = np.array([[height_in_feet]])  # Make it a 2D array

    # Use the loaded model to make predictions
    predicted_weight = loaded_model.predict(height_input_2d)

    # Extract the predicted weight and format it to 2 decimal places
    formatted_weight = f"{predicted_weight[0][0]:.2f}"  # Extract scalar from the array

    # Display the predicted weight
    st.markdown(f'<p class="prediction">🎯 Predicted weight: **{formatted_weight} kg**</p>', unsafe_allow_html=True)

# Set seaborn style for the plots
sns.set(style="darkgrid")

# Create two columns in Streamlit
col1, col2 = st.columns(2)

with col1:
    # Plot the Height vs Weight scatter plot
    st.subheader('📉 Height vs Weight Visualization')
    fig, ax = plt.subplots(figsize=(6, 4))  # Make the plot smaller

    # Create a scatter plot
    scatter = ax.scatter(df['Height(Feet.Inches)'], df['Weight_kg'], c=df['Height(Feet.Inches)'], cmap='BuPu', alpha=0.8, edgecolor='none')

    # Customize the plot
    ax.set_title('Height vs. Weight', fontsize=14)
    ax.set_xlabel('Height (Feet.Inches)')
    ax.set_ylabel('Weight (kg)')
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.8)  # Customize the grid
    plt.colorbar(scatter, label='Height(Feet.Inches)')
    plt.tight_layout()  # Avoid overlapping of the plot

    # Display the plot in the first column
    st.pyplot(fig)

with col2:
    # Display the inference in the second column
    st.info("🔍 **Inference from the Plot:**")
    st.write('''                 
    
    1. 📈 **Positive Correlation**: This plot indicates a positive correlation between height and weight.
    2. 📊 **Density of Data Points**: The central region, between heights of 5.5 to 6 feet, shows the highest density of data points. This suggests that most individuals fall within this height range and have corresponding weights between 50 to 70 kg.
    ''')

# End of the app
