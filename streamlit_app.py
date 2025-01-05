


# # Main function
# def main():
#     st.title("SocialSage")

#     # Initialize session state for chat history
#     if "messages" not in st.session_state:
#         st.session_state["messages"] = []

#     # Input field for the user
#     message = st.text_area("", placeholder="How can we assist you today?")

#     # Button to send the query
#     if st.button("Generate Insights"):
#         if not message.strip():
#             st.error("Please enter a message")
#             return

#         try:
#             with st.spinner("Running flow..."):
#                 response = run_flow(message)
#                 response_text = response.get('outputs', [])[0].get('outputs', [])[0].get('results', {}).get('message', {}).get('text', 'Sorry, I did not understand that.')
#                 print("response from :",response_text)

#             # Append user message and response to chat history
#             st.session_state["messages"].append({"user": message, "bot": response_text})

#         except Exception as e:
#             st.error(str(e))

#     # Display chat history
#     st.subheader("Chat History")
#     for chat in st.session_state["messages"]:
#         st.markdown(f"**You:** {chat['user']}")
#         st.markdown(f"**Bot:** {chat['bot']}")
#         st.divider()  # Adds a divider for better readability

# if __name__ == "__main__":
#     main()



import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os  

# # Load environment variables from .env file
load_dotenv()
ENDPOINT = "chat"

# Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "3903f33a-8df6-4c4c-9e26-759f7f7c1ffd"
FLOW_ID = "95ca71da-ca13-45f6-afd8-98afc3dea823"
APPLICATION_TOKEN = os.environ.get("SOCIAL_APPLICATION_TOKEN")   # Replace with your actual token

# Function to call the Langflow API
def call_langflow_api(message, endpoint=FLOW_ID, tweaks=None):
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    if tweaks:
        payload["tweaks"] = tweaks

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Streamlit App
st.title("Langflow API Chat Interface")
st.write("Enter your message below to interact with the Langflow flow.")

# User input
user_message = st.text_input("Your Message:", placeholder="Type your message here...")
if st.button("Send"):
    if not user_message.strip():
        st.error("Please enter a valid message.")
    else:
        st.write("Processing...")
        try:
            # Call the Langflow API
            response = call_langflow_api(user_message)
            if "outputs" in response:
                output = response["outputs"][0]["outputs"][0]["outputs"]["message"]["message"]["text"]
                st.success("Response:")
                st.write(output)
            else:
                st.error("Failed to retrieve a valid response from the API.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
