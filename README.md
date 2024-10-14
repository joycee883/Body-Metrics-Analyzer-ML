# 🎯 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐒𝐩𝐨𝐭𝐥𝐢𝐠𝐡𝐭: 𝐁𝐨𝐝𝐲 𝐌𝐞𝐭𝐫𝐢𝐜𝐬 𝐀𝐧𝐚𝐥𝐲𝐳𝐞𝐫 𝐰𝐢𝐭𝐡 𝐌𝐚𝐜𝐡𝐢𝐧𝐞 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠

### 📋 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰

The Body Metrics Analyzer project is designed to predict an individual's weight based on their height, using machine learning techniques. By leveraging real-world data and predictive models, this project aims to offer a streamlined way to estimate body weight, providing value in fitness applications, health assessments, and personalized wellness services. The project involves end-to-end data handling, model training, evaluation, and an interactive web-based interface for real-time predictions using Streamlit.

### 🛠️ 𝐓𝐨𝐨𝐥𝐬 𝐔𝐬𝐞𝐝

Programming Language: Python<br> Libraries:<br>
NumPy: For efficient numerical computations.<br>
Pandas: For handling and preprocessing data.<br>
Scikit-learn: For model development, training, and evaluation.<br>
Matplotlib & Seaborn: For data visualization and exploratory analysis.<br>
Streamlit: For creating an interactive and user-friendly web app.<br>

### 🔍 𝐊𝐞𝐲 𝐒𝐭𝐞𝐩𝐬

1.Data Collection & Preprocessing<br>
  * Data Source: A dataset containing height and weight measurements of individuals, along with additional optional attributes like gender and age.<br>
  * Data Cleaning: Checked for missing values and outliers, removed or imputed missing data where necessary.<br>
  * Feature Scaling: Used standardization techniques to scale numerical features (height, weight) to ensure consistent ranges for model inputs.<br>
  * Feature Engineering: Considered adding derived features like BMI, although the primary focus remained on height-to-weight predictions.<br>

2. Exploratory Data Analysis (EDA)<br>

  * Conducted visual analysis using scatter plots to understand the relationship between height and weight.
  * Visualized correlations between variables using heatmaps, confirming that height has a strong positive correlation with weight.<br>

3. Model Training<br>

  * Trained multiple regression models to predict weight based on height:<br>
  * Linear Regression: A baseline model assuming a linear relationship between height and weight.<br>
  * Random Forest Regressor: An ensemble model capturing complex relationships with high variance.<br>
  * Decision Tree Regressor: For visualizing the decision-making process in predictions.<br>

4. Model Evaluation<br>

  * Assessed models using common metrics for regression tasks:<br>
  * Mean Absolute Error (MAE): Measures the average magnitude of errors in predictions.<br>
  * Mean Squared Error (MSE): Emphasizes larger errors by squaring the difference between predicted and actual weights.<br>
  * R² Score: Evaluates how well the model explains the variance in the target variable (weight).<br>
  * Compared the performance of models to identify the best one for predicting weight.<br>

5. Model Deployment<br>

  * Deployed the model using Streamlit, allowing users to input their height and other optional features like gender to get instant weight predictions.<br>
  * Integrated user input sliders and interactive elements in the app, making it easy to use for anyone, from fitness enthusiasts to health professionals.<br>
  
### 📊 𝐊𝐞𝐲 𝐅𝐢𝐧𝐝𝐢𝐧𝐠𝐬
Model Results:

1.Linear Regression: Provided a simple yet effective solution for height-to-weight prediction with good accuracy.<br>
* MAE: 21.69<br>
* R² Score: 0.94<br>

2.Random Forest Regressor: Demonstrated slightly better performance in terms of accuracy, especially for complex data points.<br>
* MAE: 31.10<br>
* R² Score: 0.92<br>

3.Decision Tree: Worked effectively but tended to overfit the training data.<br>
* MAE: 41.50<br>
* R² Score: 0.90<br>

Best Performing Model: LinearRegressor showed the highest accuracy and robustness, making it the preferred model for deployment.

### 🌐 𝐀𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧

The Body Metrics Analyzer app, built using Streamlit, allows users to input their height, and optionally, age or gender, to predict their weight. The app is designed with a clean, intuitive interface and provides real-time predictions. This tool can be particularly useful for:
* Fitness Enthusiasts: Estimating body weight based on height for setting fitness goals or checking health parameters like BMI.
* Health Practitioners: Offering patients a quick estimate of body metrics without the need for physical measurement tools.
* Personal Trainers & Wellness Coaches: Providing quick assessments for clients, especially when access to weighing scales is limited.
  
### 🔮 𝐅𝐮𝐭𝐮𝐫𝐞 𝐈𝐦𝐩𝐫𝐨𝐯𝐞𝐦𝐞𝐧𝐭𝐬

* Incorporating more features like body fat percentage and muscle mass predictions based on additional data inputs like age, gender, and activity levels.
* Expanding the dataset to include diverse populations for more generalized predictions.
* Adding features to estimate BMI and recommend fitness or dietary plans based on the user's weight prediction and health goals.

https://bodymetricsanalyzer-v6na3dsemdxvs3azfzpzbk.streamlit.app/
