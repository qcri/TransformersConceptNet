#!/bin/bash
#SBATCH -J app #name of the job
#SBATCH -o run_app.txt

data_path="data/bert-base-cased"
port="8088"
host="0.0.0.0"

python -u app.py -d $data_path -p $port -hs $host 
