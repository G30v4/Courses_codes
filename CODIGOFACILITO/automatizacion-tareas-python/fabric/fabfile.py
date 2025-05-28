from fabric.api import run, sudo, task, put, get, cd, prefix, local, env

## Ejemplo hola mundo
def hola_mundo():
    print('Hola mundo, From G30v4!!')

def bye():
    print('Bye fabric!')

## Ejecucion de comandos  
def show_dir_remote():
    run('ls')

def create_folder_remote():
    run('mkdir example')

## COmandos como superusuario
def delete_folder_remote():
    sudo('rm -rf example')

## Paso de Argumentos
def create_folder_remote_arg(folder):
    run(f'mkdir {folder}')

def delete_folder_remote_arg(folder):
    sudo(f'rm -rf {folder}')

##def pull():
##    print('Obtener todos los cambios de la rama master!')

@task(alias='dp')
def deploy():
    pull()

## Cargar y obtener archivos
@task
def upload_txt_file():
    pull(
        local_path = 'example.txt',
        remote_path = './python-web'
    )

@task
def get_txt_file(file):
    get(
        local_path = './descargas/',
        remote_path = f'./python-web/{file}'
    )

## Cambiar entre directorios
def pull():
    # run('cd python-web && git pull')
    with cd('python-web'):
        run('git pull')

## Ejecución bajo contexto
def install_requirements():
    #run('cd python-web && source env/bin/activate && pip install -r requirements.txt')
    with cd('python-web'):
        with prefix('source env/bin/activate'):
            run('pip install -r requirements.txt')

## Comandos locales
def show_dir():
    local('ls -l')

## Entornos
### ENV
env.hosts = ['0.0.0.0']
env.user = 'myuser'
env.key_file = '~/.ssh/id_rsa.pub'

@task
def pull_env():
    with cd('python-web'):
        run('git pull')