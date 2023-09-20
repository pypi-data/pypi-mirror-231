from flask import Flask, render_template

class VastWeb:
    def __init__(self, name=__name__):
        self.app = Flask(name)
        self.app.config['TEMPLATES_AUTO_RELOAD'] = True

    def run(self, host='0.0.0.0', port=5000):
        self.app.run(host=host, port=port)

    def create_default_files(self):
        with open('templates/index.html', 'w') as f:
            f.write('<html><head><title>Welcome to VastWeb</title></head><body><h1>Hello, VastWeb!</h1></body></html>')

        with open('static/style.css', 'w') as f:
            f.write('body { font-family: Arial, sans-serif; }')

# Create an instance of VastWeb
web = VastWeb()

# Define a route for the index page
@web.app.route('/')
def index():
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    web.create_default_files()
    web.run()
