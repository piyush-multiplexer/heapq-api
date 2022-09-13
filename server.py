from flask import Flask, request, jsonify
import heapq

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return {'message': 'Are you sure, whatever you are doing??'}


@app.route('/nlargest', methods=['POST'])
def nlargest():
    data = request.json
    summ_sent = heapq.nlargest(
        data['size'], data['sent_scores'], key=data['sent_scores'].get)
    return jsonify({'data': (''.join(summ_sent))})


if __name__ == '__main__':
    app.run(debug=False)
