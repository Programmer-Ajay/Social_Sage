
import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os
import base64
from pathlib import Path

# # Load environment variables from .env file
load_dotenv()


# Streamlit Page Configuration
st.set_page_config(
    page_title="SocialSage - An Social Media Analytics Expert",
    page_icon="images/socialsageicon.jpeg",
    # layout="wide", // for wide screen
    initial_sidebar_state="auto",
)

# Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "3903f33a-8df6-4c4c-9e26-759f7f7c1ffd"
FLOW_ID = "95ca71da-ca13-45f6-afd8-98afc3dea823"
# Replace with your actual token
APPLICATION_TOKEN = os.environ.get("SOCIAL_APPLICATION_TOKEN")
ENDPOINT = "chat"
# logo img path
image_path = "images/SocialSage_avatar_original.JPG" 

# Custom CSS for a fixed navbar
navbar_css = """
<style>
/* Fixed Navbar */

.navbar {
    margin:0;
    display: flex;
    align-items: center;
    justify-content: start;
    # background-color: #ffffff;
    padding: 0px 20px;
    width: 100%;
    height:90px;
    z-index: 1000; /* Ensure the navbar stays on top */
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); /* Optional shadow */
    margin-bottom:25px;
}

/* Logo in Navbar */
.navbar img {
    max-height: 100%; /* Set maximum height */
    width: auto; /* Maintain aspect ratio */
    margin-right: 15px;
    # margin-top:5px;
    object-fit: contain;
}

/* Title in Navbar */
.navbar h1 {
    font-size: 70px;
    color: #ffffff;
    margin-left: 20px;
    font-weight: 800;
}

/* Media Query for Navbar Title Font Size on Small Screens */

@media (max-width: 576px) {
    .navbar h1 {
        font-size: 25px; /* Reduce font size for smaller screens */
    }
}

@media (min-width: 576px) and (max-width: 894px) {
    .navbar h1 {
        font-size: 45px; /* Reduce font size for smaller screens */
    }
}

</style>
"""
# All functions are start from here

# Function to encode a local image as Base64
def encode_image(image_path):
    """Encodes an image to Base64 to use in HTML."""
    with open(image_path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode()
    return b64_data



if not Path(image_path).exists():
    st.error("Image file not found. Please check the file path.")
else:
    image_base64 = encode_image(image_path)


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




def main():
  # Insert custom CSS for glowing effect
 st.markdown(
        """
        <style>
        .cover-glow {
            width: 100%;
            height: auto;
            padding: 3px;
            box-shadow: 
                0 0 5px #330000,
                0 0 10px #660000,
                0 0 15px #990000,
                0 0 20px #CC0000,
                0 0 25px #FF0000,
                0 0 30px #FF3333,
                0 0 35px #FF6666;
            position: relative;
            z-index: -1;
            border-radius: 45px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
   # Load and display sidebar image
 img_path = "images/SocialSage_avatar_original.JPG"
 img_base64 = encode_image(img_path)
 if img_base64:
      st.sidebar.markdown(
      f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
      unsafe_allow_html=True,
      )

 st.sidebar.markdown("---")
#    social sage feature 
 st.sidebar.markdown("""
        ### Features
        - **Ask about your social media content**: Type your questions and get the stats of your content.
        - **Powered by LangFlow and DataStax for robust and accurate analysis.**:Based on your data gives you stats of your data.
        
        """)



# NavBar section

# Inject the custom CSS
 st.markdown(navbar_css, unsafe_allow_html=True)

# Navbar content with local image
 st.markdown(
    f"""
    
    <div class="navbar">
        <img src="data:image/png;base64,{image_base64}" alt="Chatbot Logo">
        <h1>SocialSage</h1>
    </div>
    
    """,
    unsafe_allow_html=True
)

# Body content
 st.write("Welcome to SocialSage! Your Personal Social Media Assistant.")
 

# End the container div
 st.markdown('</div>', unsafe_allow_html=True)
 

 # User input using st.chat_input
 user_message = st.chat_input(placeholder="Type your message here...")

 if user_message:
    st.warning(user_message)
    try:
        # Call the Langflow API (Replace with your function)
        response = call_langflow_api(user_message)

        if "outputs" in response:
            output = response["outputs"][0]["outputs"][0]["outputs"]["message"]["message"]["text"]
            st.success("Response:")
            st.write(output)
        else:
            st.error("Failed to retrieve a valid response from the API.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
  main()




