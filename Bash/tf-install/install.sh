curl 'https://raw.githubusercontent.com/Ronterox/Scripts/main/Bash/tf-install/Makefile' > Makefile

curl 'https://raw.githubusercontent.com/Ronterox/Scripts/main/Bash/tf-install/tflow.sh' > tflow.sh && chmod +x tflow.sh

sudo apt install make && make; ./tflow.sh
