from fabric.api import *
import os

S3_PATH = "s3://tdhopper.com"

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican  -o output content -s pelicanconf.py')

def rebuild():
    clean()
    build()

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    build()
    serve()

def publish():
    local('pelican -s publishconf.py content')
    local('s3cmd sync --acl-public --delete-removed output/ %s' % S3_PATH)