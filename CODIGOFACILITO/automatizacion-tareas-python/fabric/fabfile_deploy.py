from datetime import datetime
from fabric.api import run, task, env, cd, prefix, sudo, get, local

env.hosts = ['0.0.0.0']
env.user = 'myuser'

DATABASE = 'project_web_facilito'
BACKUP_FOLDER = 'backups/'

def pull():
    run('git pull')

def install_requirements():
    run('pip install -r requirements.txt')

@task
def deploy():
    with cd('python-web'):
        pull()

        with prefix('source env/bin/activate'):
            install_requirements()
        sudo('systemctl restart python-web') # Own service
        sudo('systemctl restart nginx')



## BACKUP cmd

## Format backup filename
def get_backup_name():
    return f'{DATABASE}_{datetime.now().strftime("%d_%m_%Y")}.sql'

def get_backup(backup):
    get(
        remote_path  = backup,
        local_path = BACKUP_FOLDER
    )

def delete_backup(backup):
    sudo(f'rm -rf {backup}')

def load_backup_local(backup_path):
    local(f'mysql -u root -e "DROP DATABASE {DATABASE}"')
    local(f'mysql -u root -e "CREATE DATABASE {DATABASE}"')
    local(f'mysql -u root {DATABASE} < {backup_path}')

def create_backup(backup_name):
    run(f'mysqldump -u muyser {DATABASE} > {backup_name}')

@task
def backup():
    backup_name = get_backup_name()
    backup_path = f'{BACKUP_FOLDER}{backup_name}'
    create_backup(backup_name)
    get_backup(backup_name)
    load_backup_local()
    delete_backup(backup_name)