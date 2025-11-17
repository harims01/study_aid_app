from diffusers import DiffusionPipeline
import torch
from diffusers.utils import export_to_video

def generate_video(prompt):
    pipe = DiffusionPipeline.from_pretrained("THUDM/CogVideoX-2B", torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    frames = pipe(prompt, num_frames=48).frames
    output_path = "generated_video.mp4"
    export_to_video(frames, output_path)
    return output_path
