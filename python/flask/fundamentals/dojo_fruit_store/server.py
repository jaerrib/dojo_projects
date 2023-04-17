from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['GET', 'POST'])         
def checkout():
    print(request.form)
    data = request.form
    date_time = datetime.now().strftime("%B %d, %Y at %l:%M:%S %p") 
    num_items = int(data["strawberry"]) + int(data["raspberry"]) + int(data["apple"])
    print(f"Charging {data['first_name']} {data['last_name']} for {num_items} fruits")
    return render_template("checkout.html", data=data, num_items=num_items, date_time=date_time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    