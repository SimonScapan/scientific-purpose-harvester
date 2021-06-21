from flask import Flask, request, jsonify, send_from_directory
from harvester_foodpath import get_work_done
from harvester_scholar import get_content

app = Flask(__name__)

def do_foodpath(question):
   df =  get_work_done(question)
   return df.to_html(header="true", table_id="foodpath")

def do_newspaper(question):
   df =  get_it_done(question)
   return df.to_html(header="true", table_id="newspaper")

def do_scholar(question):
    df = get_content(question)
    return df.to_html(header="true", table_id="scholar")


# Path for our main Svelte page
@app.route('/')
def base():
    return send_from_directory('harvester/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('harvester/public', path)

@app.route('/foodpath/<string:question>')
def foodpath(question):
    resultdf = do_foodpath(question)
    result = {"output": resultdf}
    result = {str(key): value for key, value in result.items()}
    return send_from_directory('harvester/foodpath'+question, jsonify(result=result))

@app.route('/scholar/<string:question>', methods=['GET','POST'])
def scholar(question):
    resultdf = do_scholar(question)
    result = {"output": resultdf}
    result = {str(key): value for key, value in result.items()}
    return send_from_directory('harvester/scholar/'+question, jsonify(result=result))

if __name__ == '__main__':
    app.run(debug=True)