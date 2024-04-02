import yaml
import json
import os
import fnmatch

def config(data, frames):
        
    for t_p in data["target_prompts"]:
        t_p_underscore = t_p.replace(" ", "_")
        rerender_config = {
            "input":  f'/path/to/your/dir/{data["video_name"]}.mp4',
            "output": f'/path/to/your/dir/{data["video_name"]}/{t_p_underscore}/blend.mp4',
            "work_dir": f'/path/to/your/dir/{data["video_name"]}/{t_p_underscore}',
            "key_subdir": "keys",
            "frame_count": frames,
            "interval": 10,
            "prompt": t_p,
            "x0_strength": 0.75,
            "control_type": "canny",
            "canny_low": 50,
            "canny_high": 100,
            "control_strength": 0.7,
            "seed": 0,
            "warp_period": [
                0,
                0.1
            ],
            "ada_period": [
                1,
                1
            ],
            "image_resolution": 512
        }
        with open(f'/path/to/your/dir/re_config_{data["video_name"]}_{t_p}.json', 'w') as file:
            json.dump(rerender_config, file)
            
def preprcoess_n_edit(data_config): 
    with open('/path/to/your/dir/rerender_runnig_file.py', 'w') as f:
        # Write python code to the file
        f.write("import os")
        f.write("\n")
        f.write("\n")

        for data in data_config: 
            for t_p in data["target_prompts"]:      
                # device is hardcodedd
                f.write("os.system('python rerender.py "
                       f"--cfg \"/path/to/your/dir/yaml_files/re_config_{data['video_name']}_{t_p}.json\" -one -nb')")
                f.write("\n")
                f.write("os.system('python rerender.py "
                       f"--cfg \"/path/to/your/dir/yaml_files/re_config_{data['video_name']}_{t_p}.json\" -nb')")
                f.write("\n")
                f.write("os.system('python rerender.py "
                       f"--cfg \"/path/to/your/dir/yaml_files/re_config_{data['video_name']}_{t_p}.json\" -nr')")
                f.write("\n")
                f.write("\n")   

if __name__ == '__main__':
    with open('/path/to/your/dir/yaml_file.yaml', 'r') as file:
        data_config = yaml.load(file, Loader=yaml.FullLoader)
    
    for data in data_config:
        directory = f'/path/to/your/dirdata/{data["video_name"]}'
        count = 0
        for root, dirs, files in os.walk(directory):
            for file in files:
                if fnmatch.fnmatch(file, '*.png'):
                    count += 1
            break  
        
    # for data in data_config:
        config(data, count)
        print(f'data:{data}, frames:{count}')
    
    preprcoess_n_edit(data_config)
    
