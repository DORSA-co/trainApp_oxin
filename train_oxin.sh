export PATH=/usr/local/cuda-11.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CUDA_HOME=/usr/local/cuda
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

export PYTHONPATH="/home/dorsa/.local/lib/python3.8/site-packages:$PYTHONPATH"
export PATH="/home/dorsa/.local/bin/:$PATH"


cd /Sense_Softwares_Dev/trainApp_oxin

/bin/python3 /Sense_Softwares_Dev/trainApp_oxin/main_UI.py

