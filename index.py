import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔑", layout="centered")

# Custom CSS for Gradient Theme
st.markdown(
    """
    <style>
        /* Gradient Background */
        html, body, [class*="stApp"] {
            background: linear-gradient(135deg, #0A192F, #321450) !important;
            color: #E0E0E0 !important;
        }

        /* Center Content */
        div.block-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 95vh;
            padding-top: 3rem !important;
        }

        /* Hide Extra UI */
        header, footer, [data-testid="stToolbar"], 
        [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
            display: none !important;
        }

        /* Headings */
        h1 {
            color: #64FFDA;
            text-align: center;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 10px rgba(100, 255, 218, 0.5);
        }

        /* Input Field */
        .stTextInput > div > div > input {
            width: 60% !important;
            margin: auto;
            background-color: #1B2A41;
            color: #ffffff;
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #64FFDA;
            box-shadow: 0px 0px 8px rgba(100, 255, 218, 0.4);
        }

        /* Buttons */
        .stButton button {
            width: 50%;
            background: linear-gradient(90deg, #112D4E, #6A0572);
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px;
            border: none;
            transition: 0.3s;
        }
        .stButton button:hover {
            background: linear-gradient(90deg, #6A0572, #112D4E);
            transform: scale(1.05);
        }

        /* Password Box */
        .password-box {
            padding: 20px;
            background: rgba(17, 45, 78, 0.9);
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(100, 255, 218, 0.3);
            width: 50%;
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title
st.title("🔐 Password Strength Checker")

# Introduction
st.markdown("""
### 🔍 Why Use This Tool?
A strong password is crucial to **protect your accounts from cyber threats**.

This tool evaluates your password based on:  
✅ **Length** (minimum 8 characters)  
✅ **Uppercase & lowercase letters**  
✅ **Numbers**  
✅ **Special characters (!@$%&*#)**  

**💡 Enter your password below to check its strength and get improvement tips!**
""")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❎ Password should be **at least 8 characters long**.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❎ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else: 
        feedback.append("❎ Password should include **at least 1 number**.")

    if re.search(r"[!@$%&*#]", password):
       score += 1
    else: 
        feedback.append("❎ Password should include **at least 1 special character (!@$%&*#)**.")

    # Display password strength result
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure!")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback for improvements
    if feedback:
        with st.expander("🔎 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# User Input
password = st.text_input("🔑 Enter your Password:", type="password", help="Ensure your password is strong. 💪")

# Button
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
