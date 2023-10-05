from intel_optimized_stable_diffusion import run_stable_diffusion
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder = 'output_images')

model_optimized = False
# Function to train the model
def optimize_model():
    global model_optimized
    # Optimize model if model_optimized = False
    if model_optimized == False:
        print(f'################################ Starting to training the model ################################')
        run_stable_diffusion("optimize")
        print(f'################################ Training completed ################################')
        model_optimized = True
    return model_optimized

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_image_url = 'https://www.intel.com/content/dam/www/central-libraries/us/en/images/xeon-scalable-processors-family-framed-badge.jpg.rendition.intel.web.480.270.jpg'
    inference_time = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        # Acquire the generated image URL and inference time
        generated_image_url, inference_time = run_stable_diffusion(prompt)
        # Reduce inference_time to two decimal places
        inference_time = round(inference_time, 2)
        print(f'inference_time = {inference_time}')
        
    return render_template('index.html', generated_image_url=generated_image_url, inference_time=inference_time)

if __name__ == '__main__':
    # First run to trigger model optimization using Intel OpenVino Library
    optimize_model()
    # Start the App
    app.run(host='0.0.0.0')
