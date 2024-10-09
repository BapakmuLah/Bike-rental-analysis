Overview
This project focuses on exploring and visualizing data from the bike-sharing-dataset.

Requirements

To run this program , u need install following python framework:
pandas==2.2.2
numpy==1.26.4
matplotlib==3.7.5
seaborn==0.13.2
scipy===1.11.4
pycaret==3.3.2
statsmodels==0.14.2
streamlit==1.39.0
PIL==10.4.0

Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt


Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

Run steamlit app
streamlit run dashboard.py