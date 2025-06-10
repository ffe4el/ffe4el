# CUDA 12.1을 지원하는 기본 이미지 선택 (PyTorch 기준) + nvcc 동시설치
FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

# ✅ 기본 필수 패키지 + 빌드 도구 + SSH
RUN apt-get update && apt-get install -y \
    build-essential \
    git wget curl bzip2 ca-certificates sudo \
    libgl1-mesa-dev libxrender1 libsm6 libxext6 ninja-build \
    openssh-server \
    && mkdir /var/run/sshd \
    && echo 'root:root' | chpasswd \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd \
    && systemctl enable ssh || true
    

# Miniconda 설치
ENV CONDA_DIR /opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p $CONDA_DIR && \
    rm miniconda.sh && \
    conda clean -afy




# ✅ base conda 환경에 python + torch 설치
RUN conda install -y python=3.10.13 && \
    pip install --upgrade pip && \
    pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121



# SSH 포트
EXPOSE 22

# ✅ 컨테이너 실행 시 conda + torch + ssh 확인
CMD ["/bin/bash", "-c", "echo 'Checking torch...'; python -c 'import torch; print(\"CUDA available:\", torch.cuda.is_available())'; service ssh start; tail -f /dev/null"]
