import time
import torch
from diffusers import StableDiffusionPipeline
from typing import List, Dict, Tuple
import pathlib
from flask import Flask

def inference_loop(pipe, prompt, num_inference_steps, num_images, output_folder, output_type = "pil" ):
    '''
    Loop to run inference
    ''' 
    print(f'Starting inference')
    start = time.time()
    for i in range(num_images):
        output = pipe(prompt,num_inference_steps = num_inference_steps, output_type="pil").images[0]
        t1 = time.strftime("%Y%m%d_%H%M%S")
        save_path = f"{output_folder}/{t1}_SD_image.png"
        pathlib.Path(output_folder).mkdir(parents=True, exist_ok=True)
        img = output.save(save_path)
    end_time = time.time()       
    return output,save_path,start,end_time,

def run_stable_diffusion(
    prompt: str,
    model_id: str = "stabilityai/stable-diffusion-2-1",
    device: str = 'cpu',
    torch_dtype: torch.dtype = torch.float32,
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
    # Create the pipeline
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch_dtype, device=device)
    output,save_path,start,end_time = inference_loop(pipe,prompt,num_inference_steps,num_images,output_folder)
    
    inference_time = (end_time - start) / num_images
    # Return the image URL and the inference time
    return save_path,inference_time

