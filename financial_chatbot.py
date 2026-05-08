print("Welcome to the Financial Chatbot! How can I assist you today?")
import pandas as pd
df=pd.read_csv(r"C:\Users\Admin\Desktop\BCG GEN AI\Boston_consulting_group_Job_simulation\data\Financial data - Sheet1.csv")#Reading the financial data from the CSV file

while True:
    query = input("Please enter your financial query: ")

    # Simulating a response based on the user's query
    query_lower = query.lower()
    if "exit" in query_lower or "quit" in query_lower:#Exit Information
        print("Thank you for using the Financial Chatbot. Goodbye!")
        break
    elif "highest" in query_lower:#Highest Revenue Information
        if "revenue" in query_lower:
            print("Apple had the highest revenue in 2023 with 383285 million USD.")
        elif "net income" in query_lower:
            print("Apple had the highest net income in 2023 with 96995 million USD.")
    elif "lowest" in query_lower:#Lowest Revenue Information
        if "revenue" in query_lower:
            print("Tesla had the lowest revenue in 2023 with 96773 million USD.")
        elif "net income" in query_lower:
            print("Microsoft had the lowest net income in 2023 with 14974 million USD.")
    elif "revenue" in query_lower:#Revenue Information
        if "tesla"  in query_lower:
            print("Tesla's revenue for the year 2023 was 96773 million USD.")
        elif "apple" in query_lower:
            print("Apple's revenue for the year 2023 was 383285 million USD.")
        elif "microsoft" in query_lower:
            print("Microsoft's revenue for the year 2023 was 211915 million USD.")
        else:
            print("Sorry, I don't have revenue information for that company.")
    elif "net income" in query_lower:#Net  Income Information
        if "tesla" in query_lower:
            print("Tesla's net income for the year 2023 was 72361 million USD.")
        elif "apple" in query_lower:
            print("Apple's net income for the year 2023 was 96995 million USD.")
        elif "microsoft" in query_lower:
            print("Microsoft's net income for the year 2023 was 14974 million USD.")
        else:
            print("Sorry, I don't have net income information for that company.")
    elif "help" in query_lower:#Help Information
        print("Supported queries:\n-Tesla revenue 2023\n-Apple revenue 2023\n-Microsoft revenue 2023\n-Tesla net income 2023\n-Apple net income 2023\n-Microsoft net income 2023\n- Highest revenue in 2023\n- Highest net income in 2023\n- Lowest revenue in 2023\n- Lowest net income in 2023\n- Highest Revenue Growth\n- Highest Net Income Growth\n-Type 'exit' or 'quit' to end the conversation.")
    elif "highest growth" in query_lower:#Growth Information
        if "revenue" in query_lower:
            print("Tesla had the highest revenue growth from 2021 to 2023 with a growth rate of 51.5%.")
        elif "net income" in query_lower:
            print("Tesla had the highest net income growth from 2021 to 2023 with a growth rate of 200.0%.")
    else:
        print("Sorry, I can only answer predefined financial queries.")