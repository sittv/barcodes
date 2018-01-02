from barcodes.baseapp import app
from barcodes.bookiebot import bookiebot as bookiebot_bp
from barcodes.checkout_return import checkout_return as checkout_return_bp


app.register_blueprint(bookiebot_bp)
app.register_blueprint(checkout_return_bp)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)