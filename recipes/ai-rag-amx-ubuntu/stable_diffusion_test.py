from optimum.intel import OVStableDiffusionPipeline
import os
import gradio as gr

model_id = "echarlaix/stable-diffusion-v1-5-openvino"
pipeline = OVStableDiffusionPipeline.from_pretrained(model_id)
#prompt = "sailing ship in storm by Rembrandt"
#images = pipeline(prompt).images

#IF TRYING WITH YOUR OWN MODEL:
'''
model_id = "runwayml/stable-diffusion-v1-5"
pipeline = OVStableDiffusionPipeline.from_pretrained(model_id, export=True)
# Don't forget to save the exported model
pipeline.save_pretrained("openvino-sd-v1-5")
'''

batch_size = 1
num_images_per_prompt = 1
height = 512
width = 512
user_input = "frog singing"

# Statically reshape the model
pipeline.reshape(batch_size=batch_size, height=height, width=width, num_images_per_prompt=num_images_per_prompt)
# Compile the model before the first inference
pipeline.compile()

# Run inference
images = pipeline(user_input, height=height, width=width, num_images_per_prompt=num_images_per_prompt).images

def predict(user_input):
    pipeline.reshape(batch_size=batch_size, height=height, width=width, num_images_per_prompt=num_images_per_prompt)
    # Compile the model before the first inference
    pipeline.compile()
    resulting_image = pipeline(user_input, height=height, width=width, num_images_per_prompt=num_images_per_prompt).images
    yield resulting_image


demo = gr.Interface(predict,
                    inputs=gr.Text("frog singing"),
                    outputs="resulting_image")

demo.launch(share=True, server_port=8080)
