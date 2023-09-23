
how_to = '''
# just add this 1 line.
import VicksTor 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
'''

print(how_to)
