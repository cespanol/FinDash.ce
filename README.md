# FinDash.ce
An experimental financial dashboard through streamlit in the works. Trying to connect Plaid API to call on sandbox info, then use that to create my pages. Would love to learn more about how to code more and more complex interactions. 

FinDash.ce is a Streamlit-based financial dashboard application that allows users to track and manage their accounts, investments, transactions, and other financial data.

## Features

- User login and authentication
- OpenAI API integration
- Multiple pages for managing financial data
- Sidebar navigation

## Installation

Before running the application, make sure to install the required Python packages:

```bash
pip install streamlit PyPDF2 langchain werkzeug
```

Usage
To run the application, simply run the following command:

```bash
streamlit run Dashboard.py
```
The application will open in your default web browser. If not, open your browser and navigate to http://localhost:8501.

Application Structure
get_openai_api_key(): Function to obtain the OpenAI API key.
login(): Function to handle user login and authentication.
main(): The main function that initializes the Streamlit application and sets up the user interface.
Pages
The application includes the following pages:

Accounts: (Plaid API connection is currently commented out. To enable, uncomment the relevant lines and follow the instructions to integrate Plaid.)
Investments: Displays investment account information and allocation.
Transactions: Lists financial transactions.
Dashboard: Provides a general overview of the user's financial status.
Categories: Manages financial categories.
Recurrings: Manages recurring financial transactions.
Savings: Displays and manages the user's savings.
Note
The Plaid API integration is currently commented out in the code. Need help integrating the client


Goals: Create a user financial dashboard. Use that to create an accounting financial dashboard.
Use streamlit for interface
integrate openai, plaid, langchain



Application Structure
get_openai_api_key(): Function to obtain the OpenAI API key.
login(): Function to handle user login and authentication.
main(): The main function that initializes the Streamlit application and sets up the user interface.
Pages
The application includes the following pages:

Accounts: (Plaid API connection is currently commented out. To enable, uncomment the relevant lines and follow the instructions to integrate Plaid.)
Investments: Displays investment account information and allocation.
Transactions: Lists financial transactions.
Dashboard: Provides a general overview of the user's financial status.
Categories: Manages financial categories.
Recurrings: Manages recurring financial transactions.
Savings: Displays and manages the user's savings.
Note
The Plaid API integration is currently commented out in the code. To enable it, uncomment the relevant lines and follow the instructions to integrate Plaid.



Outline Rough Draft:
```bash
Main frame:
Sidebar
    Settings
        username
        password
        api secret key

    Dashboard Menu
        Accounts
            
            Net Income Graph
                Assets vs Debts 
                    Graph
            
            Credit Cards - Total $
                Balance $
                Utilized $
            
            Depository - Total $
                Available $
                Change $ (?)

        Investments

            Graph of total Balance
        
            Investment Accounts
                graph line preview and change %

            Allocation

        Transactions
            Search bar
            Add a new Transactions
            List of Transactions

            Today
            Yesterday
            THU, APRIL 28
            Netflix Emoji-Category $25.65



        Investments
        Transactions
        Dashboard
        Categories
        Recurrings
        Savings
        


Mainbar
    Pages of Dashboard Menu
        Title
        Header
        Subheader
        Write

        Accounts
        Investments
```




    
