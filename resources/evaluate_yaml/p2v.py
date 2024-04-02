import yaml
import json
import os
import fnmatch
import glob

def config(data, frames):
    for t_p in data["target_prompts"]:
        with open(f'/path/to/your/dir/pix2vid_config_{data["video_name"]}_{t_p}.cfg', 'w') as f:
            f.write("[Arguments]")
            f.write("\n")
            f.write(f"noFrames: {frames}")
            f.write("\n")
            f.write(f"org_prompt: {data['source_prompt']}")
            f.write("\n")
            f.write(f"edit_prompt: {t_p}")
            f.write("\n") 
            f.write("W: 512")
            f.write("\n") 
            f.write("H: 512")


def preprcoess_n_edit(data_config, device_num=0): 
    
    with open('/path/to/your/dir/pix2video/pix2vid_runnig_file.py', 'w') as f:
        # Write python code to the file
        f.write("import os")
        f.write("\n")
        f.write("\n")

        for data in data_config:
            for t_p in data["target_prompts"]: 
                f.write(f"os.system('python code/test_cfg.py "
                        f"--config=\"/path/to/your/dir/pix2vid_config_{data['video_name']}_{t_p}.cfg\" "
                        f"--input_path=\"/path/to/your/dir/data/{data['video_name']}\" "
                        f"--device_num={device_num} " 
                        f"--output_path=\"/path/to/your/dir/pix2video/data/{data['video_name']}_output_{t_p}\" "
                        f"--inversion_path=\"/path/to/your/dir/pix2video/data/{data['video_name']}/inversion\"')")
                f.write("\n")
                f.write("\n") 


if __name__ == '__main__':
    with open('/path/to/your/dir/yaml_file.yaml', 'r') as file:
        data_config = yaml.load(file, Loader=yaml.FullLoader)
    
    for data in data_config:
        directory = f'/path/to/your/dir/data/{data["video_name"]}'
        files = glob.glob(os.path.join(directory, 'frame*.png'))
        count = len(files)            
        config(data, count)

    preprcoess_n_edit(data_config, device_num=0)
    
