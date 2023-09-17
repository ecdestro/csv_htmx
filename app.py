from flask import Flask, render_template
import csv
import io

app = Flask(__name__)

@app.route('/')
def index():
    with open('data.csv', newline=' ') as csvfile:
        csv_data = list(csv.reader(csvfile))
        table_html= '<table>'
        for row in csv_data:
            table_html += '<tr>'
            for cell in row:
                table_html += f'<td>{cell}</td>'
            table_html += '</tr>'
        table_html += '</table>'

    return render_template('index.html', table=table_html)

if __name__ == '__main__':
    app.run(port=80, debug=True)