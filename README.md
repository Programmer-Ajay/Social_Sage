# SOCIALSAGE An Social Media Assistant Expert

The SocialSage  is a powerful tool designed to help users gain valuable insights from their social media data. This bot processes the provided data and generates meaningful metrics, including averages and other key performance indicators, to aid in decision-making and strategy development.
 
 # Features:
 ● Data Analysis: Provides a comprehensive analysis of social media data.
 ● Insights Generation: Offers averages and other important metrics for better understanding.
 ● User-Friendly: Simple to use, ensuring quick and efficient results.


##  Tools we used in this project:
● DataStax Astra DB for database operations.

● Langflow for workflow creation and GPT integration.

● Streamlit for frontend access of Langflow.
● CSS for designing.

### How to run it on your own machine
  
  *** We use use the  github codespace  for development 

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```




## Important Instruction

● Ensure  that you have a valid LangFlow API_TOKEN before running the application.

● The API token is stored securely in the .env file and accessed through python-dotenv

● Store the API_token also in streamlit at the time of development