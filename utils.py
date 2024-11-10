def add_entry(description, amount, category, entry_type):
    return {
        'description': description,
        'amount': amount if entry_type == 'income' else -amount,
        'category': category,
        'type': entry_type
    }

def calculate_totals(entries):
    income = sum(map(lambda e: e['amount'] if e['type'] == 'income' else 0, entries))
    expenses = sum(map(lambda e: e['amount'] if e['type'] == 'expense' else 0, entries))
    balance = income + expenses
    return income, abs(expenses), balance

def filter_entries(entries, entry_type):
    return list(filter(lambda e: e['type'] == entry_type, entries))

def process_data(entries):
    categories = set(entry['category'] for entry in entries)
    category_summary = {category: sum(entry['amount'] for entry in entries if entry['category'] == category) for category in categories}
    return category_summary
