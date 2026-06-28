'''1. Creates a DataFrame from this data:'''

import pandas as pd

transactions = [
    {"id": "T001", "amount": 1000, "type": "credit", "country": "US"},
    {"id": "T002", "amount": 200,  "type": "debit",  "country": "UK"},
    {"id": "T003", "amount": 500,  "type": "debit",  "country": "US"},
    {"id": "T004", "amount": 750,  "type": "credit", "country": "IN"},
    {"id": "T005", "amount": 150,  "type": "debit",  "country": "US"},
    {"id": "T006", "amount": 9000, "type": "credit", "country": "IN"},
    {"id": "T007", "amount": 300,  "type": "debit",  "country": "UK"},
    {"id": "T008", "amount": 1200, "type": "credit", "country": "US"}
]
def fraud_detector(transactions):

    df = pd.DataFrame(transactions)

    '''2. Adds a "high_value" column — True if amount > 600'''
    df["high_value"] = df["amount"] > 600
    high_value = df[df["high_value"] == True]

    '''3. Adds a "suspicious" column — True if amount > 5000'''
    suspicious = df["suspicious"] = df["amount"] > 5000

    '''4. Prints total transactions per country'''
    group_country = df.groupby("country")["id"].count()

    '''5. Prints all suspicious transactions'''
    suspicious_tran = df[df["suspicious"]== True]

    '''6. Prints average amount per transaction type'''
    average_amount = (df.groupby("type")["amount"].mean())

    '''7. Prints transactions sorted by amount descending'''
    sorted_values = (df.sort_values("amount", ascending = False))

    return {
        "High Value" : high_value,
        "Suspicious" :  suspicious,
        "Group By Country" : group_country,
        "Suspicious Transactions" : suspicious_tran,
        "Average amount" : average_amount,
        "Sorted values in Asc" : sorted_values
    }

if __name__ == "__main__":
    report = fraud_detector(transactions)
    
    print("--- High Value Transactions ---")
    print(report["High Value"])
    
    print("\n--- Transactions per Country ---")
    print(report["Group By Country"])
    
    print("\n--- Suspicious Transactions ---")
    print(report["Suspicious Transactions"])
    
    print("\n--- Average Amount per Type ---")
    print(report["Average amount"])
    
    print("\n--- Sorted by Amount ---")
    print(report["Sorted values in Asc"])



