from flask import Flask, render_template, request
from data import menu

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/options/<food_type>')
def options(food_type):
    food_list = '<h1> List of {} </h1>'.format(food_type)
    food_list += '<ul>'
    food = menu[food_type]
    
    for index, p in enumerate(food):
        food_list += f"<li> <a href=/options/{food_type}/{str(index)}> {p['name']} </a> </li>"
        food_list += '</ul>'
  
    print(food_list)
    return food_list

@app.route('/options/<food_type>/<int:food_id>')
def food(food_type, food_id):
    food = menu[food_type][food_id]
    return f"""
            <h1> {food['name']} </h1>
            <img src={food['url']} alt='alt text'>
            <p> {food['description']} </p>
            <p> {food['type']} </p>
            <p> {food['price']} </p>
            """

@app.route('/form')
def form():
    return  '''
            <form method = "POST" action = "/process">
                <p> Which item would you like? </p>
                <input type = "text" name = "item">
                <br>
                <p> How many orders? </p>
                <input type = "text" name = "quantity">
                <br>
                <input type = "submit" value = "Order">
            '''

@app.route('/process', methods = ['POST'])
def process():
    item = request.form['item']
    quantity = request.form['quantity']

    return '<h1> You purchased {} orders of {}. Happy eating! </h1>'.format(quantity, item)

if __name__ == "__main__":
    app.run(debug = True)