from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dummy data (replace this with your product availability data)
    product_availability = {
        'Pablo Ice-Cold XXL': {
            'available': False,
            'remaining': 0,
            'preis':'9',
            'nikotin':'50',
            'geschmack':'Minze',
            'image': 'static/pabloxxl.webp',
        },
        'Iceberg Drachenfrucht': {
            'available': False,
            'remaining': 0,
            'preis':'8',
            'nikotin':'110',
            'geschmack':'Drachenfrucht',
            'image': 'static/dragonfruit.webp',
        },
        'Iceberg Black': {
            'available': True,
            'remaining': 1,
            'preis':'8',
            'nikotin':'150',
            'geschmack':'Obst / Tutti frutti',
            'image': 'static/black.webp',
        },
        'Iceberg Emerald': {
            'available': True,
            'remaining': 1,
            'preis':'8',
            'nikotin':'150',
            'geschmack':'Grüner Apfel und Zitrone',
            'image': 'static/emerald.webp',
        },
        'Iceberg Crazy Mix': {
            'available': False,
            'remaining': 0,
            'preis':'8',
            'nikotin':'150',
            'geschmack':'Mehrfruchtige Zitrusfrüchte',
            'image': 'static/crazymix.webp',
        },
    }
    return render_template('index.html', availability=product_availability)

if __name__ == '__main__':
    app.run()
