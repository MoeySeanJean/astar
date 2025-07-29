# Project Setup Guide

Welcome to the project! This README will guide you through setting up the environment and getting the project up and running on your local machine.

## Prerequisites

This project is tested on Ubuntu 24.04.2 LTS with CUDA support. Make sure you have the following installed before proceeding:

- [Git](https://git-scm.com/)
- [Anaconda](https://www.anaconda.com/) for creating a virtual environment

## Setup Instructions

Follow these steps to set up the project:

1. **Create conda environment**
   ```bash
   conda create -n openvlahabitat python=3.9 cmake=3.14.0 -y
   conda activate openvlahabitat
   ```

2. **Install CUDA**
   ```bash
   conda install cuda -c nvidia/label/cuda-12.1.1
   ```

3. **Install PyTorch**
    ```bash
    conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 pytorch-cuda=12.1 -c pytorch -c nvidia
    ```

4. **Install OpenVLA**
    ```bash
    git clone https://github.com/openvla/openvla.git
    cd openvla
    pip install -e .
    pip install packaging ninja
    ninja --version; echo $?  # Verify Ninja --> should return exit code "0"
    pip install "flash-attn==2.5.5" --no-build-isolation
    cd ..
    ```
  
5. **Install Habitat Sim**
    ```bash
    conda install habitat-sim withbullet -c conda-forge -c aihabitat
    ```

6. **Install Habitat Lab**
    ```bash
    git clone --branch stable https://github.com/facebookresearch/habitat-lab.git
    cd habitat-lab
    pip install -e habitat-lab  # install habitat_lab
    pip install -e habitat-baselines  # install habitat_baselines
    cd ..
    ```

## Testing

This section outlines how to run the test suite to ensure everything is working as expected. We use automated tests to maintain code quality and catch bugs early in development.

### 1. Install Test Dependencies

Make sure you have all the development and testing dependencies installed:

```bash
pip install bitsandbytes accelerate==0.25.0 pygame==2.0.1 pybullet==3.0.4
```

### 2. Inference OpenVLA

Test out OpenVLA with local inference:

```bash
python QuickStart.py
```

### 3. Download Habitat Dataset

Make sure you have all the datasets downloaded:

```bash
python -m habitat_sim.utils.datasets_download --uids replica_cad_dataset
python -m habitat_sim.utils.datasets_download --uids hab_fetch
python -m habitat_sim.utils.datasets_download --uids ycb
```

### 4. Test Habitat

Test out habitat environment. Use keys (q,w,e,a,s,d) to control the arm and keys (i,j,k,l) to control the base.

```bash
python Interactive.py --never-end
```

### 5. Test OpenVLA in Habitat

Test out OpenVLA in Habitat. The recorded video is saved to /data/vids.

```bash
python Simulation.py --no-render --save
```

### 6. Generate dataset with OpenVLA in Habitat

To generate 1k+ dataset saved to /data, run the following:

```bash
python Automation.py
```