# api-simple-microservices

URL: api-thuyldx.com
PORT: 9001

```sh
sudo apt update && sudo apt upgrade -y
```

```sh
sudo apt install docker.io docker-compose
```

```sh
sudo docker login
```

```sh
sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

```sh
sudo apt install python3-venv python3-dev postgresql postgresql-contrib git python3-pip make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl
```

```sh
curl https://pyenv.run | bash
```

```sh
nano ~/.bashrc 
```

```sh
alias docker='sudo docker'
alias docker-compose='sudo docker-compose'
alias build-be='docker run -d -it --name be -p 9001:8000 whiteb3ar99/be:latest'
alias update-be='docker build -t whiteb3ar99/be:latest . && docker rm -f be && docker run -d -it --name be -p 9001:8000 whiteb3ar99/be:latest'
alias push-be='docker push whiteb3ar99/be:latest'
alias pull-be='docker pull whiteb3ar99/be:latest'

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

```sh
source ~/.bashrc 
```

```sh
git clone https://github.com/mercy-thuyle/api-simple-microservices.git
```

```sh
cd api-simple-microservices/be/api
```

```sh
build-be
```