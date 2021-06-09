from flask import Flask, request, render_template,jsonify
from harvester import get_work_done

app = Flask(__name__)

def do_something(question):
   df =  get_work_done(question)
   return df.to_html(header="true", table_id="table")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    question = request.form['question']
    resultdf = do_something(question)
    result = {
        "output": resultdf
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)