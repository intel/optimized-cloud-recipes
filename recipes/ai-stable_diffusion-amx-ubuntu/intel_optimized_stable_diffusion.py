import time
from optimum.intel import OVStableDiffusionPipeline 
import torch
from diffusers import StableDiffusionPipeline
from typing import List, Dict, Tuple
import pathlib
from flask import Flask

pipe_created = False
pipe = None

# Function to optimize the model and create the Intel OpenVINO Stable Diffusion pipeline
def create_pipe(model_id):
    '''
    Create the pipeline
    '''
    print(
        '''
    		========================================================================
								_       _       _ 
								(_)     | |     | |
								_ _ __ | |_ ___| |
								| | '_ \| __/ _ \ |
								| | | | | ||  __/ |
								|_|_| |_|\__\___|_|
										
		    ========================================================================
        '''
    )
    
    global pipe
    print(f'################################ Optimizing with Intel OpenVino ################################')
    pipe = OVStableDiffusionPipeline.from_pretrained(model_id, export=True)
    print(f'################################ Completed Optimizing with Intel OpenVino ################################')
    
    print(f'################################ Saving model to openvino-sd-v2-1 ################################')
    pipe.save_pretrained("openvino-sd-v2-1")  
    print(f'################################ Completed saving model ################################')  
    
    # Define the shapes related to the inputs and desired outputs
    batch_size, num_images, height, width = 1, 1, 512, 512

    # Statically reshape the model
    pipe.reshape(batch_size, height, width, num_images)
    # Compile the model before inference
    pipe.compile()
    
    
    global pipe_created
    pipe_created = True
    return pipe

# Function to run inference
def inference_loop(pipe, prompt, num_inference_steps, num_images, output_folder, output_type = "pil" ):
    '''
    Loop to run inference
    ''' 
    print(f'################################ Starting inference ################################')
    start = time.time()
    for i in range(num_images):
        output = pipe(prompt,num_inference_steps = num_inference_steps, output_type="pil").images[0]
        t1 = time.strftime("%Y%m%d_%H%M%S")
        save_path = f"{output_folder}/{t1}_SD_image.png"
        pathlib.Path(output_folder).mkdir(parents=True, exist_ok=True)
        img = output.save(save_path)
    end_time = time.time()
    print(f'################################ Completed inference ################################')     
    return output,save_path,start,end_time,

# Main Stable Diffusion function
def run_stable_diffusion(
    prompt: str,
    model_id: str = "stabilityai/stable-diffusion-2-1",
    device: str = 'cpu',
    torch_dtype: torch.dtype = torch.bfloat16,
    num_inference_steps: int = 16,
    num_images: int = 1,
    output_folder: str = 'output_images'
    ):
    '''
    The main function to run stable diffusion. Arguments:
    
    - model_id: The stable diffusion model ID from Hugging Face
    - prompt: A string prompt to build the image
    - device: 'cpu' for an Intel CPU,  'xpu' for an Intel GPU
    - torch_dtype: torch.bfloat16 or torch.float32
    - num_inference_steps: number of noise removal steps
    - num_images: how many images to create
    - output_folder: The local folder to save the images to.
    '''
    #Ony call create_pipe once if pipe_created = False
    global pipe_created
    global pipe
    if pipe_created == False:
        pipe = create_pipe(model_id)
    else:
        print(f'#################### Skipped, pipeline already created ################################')
    
    # Execute inference and create the image
    output,save_path,start,end_time = inference_loop(pipe,prompt,num_inference_steps,num_images,output_folder)
    
    inference_time = (end_time - start) / num_images
    # Return the image URL and the inference time
    return save_path,inference_time

