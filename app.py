from flask import Flask, render_template, request
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/products.html', methods=['POST'])
def products():
	search_response = request.form['search_response']
	return render_template('products.html', search_response=search_response)


if __name__ == '__main__':
    app.run(debug=True)