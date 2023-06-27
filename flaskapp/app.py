from flask import Flask, request, render_template, redirect, url_for, session
from pyrad.client import Client
from pyrad.dictionary import Dictionary
from pyrad import packet

app = Flask(__name__)

# Configure RADIUS server details
RADIUS_SERVER = '172.17.0.2'
RADIUS_SECRET = b'not_so_radius_secret'
dictionary = Dictionary("dictionary")
# Configure Flask secret key for session
app.secret_key = 'your_secret_key'


def authenticate(username, password):
    client = Client(server=RADIUS_SERVER, authport=1812, secret=RADIUS_SECRET, dict=dictionary)
    client.timeout = 3

    # Create an Access-Request packet
    req = client.CreateAuthPacket(code=packet.AccessRequest)
    req['User-Name'] = username
    req['User-Password'] = password

    # Send the packet to the RADIUS server
    reply = client.SendPacket(req)

    # Check if the authentication was successful
    if reply.code == packet.AccessAccept:
        return True

    return False



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate(username, password):
            # Authentication successful
            # Store the username in the session
            session['username'] = username
            return redirect(url_for('home'))
        else:
            # Authentication failed
            error_message = "Invalid username or password"
            return render_template('login.html', error=error_message)

    # GET request, render the login form
    return render_template('login.html')


@app.route('/home')
def home():
    # Check if the user is authenticated
    if 'username' in session:
        username = session['username']
        return render_template('home.html', username=username)

    # User is not authenticated, redirect to login page
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Remove the username from the session
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
