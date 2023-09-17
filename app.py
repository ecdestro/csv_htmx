from flask import Flask, render_template, request, jsonify
import csv
import io

app = Flask(__name__)

# Define a global variable to store the table data
table_data = []

@app.route('/')
def index():
    return render_template('index.html', table="")

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    global table_data
    csv_file = request.files['csv_file']
    if csv_file:
        # Read the uploaded CSV file and convert it to an HTML table
        csv_data = list(csv.reader(io.StringIO(csv_file.read().decode('utf-8'))))
        table_data = csv_data  # Store the table data globally
        table_html = generate_table_html(table_data)
        return table_html
    else:
        return "No file uploaded."

@app.route('/search', methods=['POST'])
def search():
    global table_data
    search_query = request.form.get('search_query', '').lower()

    if search_query:
        # Filter the table data based on the search query
        filtered_data = [row for row in table_data if any(search_query in str(cell).lower() for cell in row)]
        table_html = generate_table_html(filtered_data)
        return table_html
    else:
        # If no search query is provided, return the full table
        table_html = generate_table_html(table_data)
        return table_html

def generate_table_html(data):
    # Generate an HTML table from the data
    table_html = '<table>'
    for row in data:
        table_html += '<tr>'
        for cell in row:
            table_html += f'<td>{cell}</td>'
        table_html += '</tr>'
    table_html += '</table>'
    return table_html

if __name__ == '__main__':
    app.run(port=80, debug=True)
