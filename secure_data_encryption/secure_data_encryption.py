import streamlit as st
import hashlib
import json
import time
from cryptography.fernet import Fernet

# ----------------------------
# Generate a static encryption key
# ----------------------------
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# ----------------------------
# In-memory data storage
# ----------------------------
stored_data = {}
failed_attempts = 0

# ----------------------------
# Hash passkey with SHA-256
# ----------------------------
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# ----------------------------
# Encrypt data using Fernet
# ----------------------------
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# ----------------------------
# Decrypt data using Fernet
# ----------------------------
def decrypt_data(encrypted_text, passkey):
    global failed_attempts
    hashed_passkey = hash_passkey(passkey)

    for key, value in stored_data.items():
        if key == encrypted_text and value["passkey"] == hashed_passkey:
            failed_attempts = 0  # Reset on success
            return cipher.decrypt(encrypted_text.encode()).decode()

    failed_attempts += 1
    return None

# ----------------------------
# Streamlit App UI
# ----------------------------
st.set_page_config(page_title="🔒 Secure Data Encryption System", layout="centered")
st.title("🔒 Secure Data Encryption System")

# ----------------------------
# Navigation Menu
# ----------------------------
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# ----------------------------
# Home Page
# ----------------------------
if choice == "Home":
    st.subheader("🏠 Welcome!")
    st.info("➡️ Use the sidebar to **Store** or **Retrieve** data securely with your passkey.")

# ----------------------------
# Store Data Page
# ----------------------------
elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data to Encrypt:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)

            stored_data[encrypted_text] = {
                "passkey": hashed_passkey
            }

            st.success("✅ Data encrypted & stored securely!")
            st.code(f"Encrypted Data:\n{encrypted_text}")

        else:
            st.error("⚠️ Both Data and Passkey are required.")

# ----------------------------
# Retrieve Data Page
# ----------------------------
elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Data")
    encrypted_text = st.text_area("Enter Encrypted Data to Decrypt:")
    passkey = st.text_input("Enter Your Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)

            if result:
                st.success(f"✅ Decrypted Data:\n{result}")
            else:
                attempts_left = 3 - failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")

                if failed_attempts >= 3:
                    st.warning("🚫 Too many failed attempts! Redirecting to Login...")
                    time.sleep(2)
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required.")

# ----------------------------
# Login Page (Reauthorization)
# ----------------------------
elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Admin Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Demo purpose only
            failed_attempts = 0
            st.success("✅ Reauthorized! Redirecting to Retrieve Data...")
            time.sleep(1.5)
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect Admin Password!")
