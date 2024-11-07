import argparse
import os
import sys
import shutil
from pathlib import Path
from one_click import *


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python start-abus.py <app_name>")
        sys.exit(1)

    app_name = sys.argv[1]
    print(f"app_name: {app_name}")
    
        
    # check start-appname.py    
    python_filename = f'start-{app_name}.py'
    if not os.path.exists(python_filename):
        print(f"File not found - {python_filename}")
        sys.exit(1)
            
   
    
    check_env()

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--update-wizard', action='store_true', help='Launch a menu with update options.')
    args, _ = parser.parse_known_args()


    if not is_installed():
        install_webui(app_name)
        os.chdir(script_dir)

    if os.environ.get("LAUNCH_AFTER_INSTALL", "").lower() in ("no", "n", "false", "0", "f", "off"):
        print_big_message("Will now exit due to LAUNCH_AFTER_INSTALL.")
        sys.exit()
        
    # Workaround for llama-cpp-python loading paths in CUDA env vars even if they do not exist
    conda_path_bin = os.path.join(conda_env_path, "bin")
    if not os.path.exists(conda_path_bin):
        os.makedirs(conda_path_bin, exist_ok=True)

    # ABUS - start Gulliver
    print("Start the program...")
    run_cmd(f"python {python_filename}", environment=True) 
    
