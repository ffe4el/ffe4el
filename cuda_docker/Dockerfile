# docker build -t chacorp/diff3f:latest .
FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update

RUN pip install jupyterlab ipywidgets
### setup for vessl path
RUN ln -s /opt/conda/bin/jupyter /usr/local/bin/jupyter

# Install sshd
RUN apt-get install -y -q openssh-server libsqlite3-dev

# ### ETC
RUN apt-get install -y tmux htop
RUN pip install nvitop


RUN pip install xformers==0.0.22.post7
# RUN pip install torch==2.1.0 xformers --index-url https://download.pytorch.org/whl/cu121
RUN apt-get install -y --no-install-recommends \
        software-properties-common build-essential git wget curl cmake libeigen3-dev ffmpeg libsm6 libxext6
# RUN apt-get install -y --no-install-recommends python3-dev python3-pip 

COPY cpp_extension.py /opt/conda/lib/python3.10/site-packages/torch/utils/cpp_extension.py
# RUN pip install "git+https://github.com/facebookresearch/pytorch3d.git@v0.7.6"
RUN pip install fvcore iopath \
    && git clone https://github.com/facebookresearch/pytorch3d.git \
    && cd pytorch3d \
    && pip install -e .
RUN conda init bash \
    && . ~/.bashrc \
    && conda install -y -c conda-forge -c matplotlib numpy scikit-learn scipy meshplot \
    && python -m ipykernel install --user --name=base \
    && pip install --upgrade diffusers==0.21.4 einops huggingface-hub meshio opencv-python plyfile transformers trimesh potpourri3d robust_laplacian accelerate \
    && pip install cupy==13.4.0 \
        libigl==2.5.1 \
        open3d==0.19.0 \
        openmesh==1.2.1 \
        k3d==2.16.1 \
        PyOpenGL==3.1.0 \
        pyrender==0.1.45 \
        transforms3d==0.4.2 \
        easydict==1.13 \
        tensorboard==2.19.0 \
        setuptools==69.5.1 \
    && pip install torch_cluster torch_scatter torch_sparse -f https://data.pyg.org/whl/torch-2.1.0+cu121.html --no-cache-dir
# docker push chacorp/diff3f:latest
# docker image tag chacorp/diff3f:latest chacorp/diff3f:0.1.250318
