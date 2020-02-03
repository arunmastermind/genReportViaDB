import pandas as pd
from pymongo import MongoClient
from flask import Flask, render_template, jsonify
from bson import json_util, ObjectId
import json

app = Flask(__name__)

def getQueryData():
    client = MongoClient('mongodb://onega:27017')
    db = client.AutoRedGreen
    collection = db.QUERY
    data = pd.DataFrame(list(collection.find()))
    return data

@app.route('/', methods=['GET','POST'])
def test():
    data = getQueryData()
    data['output'] = data['output'].str.slice(0, 300)
    # del data['_id']
    # return data.to_html(header="true", table_id="table")
    # return render_template('table.html',  tables=[data.to_html(classes='data')], titles=data.columns.values)
    # return render_template('table.html', row_data=list(data.values.tolist()), titles=data.columns.values)
    # return data.to_json(orient='records', lines=True)
    # return jsonify(data)
    # return data.to_dict(orient='index')
    page_sanitized = json_util.dumps(data.to_dict(orient='index'))
    return page_sanitized

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2020)
