from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
tiles = ['GRATIS','Bert Flext','Boner Action','Je Moeder','Mumuh',' Maas Grap','Koen Schreeuwt','Helden van Luskan','Hit Dat?','Inventory Management','XP Farmen','Verkeerd Accent','Glasstaf','Teun Eet','Level Up','Noud Rolt Kut']


def generate_bingo_card():
    random.shuffle(tiles)
    card = []
    for i in range(4):
        column = tiles[i*4:(i+1)*4]
        card.append(column)
    return card

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'bingo_card' not in session:
        session['bingo_card'] = generate_bingo_card()
        session['clicked_buttons'] = []

    if request.method == 'POST':
        clicked_button = request.form['button']
        if clicked_button not in session['clicked_buttons']:
            session['clicked_buttons'].append(clicked_button)
            print(f'Button clicked: {clicked_button}')
    bingo_card = session['bingo_card']
    clicked_buttons = session['clicked_buttons']
    return render_template('index.html', card=bingo_card,clicked_buttons=clicked_buttons)

if __name__ == '__main__':
    app.run(debug=True)
