from re import escape
from flask import Flask, request, render_template,jsonify

# import our own python functions
from harvester_foodpath import get_work_done
from harvester_scholar import get_content

app = Flask(__name__)

# define the call to Python functions
def do_foodpath(question):
   df = get_work_done(question)
   html = df.to_html(header="true", table_id="foodpath", columns=['Title', 'Content', 'URL'], col_space=['20%','60%','20%'], justify='center', escape=False)
   return html

def do_scholar(question):
    df = get_content(question)
    html = df.to_html(header="true", table_id="foodpath", columns=['Title', 'Content', 'URL'], col_space=['20%','60%','20%'], justify='center', escape=False)
    return html

@app.route('/')
def home():
    return render_template('home.html')

# returns for HTML calls
@app.route('/foodpath', methods=['GET','POST'])
def my_form_post():
    question = request.form['question']             # get question from Form/HTML input
    resultdf = do_foodpath(question)                # call Python Funciton with question
    result = {
        "output": resultdf
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/scholar', methods=['GET','POST'])
def my_form_post2():
    question = request.form['question']             # get question from Form/HTML input
    resultdf = do_scholar(question)                 # call Python Funciton with question
    result = {
        "output": resultdf
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)