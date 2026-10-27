
# نصب Docker
sudo apt update
sudo apt install -y docker.io docker-compose-v2

# نصب NVIDIA Container Toolkit (برای دسترسی کانتینر به GPU)
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt update
sudo apt install -y nvidia-container-toolkit

# پیکربندی Docker برای استفاده از NVIDIA
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

