import streamlit as st
from savings_account import SavingsAccount
from current_account import CurrentAccount

st.set_page_config(page_title="OMEGA Bank App", layout="centered")
USERS = {
    "sulesaada19@gmail.com": {"password": "1234", "savings": 200000, "current": 50000},
    "calebonuh@gmail.com": {"password": "@123", "savings": 40000, "current": 1000000},
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

st.markdown("""
<div style="background-color:#0a3d62;padding:30px 20px 20px 20px;border-radius:15px;margin-bottom:25px;">
    <h1 style="color:#fff;text-align:center;margin-bottom:10px;">🌟 <span style='color:#f9ca24;'>OMEGA Bank App</span> 🌟</h1>
    <h3 style="color:#f6e58d;text-align:center;margin-bottom:5px;">Hi, welcome to <span style='color:#f9ca24;'>OMEGA Bank App</span></h3>
    <p style="color:#dff9fb;text-align:center;font-size:18px;">Your one-stop solution for digital banking.</p>
    <div style="text-align:center;margin-top:20px;">
        <span style="font-size:22px;">🤖</span>
        <span style="color:#f9ca24;font-weight:bold;font-size:20px;">I AM SAADA, YOUR DIGITAL BANKING ASSISTANT</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.balloons()

if not st.session_state.logged_in:
    st.subheader("Login")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/747/747376.png", width=80)
    with col2:
        st.markdown("<h4 style='margin-bottom:10px;'>Please enter your credentials</h4>", unsafe_allow_html=True)
        useremail = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        if st.button("Login"):
            if useremail in USERS and USERS[useremail]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.user = useremail
                st.session_state.account_data = USERS[useremail]
                st.success(f"Welcome back, {useremail}!")
                st.rerun()
            else:
                st.error("Invalid email or password.")

if st.session_state.logged_in:
    user_data = st.session_state.get("account_data")
    if user_data:
        savings_account = SavingsAccount(user_data["savings"])
        current_account = CurrentAccount(user_data["current"])

        # --- Account Type Section ---
        st.markdown("""
        <div style="background-color:#f0f2f6;padding:20px 20px 10px 20px;border-radius:10px;margin-bottom:20px;">
            <h4 style="color:#0a3d62;margin-bottom:10px;">🏦 Choose Account Type</h4>
        </div>
        """, unsafe_allow_html=True)
        account_type = st.radio(
            "Select an account:",
            ["💰 Savings Account", "💳 Current Account"],
            horizontal=True
        )

        # --- Transaction Options Section ---
        st.markdown("""
        <div style="background-color:#f0f2f6;padding:20px 20px 10px 20px;border-radius:10px;margin-bottom:20px;">
            <h4 style="color:#0a3d62;margin-bottom:10px;">💼 Transaction Options</h4>
        </div>
        """, unsafe_allow_html=True)
        transaction_type = st.selectbox(
            "Select a transaction:",
            ["Deposit", "Withdraw", "Check Balance"]
        )
        amount = st.number_input("Enter amount:", min_value=0.0, max_value=500000.0)

        if st.button("Submit"):
            # Remove emoji for logic
            acc_type = "Savings Account" if "Savings" in account_type else "Current Account"
            if acc_type == "Savings Account":
                if transaction_type == "Deposit":
                    if amount > 0:
                        savings_account.deposit(amount)
                        user_data["savings"] = savings_account.balance
                        st.success(f"Successfully deposited N{amount:.2f} into Savings Account.")
                    else:
                        st.error("Deposit amount must be greater than zero.")
                elif transaction_type == "Withdraw":
                    if amount > 0:
                        if savings_account.withdraw(amount):
                            user_data["savings"] = savings_account.balance
                            st.success(f"Successfully withdrew N{amount:.2f} from Savings Account.")
                        else:
                            st.error("Insufficient funds in Savings Account.")
                    else:
                        st.error("Withdrawal amount must be greater than zero.")
                elif transaction_type == "Check Balance":
                    st.info(f"Savings Balance: N{savings_account.balance:.2f}")
                else:
                    st.error("Invalid transaction type.")
            elif acc_type == "Current Account":
                if transaction_type == "Deposit":
                    if amount > 0:
                        current_account.deposit(amount)
                        user_data["current"] = current_account.balance
                        st.success(f"Successfully deposited N{amount:.2f} into Current Account.")
                    else:
                        st.error("Deposit amount must be greater than zero.")
                elif transaction_type == "Withdraw":
                    if amount > 0:
                        if current_account.withdraw(amount):
                            user_data["current"] = current_account.balance
                            st.success(f"Successfully withdrew N{amount:.2f} from Current Account.")
                        else:
                            st.error("Insufficient funds in Current Account.")
                    else:
                        st.error("Withdrawal amount must be greater than zero.")
                elif transaction_type == "Check Balance":
                    st.info(f"Current Balance: N{current_account.balance:.2f}")
                else:
                    st.error("Invalid transaction type.")
            else:
                st.error("Invalid account type selected.")

        if st.button("Logout"):
            st.session_state.update(logged_in=False, user=None, account_data=None)
            st.success("You have been logged out.")
            st.rerun()
