# Comandos utiles

## Instalaciónde fabric

```bash
# Crear entorno de python
python -m venv env
# Activar entorno de python
source env/bin/activate
# Instalar dependencia
pip install fabric3
# Craer archivo por defecto de fabric
touch fabfile.py
```

## Ejecutar fabric desde la terminal
```bash
# Listar comandos disponibles
fab -l
# Ejecutar comando
fab hola_mundo
# Ejecutar comando con banderas
fab -H 0.0.0.0 show_dir_remote --user=muyser
# Ejecutar comandos con argumentos
fab -H 0.0.0.0 create_folder_remote_arg:folder=myfolder --user=muyser
```

## Conexión a un equipo remoto

```bash
ssh usuario@direccion_ip
```

## Conexión a un equipo remoto mediante llaves

```bash
# verificar si existe llave
cat ~/.ssh/id_rsa.pub 
# crear llave
ssh-keygen -t rsa -b 4096
# copiar llave a host remoto
ssh-copy-id usuario@direccion_ip
```
## Configuracion servidor SSH '+' Seguridad

```bash
# Editar archivo de configuración
sudo nano /etc/ssh/sshd_config

# PArametros a configurar
-> PasswordAuthentication no
-> AuthenticationMethods publickey

# Reinicar servicio
sudo service ssh restart
```

## Conexión a múltiples equipos

```bash
# Acceder a la ruta de las claves ssh
cd ~/.ssh
# Editar archivo de configuración
nano config

# Parametros a configurar
"""
Host nuestro_alias
Hostname direccion_ip
User usuario
PubKeyAuthentication yes
IdentityFile ~/.ssh/id_rsa
"""
# Reinicar servicio
sudo service ssh restart 
```

## Instalaciónde paramiko $ scp
```bash
# Crear entorno de python
python -m venv env
# Activar entorno de python
source env/bin/activate
# Instalar dependencia
pip install paramiko scp
# Craer archivo por defecto de fabric
touch paramiko.py
```

## Ejecutar paramiko desde la terminal
```bash
# Listar comandos disponibles
python paramiko.py
```

## Recursos
- [Generar llaves Publica - Privada](https://www.youtube.com/watch?v=OAhLWoB9Ekw)
- [SFTP - Paramiko](http://docs.paramiko.org/en/stable/api/sftp.html)