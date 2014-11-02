#!/bin/bash
source ~/.bashrc
cd ~/repos/stigler-diet
workon stiglerdiet

git pull --rebase
fab build
fab publish
