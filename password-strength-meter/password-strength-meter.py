import streamlit as st
import re
import random
import string

# 🔹 Common Weak Passwords List
weak_passwords = ["password", "123456", "qwerty", "password123", "letmein", "welcome"]

# 🔹 Password Strength Check Function
def check_password_strength(password):
    score = 0
    feedback = []

    # 🚨 Check if password is in weak list
    if password.lower() in weak_passwords:
        return 0, "❌ This is a commonly used password. Please choose a stronger one."

    # ✅ Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # ✅ Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # ✅ Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # ✅ Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # 🔹 Strength Rating
    if score == 4:
        return 5, "✅ Strong Password! 💪"
    elif score == 3:
        return 3, "⚠️ Moderate Password - Consider adding more security features."
    else:
        return 1, "❌ Weak Password - Improve it using the suggestions above."

# 🔹 Password Generator Function
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for i in range(length))

# 🔥 Streamlit UI
st.title("🔑 Password Strength Meter")

# 🔹 Password Input
password = st.text_input("Enter your password", type="password")

if password:
    score, message = check_password_strength(password)
    st.write(f"Password Strength: {message}")

    # 🔹 Suggest Password if Weak
    if score < 4:
        st.write("🔹 **Try this strong password:**")
        st.code(generate_password(), language="")

# 🔥 Generate Strong Password Button
if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.write("🔹 **Suggested Strong Password:**")
    st.code(strong_password, language="")
