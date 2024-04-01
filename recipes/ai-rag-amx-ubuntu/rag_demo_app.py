# Intel® Corporation Copyright
# Contributors: William Fowler

from rag_demo import prep_model, run_rag, RAGBot
from flask import Flask, render_template, request, session

app = Flask(__name__)

model_ready = False
bot = RAGBot()

# Prepare the model on the first load
def int_load_model():
    global model_ready

    if not model_ready:
        model = 'Falcon'
        dataset = 'robot maintenance'
        top_k = 2
        #useRag = False
        print("Loading model...")
        model_ready = prep_model(model,dataset,top_k)
        #model_ready = True
    return model_ready

@app.route('/', methods=['GET','POST'])
def index():
    global model_ready
    global bot
    print("Starting Index route...")
    if request.method == 'GET':
        print("Starting GET method for load model...")
       # model_ready = int_load_model()
        return render_template('index.html', model_ready=model_ready)
    elif request.method == 'POST':
        print("Starting POST method for load model...")
        print("Loading model...")
        model = request.form['model']
        dataset = request.form['dataset']
        top_k = request.form['top-k-slider']
        # useRag = request.form['useRag']
        print("Got variables from form: ", model, dataset, top_k)
        model_ready, bot = prep_model(model, dataset, top_k)
        return render_template('index.html', model_ready=model_ready,bot=bot)


# App route for Query
@app.route('/query', methods=['POST'])
def handle_query():
    global bot
    print("Asking question...")
    # Get the question from the form
    question = request.form['prompt']
    try:
        result = run_rag(question,bot)
    except ValueError as e:
            result = str(e)
    return render_template('index.html', model_ready=True, result=result, question=question)
    

if __name__ == '__main__':
    # Load the model before starting the app
#    int_load_model()
    # Start the app
    app.run(host='0.0.0.0', debug=True, port=8080)
