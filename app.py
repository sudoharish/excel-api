from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load Excel data
excel_file = "data.xlsx"  # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Define a route to get filtered results
@app.route('/api/data', methods=['GET'])
def get_data():
    filters = request.args  # Get query parameters from the request

    filtered_df = df.copy()

    for key, value in filters.items():
        if key in df.columns:
            filtered_df = filtered_df[filtered_df[key] == value]

    results = filtered_df.to_dict(orient='records')
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
