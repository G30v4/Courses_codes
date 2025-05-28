import scp
import time
import paramiko
from getpass import getpass
import paramiko.ssh_exception

HOST = '0.0.0.0'
USER = 'myuser'

if __name__ == '__main__':
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        password = getpass('Ingresa tu contrasema SSH')
        client.connect(HOST, username=USER, password=password)

        ## Uso de SFTP
        sftp_client = client.open_sftp()

        ### Upload files
        sftp_client.put(
            'my-file.txt', # Source - local
            'my-dir/myfile.txt' # Target - remote
        )

        ### Download files
        sftp_client.get(
            'my-dir/myfile.txt', # Source - remote
            'download/myfile.txt' # target - local
        )

        ## Uso de SCP
        scp_client = scp.SCPClient(client.get_transport())

        ### Upload files - SCP
        scp_client.put(
            'my-file.txt', # Source - local
            'my-dir/' # Target - remote
        )

        ### Download files - SCP
        scp_client.get(
            'my-dir/myfile.txt', # Source - remote
            'download/' # target - local
        )


        # Ejemplo basico
        ''' 
        stdin, stout, stderr = client.exec_command('ls')
        time.sleep(1)
        result = stout.read().decode()
        print(result)
        '''
        
        # Uso de Canales - 'se ejecuta una unica vez'
        session = client.get_transport().open_session()
        if session.active:
            session.exec_command('cd my-dir && ls -l')
            result = session.recv(1024).decode()
            print(result)

        # Comandos con superuser
        session_sudo = client.get_transport().open_session()
        if session_sudo.active:
            session_sudo.set_combine_stderr(True)
            session_sudo.get_pty() # pedir contraseña
            
            #session_sudo.exec_command('sudo ls -l')
            #stdin = session_sudo.makefile('wb')

            # Alternativas
            session_sudo.exec_command(f'echo {password} | sudo -S ls -l')

            stdout = session_sudo.makefile('rb')
            #stdin.write(password + '\n')
            result = stdout.read().decode()
            print(result)
        
        sftp_client.close()
        scp_client.close()
        client.close()
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Autenticacion fallida")