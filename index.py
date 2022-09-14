from flask import Flask, request, jsonify, render_template
import heapq

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/nlargest', methods=['POST'])
def nlargest():
    data = request.json
    summ_sent = heapq.nlargest(
        data['size'], data['sent_scores'], key=data['sent_scores'].get)
    return jsonify({'data': (''.join(summ_sent))})


if __name__ == '__main__':
    app.run(debug=True)
