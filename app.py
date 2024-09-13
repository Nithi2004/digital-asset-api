from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

# Home route to render the front-end HTML
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate and return random crypto values based on user input
@app.route('/crypto', methods=['GET'])
def get_crypto_values():
    asset = request.args.get('asset').upper()  # Convert to uppercase for consistency

    if asset == 'BTC':
        # Generate random float values for Bitcoin
        bitcoin_price = round(random.uniform(50000, 60000), 2)
        bitcoin_volume = round(random.uniform(18, 30), 2)
        crypto_data = {
            'digital_asset': 'BTC',
            'digital_asset_name': 'Bitcoin',
            'digital_asset_price': bitcoin_price,
            'digital_asset_next_24_hour_volume(in B)': bitcoin_volume
        }
        return jsonify(crypto_data)
    
    elif asset == 'ETH':
        # Generate random float values for Ethereum
        ethereum_price = round(random.uniform(2000, 3000), 2)
        ethereum_volume = round(random.uniform(9, 13), 2)
        crypto_data = {
            'digital_asset': 'ETH',
            'digital_asset_name': 'Ethereum',
            'digital_asset_price': ethereum_price,
            'digital_asset_next_24_hour_volume(in B)': ethereum_volume
        }
        return jsonify(crypto_data)
    
    else:
        return jsonify({'error': 'Invalid asset! Use BTC or ETH.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
