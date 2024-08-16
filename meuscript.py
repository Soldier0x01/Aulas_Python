import sys 
import subprocess

if len(sys.argv) < 2: 
    print("Você deve fornecer um nome para o ambiente virtual.")
    sys.exit()
    
env_name = sys.argv[1]

subprocess.run(["python", "-m", "venv", env_name])
subprocess.run([env_name + "/bin/pip", "install", "numpy"])

print("Ambiente virtual criado com sucesso e biblioteca numpy instalada")