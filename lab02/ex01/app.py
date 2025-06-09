from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

# router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# router routes for Caesar cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# CaesarCipher
@app.route("/encrypt_caesar", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainTextCaesar']
    key = int(request.form['inputKeyPlainCaesar'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/decrypt_caesar", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherTextCaesar']
    key = int(request.form['inputKeyCipherCaesar'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

# router routes for Vigenere cipher
@app.route("/vigenere")
def vegenere():
    return render_template('vigenere.html')

@app.route("/encrypt_vegenere", methods=['POST'])
def vegenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)   # gọi đúng method
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt_vegenere", methods=['POST'])
def vegenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)   # gọi đúng method
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# RailFenceCipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/encrypt_railfence", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    if key <= 1 or key >= len(text):
        return f"<b style='color:red;'>Error:</b> Key must be > 1 and < length of the text.<br>Text length = {len(text)}, key = {key}"
    
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}"

@app.route("/decrypt_railfence", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}"


# Playfair
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/create_matrix_playfair", methods=['POST'])
def create_matrix():
    key = request.form['matrixKey']
    playfair = PlayfairCipher()
    matrix = playfair.create_playfair_matrix(key)
    # Chuyển matrix thành chuỗi dễ đọc để trả về
    matrix_str = "<br>".join([" ".join(row) for row in matrix])
    return f"<b>Matrix for key '{key}':</b><br>{matrix_str}"

@app.route("/encrypt_playfair", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayfairCipher()
    encrypted_text = playfair.playfair_encrypt(text, key)   # gọi đúng method
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt_playfair", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayfairCipher()
    decrypted_text = playfair.playfair_decrypt(text, key)   # gọi đúng method
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
