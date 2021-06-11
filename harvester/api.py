from flask import Flask, request, render_template,jsonify
from harvester_foodpath import get_work_done
from harvester_newspap3r import get_it_done

app = Flask(__name__)

def do_foodpath(question):
   df =  get_work_done(question)
   return df.to_html(header="true", table_id="foodpath")

def do_newspaper(question):
   df =  get_it_done(question)
   return df.to_html(header="true", table_id="newspaper")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/foodpath', methods=['GET','POST'])
def my_form_post():
    question = request.form['question']
    resultdf = do_foodpath(question)
    result = {
        "output": resultdf
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

app.route('/newspaper', methods=['GET','POST'])
def my_form_post():
    question = request.form['question']
    resultdf = do_newspaper(question)
    result = {
        "output": resultdf
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)