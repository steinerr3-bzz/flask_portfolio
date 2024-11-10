from flask import Flask, render_template, request, redirect, url_for
from utils import add_entry, calculate_totals, filter_entries, process_data

app = Flask(__name__)

entries = []

@app.route('/')
def index():
    total_income, total_expenses, balance = calculate_totals(entries)
    return render_template('index.html', entries=entries, income=total_income, expenses=total_expenses, balance=balance)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        entry_type = request.form['type']

        new_entry = add_entry(description, amount, category, entry_type)
        entries.append(new_entry)

        return redirect(url_for('index'))
    return render_template('add_entry.html')

if __name__ == '__main__':
    app.run(debug=True)
