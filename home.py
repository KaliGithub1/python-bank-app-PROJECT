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
st.title("OMEGA Bank App")
st.header("Hi, welcome to OMEGA Bank App")
st.write("Your one-stop solution for digital banking.")
st.subheader("I AM SAADA, YOUR DIGITAL BANKING ASSISTANT")
st.balloons()
if not st.session_state.logged_in:
    st.subheader("Login")
    useremail = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if useremail in USERS and USERS[useremail]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.user = useremail
            st.session_state.account_data = USERS[useremail]
            st.success(f"Welcome back, {useremail}!")
        else:
            st.error("Invalid email or password.")
if st.session_state.logged_in:
    user_data = st.session_state.get("account_data")

    if user_data:
        savings_account = SavingsAccount(user_data["savings"])
        current_account = CurrentAccount(user_data["current"])
st.subheader("Choose Account Type")
account_type = st.radio("Select an account:", ["Savings Account", "Current Account"])

st.subheader("Transaction Options")
transaction_type = st.selectbox("Select a transaction:", ["Deposit", "Withdraw", "Check Balance"]amount = st.number_input("Enter amount:", min_value=0.0, max_value=500000.0))
if st.button("Submit"):
            if account_type == "Savings Account":
                if transaction_type == "Deposit":
                    if amount > 0:
                        savings_account.deposit(amount)
                        user_data["savings"] = savings_account.balance
                        st.success(f"Successfully deposited:")
                    else:
                        st.error("Deposit amount must be greater than zero.")
                elif transaction_type == "Withdraw":
                    if amount >1000.00:
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
            elif account_type == "Current Account":
             if transaction_type == "Deposit":
                if amount > 0:
                 current_account.deposit(amount)  # Update the current account balance
                user_data["current"] = current_account.balance  # Update session data
             st.success(f"Successfully deposited N{amount:.2f} into Current Account.")
            else:
             st.error("Deposit amount must be greater than zero.")
elif transaction_type == "Withdraw":
    if amount > 0.00:
        if current_account.withdraw(amount):
            user_data["current"] = current_account.balance 
            st.success(f"Successfully withdrew N{amount:.2f} from Current Account.")
        else:
            st.error("Insufficient funds in Current Account.")
    else:
        st.error("Withdrawal amount must be greater than zero.")
        
else:
         st.error("Insufficient funds in Current Account.")
    

         st.error("Withdrawal amount must be greater than zero.")
elif transaction_type == "Check Balance":
    st.info(f"Current Balance: N{current_account.balance:.2f}")

    else:
        st.error("Invalid transaction type.")
        st.error("Invalid account type selected.")
    if st.button("Logout"):
        st.session_state.update(logged_in=False, user=None, account_data=None)
        st.success("You have been logged out.")
