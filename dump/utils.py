def calculate_summary(transactions):
    income = sum(t['amount'] for t in transactions if t['type'].lower() == 'income')
    expenses = sum(t['amount'] for t in transactions if t['type'].lower() == 'expense')
    balance = income - expenses
    return {"income": income, "expenses": expenses, "balance": balance}
