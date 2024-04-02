import yaml
import json
import os
import fnmatch

def config(data, frames, device_num=0, sd='2.1'):
    
    tf_config = {
            # general
            'seed': 1,
            'device': f'cuda:{device_num}',
            'output_path_original': 'tokenflow-results',
            'output_path': '',

            # data
            'data_path': f'./data/{data["video_name"]}',
            'latents_path': 'latents', 
            'n_inversion_steps': 500, 
            'n_frames': frames, 

            # diffusion
            'sd_version': sd,
            'guidance_scale': 7.5,
            'n_timesteps': 50,
            'prompts': data["target_prompts"],
            'prompt': "",
            'negative_prompt': "ugly, blurry, low res, unrealistic, unaesthetic",
            'batch_size': 8,

            # pnp params -- injection thresholds ∈ [0, 1]
            'pnp_attn_t': 0.5,
            'pnp_f_t': 0.8,
    }
    
    with open(f'/path/to/your/dir/tf_config_{data["video_name"]}.yaml', 'w') as file:
        yaml.dump(tf_config, file)


def preprcoess_n_edit(data_config, frames, device_num=0, sd='2.1'):
    
    with open('/path/to/your/dir/tf_runnig_file.py', 'w') as f:
        # Write python code to the file
        f.write("import os")
        f.write("\n")
        f.write("\n")

        for i, data in enumerate(data_config):       
            # Preprocess
            # device is hardcodedd in preprocess.py
            f.write("# Preprocess")
            f.write("\n")
            f.write(f"os.system('python preprocess.py --data_path \"/path/to/your/dir/{data['video_name']}.mp4\" "
                f"--inversion_prompt \"{data['source_prompt']}\" "
                f"--sd_version {sd} "
                f"--save_dir \"./latents\" --n_frames {frames[i]}')")
            f.write("\n")
            f.write("\n")   
            # Edit
            f.write("# Edit")
            f.write("\n")
            f.write(f"os.system('python run_tokenflow_pnp.py "
                    f"--config_path \"./tf_confs/tf_config_{data['video_name']}.yaml\"')")
            f.write("\n")
            f.write("\n")   

if __name__ == '__main__':
    with open('/path/to/your/dir/yaml_file.yaml', 'r') as file:
        data_config = yaml.load(file, Loader=yaml.FullLoader)
    frame_count_list = []
    for data in data_config:
        directory = f'/path/to/your/dir/{data["video_name"]}'
        count = 0
        for root, dirs, files in os.walk(directory):
            for file in files:
                if fnmatch.fnmatch(file, '*.png'):
                    count += 1
            frame_count_list.append(count)
            break  
  
        # for data in data_config:
        config(data, count, 0, sd='2.1')

    preprcoess_n_edit(data_config, frame_count_list, device_num=0, sd='2.1')
    
