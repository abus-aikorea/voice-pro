import os
import platform
import site
import subprocess
import sys
import importlib
import time
from pathlib import Path



class OneClick():
    script_dir = os.getcwd()
    
    conda_root_prefix = os.environ.get('CONDA_ROOT_PREFIX', os.path.join(script_dir, "installer_files", "conda"))
    conda_env_path = os.environ.get('INSTALL_ENV_DIR', os.path.join(script_dir, "installer_files", "env"))
    app_model_path = os.path.join(script_dir, "model")
    
    print("Info: Start 1-click ...")
    

    @classmethod
    def is_linux(cls):
        return sys.platform.startswith("linux")

    @classmethod
    def is_windows(cls):
        return sys.platform.startswith("win")

    @classmethod
    def is_macos(cls):
        return sys.platform.startswith("darwin")

    @classmethod
    def is_x86_64(cls):
        return platform.machine() == "x86_64"


    @classmethod
    def torch_version(cls):
        site_packages_path = None
        for sitedir in site.getsitepackages():
            if "site-packages" in sitedir and cls.conda_env_path in sitedir:
                site_packages_path = sitedir
                break

        if site_packages_path:
            torch_version_file = open(os.path.join(site_packages_path, 'torch', 'version.py')).read().splitlines()
            torver = [line for line in torch_version_file if line.startswith('__version__')][0].split('__version__ = ')[1].strip("'")
        else:
            from torch import __version__ as torver

        return torver    

    @classmethod
    def update_pytorch(cls):
        cls.oc_print_big_message("Checking for PyTorch updates")

        # On macOS, PyTorch must be installed via conda (not pip)
        if cls.is_macos():
            # Check if we're using CPU mode (GPU not supported on macOS via conda)
            torver = cls.torch_version()
            if torver:
                print(f"Current PyTorch version: {torver}")
                # Update PyTorch via conda on macOS
                print("Updating PyTorch via conda (required for macOS)...")
                max_retries = 3
                retry_count = 0
                success = False
                while retry_count < max_retries and not success:
                    if retry_count > 0:
                        print(f"Retrying PyTorch update (attempt {retry_count + 1}/{max_retries})...")
                        time.sleep(5)
                    success = cls.oc_run_cmd(f"conda install -y pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 -c pytorch", assert_success=False, environment=True)
                    retry_count += 1
                
                if not success:
                    print("WARNING: Failed to update PyTorch via conda. Continuing anyway...")
                    print("You can try updating manually:")
                    print("  conda install -y pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 -c pytorch")
            else:
                print("PyTorch not found. It will be installed during the installation process.")
        else:
            # For non-macOS systems, use pip
            torver = cls.torch_version()
            is_cuda = '+cu' in torver if torver else False

            if is_cuda:
                install_pytorch = "python -m pip install --upgrade torch==2.5.1+cu124 torchvision==0.20.1+cu124 torchaudio==2.5.1+cu124 --extra-index-url https://download.pytorch.org/whl/cu124"        
            else:
                install_pytorch = "python -m pip install --upgrade torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1"                

            cls.oc_run_cmd(f"{install_pytorch}", assert_success=True, environment=True)


    @classmethod
    def oc_is_installed(cls):
        # Check if key packages are installed to verify installation is complete
        site_packages_path = None
        for sitedir in site.getsitepackages():
            if "site-packages" in sitedir and cls.conda_env_path in sitedir:
                site_packages_path = sitedir
                break

        if site_packages_path:
            # Check if at least torch and a couple other key packages exist
            torch_exists = os.path.isfile(os.path.join(site_packages_path, 'torch', '__init__.py'))
            json5_exists = os.path.isfile(os.path.join(site_packages_path, 'json5', '__init__.py'))
            gradio_exists = os.path.isfile(os.path.join(site_packages_path, 'gradio', '__init__.py'))
            
            # If packages don't exist, definitely not installed
            if not (torch_exists and json5_exists and gradio_exists):
                return False
            
            # Additional check: Try to actually import torch to verify it works
            # This catches cases where torch is installed but broken
            try:
                # Use a clean environment to test import
                test_cmd = 'python -c "import sys; sys.path.insert(0, \'\'); import torch; assert hasattr(torch, \'_C\') or hasattr(torch, \'__version__\')"'
                return cls.oc_run_cmd(test_cmd, environment=True, capture_output=True)
            except:
                # If import test fails, assume not properly installed
                return False
        else:
            # If environment doesn't exist, definitely not installed
            return False

    @classmethod
    def oc_check_env(cls):
        # If we have access to conda, we are probably in an environment
        conda_exist = cls.oc_run_cmd("conda", environment=True, capture_output=True)
        if not conda_exist:
            print("Error: Conda is not installed. Exiting...")
            sys.exit(1)

        # Ensure this is a new environment and not the base environment
        if os.environ.get("CONDA_DEFAULT_ENV") == "base":
            print("Error: Create an environment for this project and activate it. Exiting...")
            sys.exit(1)
            
        # Workaround for llama-cpp-python loading paths in CUDA env vars even if they do not exist
        conda_path_bin = os.path.join(cls.conda_env_path, "bin")
        if not os.path.exists(conda_path_bin):
            os.makedirs(conda_path_bin, exist_ok=True)
        
        # Check if we're in a PyTorch source directory (can cause import issues)
        current_dir = os.getcwd()
        torch_source_dir = os.path.join(current_dir, "torch")
        if os.path.exists(torch_source_dir) and os.path.exists(os.path.join(torch_source_dir, "_C")):
            print("=" * 70)
            print("WARNING: PyTorch source directory detected in current path!")
            print(f"Current directory: {current_dir}")
            print(f"Found: {torch_source_dir}")
            print("This can cause PyTorch import errors.")
            print("=" * 70)
            print("Solution options:")
            print("1. Remove or rename the 'torch' directory in the current path")
            print("2. Run the script from a different directory")
            print("=" * 70)
            
        # Ensure PYTHONPATH doesn't interfere with installed packages
        # Clear any torch-related paths that might cause conflicts
        pythonpath = os.environ.get('PYTHONPATH', '')
        if pythonpath:
            paths = pythonpath.split(os.pathsep)
            filtered_paths = [p for p in paths if not os.path.exists(os.path.join(p, 'torch', '_C'))]
            if len(filtered_paths) != len(paths):
                print("Warning: Removed PyTorch source paths from PYTHONPATH to avoid conflicts")
                os.environ['PYTHONPATH'] = os.pathsep.join(filtered_paths) if filtered_paths else ''          
              

    @classmethod
    def clear_cache(cls):
        print("clear_cache?? no...")
        # oc_run_cmd("conda clean -a -y", environment=True)
        # oc_run_cmd("python -m pip cache purge", environment=True)


    @classmethod
    def oc_print_big_message(cls, message):
        message = message.strip()
        lines = message.split('\n')
        print("\n\n*******************************************************************")
        for line in lines:
            print("*", line)

        print("*******************************************************************\n\n")

        
    @classmethod        
    def oc_run_cmd(cls, cmd, assert_success=False, environment=False, capture_output=False, env=None):
        # Use the conda environment
        if environment:
            if cls.is_windows():
                conda_bat_path = os.path.join(cls.conda_root_prefix, "condabin", "conda.bat")
                if not os.path.exists(conda_bat_path):
                    print(f"Warning: Conda batch file not found at {conda_bat_path}")
                    return False
                    
                cmd = f'"{conda_bat_path}" activate "{cls.conda_env_path}" >nul && {cmd}'
            else:
                conda_sh_path = os.path.join(cls.conda_root_prefix, "etc", "profile.d", "conda.sh")
                if not os.path.exists(conda_sh_path):
                    print(f"Warning: Conda shell script not found at {conda_sh_path}")
                    return False
                    
                cmd = f'. "{conda_sh_path}" && conda activate "{cls.conda_env_path}" && {cmd}'

        # Run shell commands
        try:
            result = subprocess.run(cmd, shell=True, capture_output=capture_output, env=env)

            # Assert the command ran successfully
            if assert_success and result.returncode != 0:
                print(f"Command '{cmd}' failed with exit status code '{str(result.returncode)}'.\n\nExiting now.\nTry running the start/update script again.")
                sys.exit(1)

            return result.returncode == 0
        except Exception as e:
            print(f"Command: '{cmd}' failed with {e}")
            return False    


    @classmethod
    def get_user_choice(cls, question, options_dict):
        print()
        print(question)
        print()

        for key, value in options_dict.items():
            print(f"{key}) {value}")

        print()

        choice = input("Input> ").upper()
        while choice not in options_dict.keys():
            print("Invalid choice. Please try again.")
            choice = input("Input> ").upper()

        return choice


    @classmethod
    def oc_install_webui(cls, app_name: str, is_update = False):
        # Ask the user for the GPU vendor
        if "GPU_CHOICE" in os.environ:
            choice = os.environ["GPU_CHOICE"].upper()
            cls.oc_print_big_message(f"Selected GPU choice \"{choice}\" based on the GPU_CHOICE environment variable.")
        else:
            choice = cls.get_user_choice(
                "What is your GPU?",
                {
                    'G': 'NVIDIA GTX, RTX, Tesla',
                    # 'B': 'Intel Arc (IPEX)',
                    'C': 'CPU (I want to run models in CPU mode)'
                },
            )

        gpu_choice_to_name = {
            "G": "NVIDIA",
            # "B": "INTEL",
            "C": "CPU"
        }

        selected_gpu = gpu_choice_to_name[choice]
        
        # pip 버전이 24.1 이상인 경우, 
        # omegaconf 를 시작으로 fairseq 0.12.2, hydra-core 1.0.7  설치 문제가 발생하기 때문에
        # pip 버전을 24.0 으로 설정함.
        # oc_run_cmd("python -m pip install pip==24.0", assert_success=True, environment=True)    
        cls.oc_run_cmd("python -m pip install pip==25.0", assert_success=True, environment=True)
        
        # conda package
        cls.install_conda_packages(app_name, selected_gpu)
        
        if is_update:
            cls.update_pytorch()

        # Install the webui requirements
        cls.install_requirements(app_name, is_update, selected_gpu)    

        # cudnn & onnxruntime
        # install_cudnn()
        # install_onnxruntime()
        
        # Final verification: Ensure PyTorch works correctly
        if cls.is_macos() and selected_gpu == 'CPU':
            cls.oc_print_big_message("Final PyTorch verification")
            verify_cmd = 'python -c "import torch; assert hasattr(torch, \'_C\'), \'PyTorch C extensions not found\'; print(f\'PyTorch {torch.__version__} verified successfully\')"'
            if not cls.oc_run_cmd(verify_cmd, environment=True):
                print("Warning: PyTorch verification failed. The installation may have issues.")
                print("You may need to reinstall PyTorch manually:")
                print("  conda remove -y pytorch torchvision torchaudio")
                print("  conda install -y pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 -c pytorch")
        
        cls.clear_cache()  
    
    
    @classmethod
    def check_package_installed(cls, package_name):
        try:
            importlib.import_module(package_name)
            return True
        except ImportError:
            return False    
    
    @classmethod   
    def install_requirements(cls, app_name, is_update=False, selected_gpu='NVIDIA'): 
        requirements_file = f'requirements-{app_name}-gpu.txt' if selected_gpu=="NVIDIA" else f'requirements-{app_name}-cpu.txt'
        cls.oc_print_big_message(f"Install/Update webui requirements from file: {requirements_file}")
        
        # openai-whisper (and some other sdists) import pkg_resources during build.
        # Recent setuptools versions (>=80) have removed pkg_resources, so downgrade
        # to a known-compatible version before installing requirements.
        cls.oc_print_big_message("Ensuring compatible setuptools for legacy builds")
        cls.oc_run_cmd('python -m pip install "setuptools<70" wheel', assert_success=False, environment=True)
        
        # openai-whisper is only available as sdist and its setup.py imports pkg_resources.
        # Even with compatible setuptools in the main env, pip's isolated build environment
        # may pull in a newer setuptools that lacks pkg_resources. Build without isolation
        # so the main env's setuptools is used.
        whisper_pkg = "openai-whisper==20240930"
        cls.oc_print_big_message(f"Pre-installing {whisper_pkg} without build isolation")
        cls.oc_run_cmd(f"python -m pip install --no-build-isolation {whisper_pkg}", assert_success=False, environment=True)
        
        cmd = f"python -m pip install -r {requirements_file}"
        cmd = cmd + " --upgrade" if is_update else cmd
        cls.oc_run_cmd(cmd, assert_success=True, environment=True)
        
        # Fix: ctranslate2 bundles a renamed cuDNN 8 library but omits the split
        # .so files (e.g. libcudnn_ops_infer.so.8) that it dlopen's at runtime.
        # Extract the missing libs from the official cuDNN 8 wheel so CUDA ops work.
        cls.oc_print_big_message("Checking ctranslate2 cuDNN 8 library compatibility")
        fix_script = """import os, site, subprocess, sys, zipfile, glob, shutil
sp = next((p for p in site.getsitepackages() if sys.prefix in p), None)
libs = os.path.join(sp, "ctranslate2.libs") if sp else ""
needed = os.path.join(libs, "libcudnn_ops_infer.so.8") if libs else ""
if libs and os.path.isdir(libs) and not os.path.exists(needed):
    print("ctranslate2 cuDNN 8 split libs missing - extracting...")
    os.makedirs("/tmp/cudnn8_fix", exist_ok=True)
    subprocess.check_output([sys.executable, "-m", "pip", "download", "--no-deps", "-d", "/tmp/cudnn8_fix", "nvidia-cudnn-cu12==8.9.7.29"])
    whl_path = glob.glob("/tmp/cudnn8_fix/nvidia_cudnn_cu12-8.9.7.29*.whl")[0]
    with zipfile.ZipFile(whl_path, "r") as z:
        for name in ["nvidia/cudnn/lib/libcudnn.so.8", "nvidia/cudnn/lib/libcudnn_ops_infer.so.8", "nvidia/cudnn/lib/libcudnn_cnn_infer.so.8", "nvidia/cudnn/lib/libcudnn_adv_infer.so.8"]:
            z.extract(name, "/tmp/cudnn8_fix")
            src = os.path.join("/tmp/cudnn8_fix", name)
            dst = os.path.join(libs, os.path.basename(name))
            shutil.move(src, dst)
    print("cuDNN 8 split libs installed in", libs)
else:
    print("ctranslate2 cuDNN 8 libs OK or not applicable")
"""
        fix_script_path = "/tmp/fix_cudnn8.py"
        with open(fix_script_path, "w") as f:
            f.write(fix_script)
        cls.oc_run_cmd(f'python "{fix_script_path}"', assert_success=False, environment=True)
        
        # Install PyTorch via pip for non-macOS systems (CPU builds)
        # On macOS, PyTorch is installed via conda in install_conda_packages
        if not cls.is_macos() and selected_gpu == 'CPU':
            if not cls.check_package_installed('torch'):
                cls.oc_print_big_message("Installing PyTorch via pip")
                cls.oc_run_cmd(f"python -m pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1", assert_success=True, environment=True)


    @classmethod
    def install_conda_packages(cls, app_name, selected_gpu='NVIDIA'):
        # Configure conda channels first (recommended by Anaconda documentation)
        # Reference: https://www.anaconda.com/docs/getting-started/miniconda/install#macos-2
        cls.oc_print_big_message("Configuring conda channels")
        
        # Add conda-forge channel (idempotent operation)
        # The command will fail if channel already exists, which is fine
        print("Adding conda-forge channel...")
        cls.oc_run_cmd("conda config --add channels conda-forge 2>&1 | grep -v 'already exists' || true", environment=True)
        
        # Set channel priority to flexible (allows packages from multiple channels)
        # This is recommended for better package resolution
        print("Setting channel priority to flexible...")
        cls.oc_run_cmd("conda config --set channel_priority flexible", environment=True)
        
        # Verify channel configuration
        print("Verifying channel configuration...")
        cls.oc_run_cmd("conda config --show channels", environment=True)
        
        if app_name in ["gulliver", "voice"]:
            if cls.check_package_installed('pynini') == False:
                cls.oc_print_big_message("Installing pynini from conda-forge")
                # Retry logic for network issues
                max_retries = 3
                retry_count = 0
                success = False
                while retry_count < max_retries and not success:
                    if retry_count > 0:
                        print(f"Retrying pynini installation (attempt {retry_count + 1}/{max_retries})...")
                        time.sleep(5)  # Wait before retry
                    
                    # Try installing with explicit channel specification
                    # Use --strict-channel-priority to ensure we get from conda-forge
                    success = cls.oc_run_cmd(f"conda install -y -c conda-forge --strict-channel-priority pynini==2.1.5", assert_success=False, environment=True)
                    
                    if not success:
                        # Try without strict priority (more flexible)
                        print("Trying with flexible channel priority...")
                        success = cls.oc_run_cmd(f"conda install -y -c conda-forge pynini==2.1.5", assert_success=False, environment=True)
                    
                    if not success:
                        # Try alternative: use defaults channel as fallback
                        print("Trying alternative installation method (defaults channel)...")
                        success = cls.oc_run_cmd(f"conda install -y pynini==2.1.5", assert_success=False, environment=True)
                    
                    retry_count += 1
                
                if not success:
                    print("ERROR: Failed to install pynini after multiple attempts.")
                    print("This may be due to network issues. Please check your internet connection.")
                    print("You can try installing manually:")
                    print("  conda install -y -c conda-forge pynini==2.1.5")
                    sys.exit(1)
        
        # Install PyTorch via conda on macOS (CPU builds only)
        # PyTorch 2.5.1 is not available via pip on macOS, must use conda
        if cls.is_macos() and selected_gpu == 'CPU':
            if not cls.check_package_installed('torch'):
                cls.oc_print_big_message("Installing PyTorch via conda (required for macOS)")
                # Retry logic for network issues
                max_retries = 3
                retry_count = 0
                success = False
                while retry_count < max_retries and not success:
                    if retry_count > 0:
                        print(f"Retrying PyTorch installation (attempt {retry_count + 1}/{max_retries})...")
                        time.sleep(5)  # Wait before retry
                    
                    success = cls.oc_run_cmd(f"conda install -y pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 -c pytorch", assert_success=False, environment=True)
                    retry_count += 1
                
                if not success:
                    print("ERROR: Failed to install PyTorch after multiple attempts.")
                    print("This may be due to network issues. Please check your internet connection.")
                    print("You can try installing manually:")
                    print("  conda install -y pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 -c pytorch")
                    sys.exit(1)
                
                # Verify PyTorch installation works (with clean environment)
                cls.oc_print_big_message("Verifying PyTorch installation")
                # Clear PYTHONPATH to avoid source directory conflicts
                verify_cmd = 'PYTHONPATH= python -c "import torch; print(f\'PyTorch {torch.__version__} installed successfully\')"'
                if not cls.oc_run_cmd(verify_cmd, environment=True):
                    cls.oc_print_big_message("PyTorch installation verification failed. Reinstalling...")
                    # Remove and reinstall
                    cls.oc_run_cmd(f"conda remove -y pytorch torchvision torchaudio", environment=True)
                    cls.oc_run_cmd(f"conda install -y pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 -c pytorch", assert_success=True, environment=True)
                    # Verify again
                    if not cls.oc_run_cmd(verify_cmd, environment=True):
                        print("Warning: PyTorch installation may have issues. Continuing anyway...")
                
        # Install ninja and git with retry logic
        print("Installing ninja and git...")
        max_retries = 3
        retry_count = 0
        success = False
        while retry_count < max_retries and not success:
            if retry_count > 0:
                print(f"Retrying ninja/git installation (attempt {retry_count + 1}/{max_retries})...")
                time.sleep(5)
            success = cls.oc_run_cmd(f"conda install -y -k ninja git", assert_success=False, environment=True)
            retry_count += 1
        
        if not success:
            print("WARNING: Failed to install ninja/git. Continuing anyway...")
        
        # Remove nomkl and install mkl
        # nomkl may not be installed, so don't fail if it's not found
        print("Removing nomkl (if present)...")
        cls.oc_run_cmd(f'conda remove --force --yes nomkl 2>&1 || true', environment=True)
        
        # Install mkl with retry logic
        max_retries = 3
        retry_count = 0
        success = False
        while retry_count < max_retries and not success:
            if retry_count > 0:
                print(f"Retrying mkl installation (attempt {retry_count + 1}/{max_retries})...")
                time.sleep(5)
            success = cls.oc_run_cmd(f'conda install --yes mkl -c anaconda', assert_success=False, environment=True)
            retry_count += 1
        
        if not success:
            print("WARNING: Failed to install mkl. Continuing anyway...")    
        
        

    @classmethod                    
    def launch_webui(cls, app_file):
        print("Start the program...")
        cls.oc_run_cmd(f"python {app_file}", environment=True) 

