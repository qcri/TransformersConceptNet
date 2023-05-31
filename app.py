from flask import Flask, redirect, render_template, request, url_for

from collections import Counter
import argparse 
from read_data import load_annotations

app = Flask(__name__) 


@app.route("/")
def index(): 
   return redirect(url_for("get_cluster", cluster_id=0, layer_id=0, model="bert")) 

@app.route('/cluster/<layer_id>/<cluster_id>', methods = ['GET'])
def get_cluster(layer_id, cluster_id):

    words = DATA[layer_id][cluster_id]["words"] 
    label = DATA[layer_id][cluster_id]["label"]

    word_frequencies = Counter(words) 

    return render_template("display.html", word_frequencies=word_frequencies)


def main(): 

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data_path", help="paht to where the data is stored")
    parser.add_argument("-p", "--port", help="port used to run the app")
    parser.add_argument("-h", "--host", help="host used to run the app")
    args=parser.parse_args()
    
    data_path = args.data_path
    PORT=args.port
    HOST=args.host

    DATA=load_annotations(data_path)
    app.run(host=HOST, debug=True, port= PORT)


if __name__=="__main__": 
    main() 