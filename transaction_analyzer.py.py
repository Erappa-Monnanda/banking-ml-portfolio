transactions = [
    {"id": "T001", "amount": 1000, "type": "credit"},
    {"id": "T002", "amount": 200,  "type": "debit"},
    {"id": "T003", "amount": 500,  "type": "debit"},
    {"id": "T004", "amount": 750,  "type": "credit"},
    {"id": "T005", "amount": 150,  "type": "debit"}
]

def transaction_analyser(transactions):
    amounts = [t["amount"] for t in transactions]
    credit_amounts = [t["amount"] for t in transactions
                                    if t["type"] == "credit"]
    Ids_600 = [t["id"] for t in transactions
                        if t["amount"] > 600]
    
    total_credit = 0
    total_debit = 0
    highest_transaction = transactions[0]
    total = 0
    
    for t in transactions:
        if t["type"] == "credit":
            total_credit += t["amount"]
        else:
            total_debit += t["amount"]
        
        if t["amount"] > highest_transaction["amount"]:
            highest_transaction = t

        total += t["amount"]

    total_counts = len(transactions)
    average_tran = total / total_counts

    above_average = [t for t in transactions
                                        if t["amount"] > average_tran]

    debit_ids = [t["id"] for t in transactions
                            if t["type"] == "debit"]
    
    summary = f"Processed {total_counts} transactions. Credits: {total_credit}, Debits: {total_debit}"

    return{
        "All amounts" : amounts,
        "Credit amounts" : credit_amounts,
        "Flag" : Ids_600,
        "Total Credit" : total_credit,
        "Total Debit" : total_debit,
        "Highest transaction" : highest_transaction,
        "Total" : total,
        "Average amount" : average_tran,
        "Debit IDs" : debit_ids,
        "Above Average" : above_average,
        "Summary": summary
    }
        

if __name__ == "__main__":
    report = transaction_analyser(transactions)
    print("All amounts:", report["All amounts"])
    print("Credit amounts:", report["Credit amounts"])
    print("Flagged IDs:", report["Flag"])
    print("Total Credit:", report["Total Credit"])
    print("Total Debit:", report["Total Debit"])
    print("Highest:", report["Highest transaction"])
    print("Average:", report["Average amount"])
    print("Debit IDs: ", report["Debit IDs"])
    print("Above Average: ", report["Above Average"])
    print("Summary", report["Summary"])