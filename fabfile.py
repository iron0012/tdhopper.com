from fabric.api import *
import fabric.contrib.project as project
import os

S3_PATH = "s3://stiglerdiet.com"

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    todos()
    local('pelican  -o output content -s pelicanconf.py')

def rebuild():
    clean()
    build()

# def regenerate():
#     local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -o output content -s publishconf.py')

def publish():
    todos()
    local('pelican -s publishconf.py content')
    local('s3cmd sync --acl-public --delete-removed output/ %s' % S3_PATH)

def todos():

    done = """
    PELICAN_PAGES=content/pages
    ofexport -o $PELICAN_PAGES/done.md \
        -f flatten \
        -p "((name='Posts to Write') or (name='To Read'))" \
        -I -t "(done='to today')" \
        -T markdown_done_tasks
    echo -n $'Title: Todo \nSlug: todo \nDate: ' > todo_head.txt
    echo $(date +%Y-%m-%d) >> todo_head.txt
    echo $'Author: Tim\n\n This page of blog posts
        I\'d like to write and things I\'d
        like to read is automatically generated from my
        [Omnifocus](http://www.omnigroup.com/products/omnifocus/)
        task list using
        [ofexport](https://github.com/psidnell/ofexport).\n\n' >> todo_head.txt
    ofexport -o $PELICAN_PAGES/todo.md \
        -f flatten \
        -p "((name='Posts to Write') or (name='To Read'))" \
        -E -t "(done='to today')" \
        -T markdown_future_tasks
    cd $PELICAN_PAGES
    cat done.md >> todo.md # Concatenate files
    rm done.md # Remove file"""
    local(done)


