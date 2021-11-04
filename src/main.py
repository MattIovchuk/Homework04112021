app = Flask(__name__)

@app.route('/')
def homepage():
  
  return render_template("index.html", len = len(worklist), worklist = worklist)

if __name__ == '__main__':
  
  app.run(host='0.0.0.0', port=5000)