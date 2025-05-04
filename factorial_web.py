from flask import Flask, request, render_template_string
import xmlrpc.client

app = Flask(__name__)

# Connect to the existing XML-RPC factorial server
factorial_server = xmlrpc.client.ServerProxy("http://localhost:8000/")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        number = request.form.get('number')
        try:
            result = factorial_server.factorial(number)
        except Exception as e:
            error = str(e)
    return render_template_string('''
        <h1>Factorial Calculator</h1>
        <form method="post">
            <input type="text" name="number" placeholder="Enter an integer" required>
            <input type="submit" value="Calculate">
        </form>
        {% if result is not none %}
            <p>Factorial result: {{ result }}</p>
        {% endif %}
        {% if error %}
            <p style="color:red;">Error: {{ error }}</p>
        {% endif %}
    ''', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
