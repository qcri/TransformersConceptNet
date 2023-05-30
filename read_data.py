from typing import Dict 
import json 
import argparse 

def load_annotations(path: str) -> Dict: 
    with open(path, "r") as reader: 
        annotations = json.load(reader)
    return annotations 


def main(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-p", "--path", help="path to where the annotations file is stored. This will be one of the files stored under the data directory") 
    parser.add_argument("-l", "--layer", help="layer that we want to get the annotations for") 
    parser.add_argument("-c", "--cluster_id", help="cluster id for which we want to investiate the annotations") 

    args = parser.parse_args()
    path=args.path 
    layer=args.layer
    cluster_id=args.cluster_id

    annotations=load_annotations(path) 

    print(annotations[layer][cluster_id]["label"])
    print(annotations[layer][cluster_id]["words"])

if __name__=="__main__": 
    main()

