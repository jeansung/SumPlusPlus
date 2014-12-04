#Credit to Alejandro Frias
#!/bin/bash


echo "Setting up Sum Plus Plus"

echo "Installing virtualenv"
pip install virtualenv

echo "Creating Python Virtual Environment venv"
virtualenv venv

# Activate virtual environment and install necessary packages
echo "Installing Packages"
source venv/bin/activate
pip install pypeg2
pip install nose
pip install setuptools
pip install xlrd
pip install xlutils
pip install xlwt
