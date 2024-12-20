from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Shop

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    products = Shop.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        weight = request.form['weight']
        quantity = request.form['quantity']
        price = request.form['price']
        new_item = Shop(name=name, description=description, weight=weight, quantity=quantity, price=price)
        db.session.add(new_item)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Shop.query.get(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.weight = float(request.form['weight'])
        product.quantity = request.form['quantity']
        product.price = request.form['price']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', product=product)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = Shop.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect('/')

@app.route('/promotion', methods=['GET'])
def promotion():
    return render_template('promotion.html')

if __name__ == '__main__':
    app.run()