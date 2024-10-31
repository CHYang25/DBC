# Installation Guide - Mujoco setup

After following the setup steps in [README.md](./README.md), continue the following steps:

1. Carla (version 0.9.8)
    - Change Directory and add the Carla directory
        ```
        cd ~
        mkdir CARLA_0.9.8
        cd CARLA_0.9.8
        ```
    - Download the following zip files. They should be unzipped within the same directory.
        ```
        wget https://tiny.carla.org/carla-0-9-8-linux
        wget https://tiny.carla.org/additional-maps-0-9-8-linux
        ```
    - Unzip the tar.gz files
        ```
        tar -xvf carla-0-9-8-linux
        tar -xvf additional-maps-0-9-8-linux
        ```
    - Add the following environment variables (remember to change the username):
        ```
        export PYTHONPATH=$PYTHONPATH:/home/chyang/CARLA_0.9.8/PythonAPI
        export PYTHONPATH=$PYTHONPATH:/home/chyang/CARLA_0.9.8/PythonAPI/carla
        export PYTHONPATH=$PYTHONPATH:/home/chyang/CARLA_0.9.8/PythonAPI/carla/dist/carla-0.9.8-py3.5-linux-x86_64.egg
        ```
    - Install the following extra libraries
        ```
        pip install pygame
        pip install networkx
        pip install dotmap
        ```
    - Testing
        - Open a new terminal session, and run the CARLA simulator:
            ```
            bash CarlaUE4.sh -fps 20
            ```
        - In a second terminal window, run
            ```
            ./PythonAPI/util/config.py --map Town03 --delta-seconds 0.05
            ```

2. Flow (install from github)
    - Clone the repo
        ```
        git clone https://github.com/flow-project/flow.git
        cd flow
        ```
    - Install dependencies 
        ```
        pip install -e .
        ```
    - Since there's no setup bash for ubuntu 20.04, so we're doing it manually
        ```
        git clone https://github.com/eclipse/sumo.git
        cd sumo
        ```
    - Install needed pacakges in conda (though the documentation recommended not to do so)
        **install cmake as well, so that the cmake in conda can find the depnedent packages in conda**
        **just intall the latest libgdal, and it'll automatically install other dependent packages**
        **if you can't install some package of another version, remove the original version first**
        **remember to remove the ./build directory when you want to rebuild**
        ```
        conda install anaconda::cmake
        conda install conda-forge::fox
        conda install conda-forge::libgdal=3.9.2
        conda install conda-forge/label/cf202003::gl2ps
        conda install conda-forge/label/cf202003::openjdk
        conda install conda-forge/label/cf202003::maven
        conda install omnia::eigen3
        conda install conda-forge::fmt=11.0.1
        
        pip install -r tools/requirements.txt -r tools/req_dev.txt
        pip install -U pip setuptools   
        pip3 install --upgrade sumolib
        ```
    - Decalre SUMO_HOME env variable
        ```
        export SUMO_HOME=/home/chyang/sumo
        ```
    - Cmake to build sumo
        ```
        cmake -B build .
        cmake --build build -j$(nproc)
        ```

3. mjrl
    ```
    git clone https://github.com/aravindr93/mjrl.git
    cd mjrl
    pip install -e .
    ```
4. dm_control
    ```
    pip install dm-control
    ```
5. upgrade six
    ```
    pip install --upgrade six
    ```
5. Final few env variable setups:
    ```
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/chyang/.mujoco/mujoco210/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
    ```

## References
[Carla Installation Instruction](https://github.com/Farama-Foundation/d4rl/wiki/CARLA-Setup)
[Carla Zip file download](https://github.com/carla-simulator/carla/releases/tag/0.9.8/)
[Sumo Installation Guides](https://flow.readthedocs.io/en/latest/flow_setup.html#optional-direct-install-of-sumo-from-github)
[Sumo Build Guide](https://sumo.dlr.de/docs/Installing/Linux_Build.html)
https://anaconda.org/conda-forge/xerces-c
https://anaconda.org/conda-forge/fox
https://anaconda.org/anaconda/proj
https://anaconda.org/conda-forge/libgdal
https://anaconda.org/conda-forge/gl2ps/
https://anaconda.org/conda-forge/openjdk
https://anaconda.org/conda-forge/maven
https://anaconda.org/omnia/eigen3
https://anaconda.org/conda-forge/fmt
https://proj.org/en/9.5/development/reference/functions.html