# TransformersConceptNet
Code and Data Associated with **Can LLMs facilitate interpretation of pre-trained language models?** 

# Data 
The data can be downloaded from the following link [Transformers Concept Net](https://drive.google.com/file/d/17Dc3gDfCTFpM-wOhkao3fi5yMEHPBkGx/view?usp=drive_link)

# Data Description 

We use agglomerative hierarchical clustering over contextualized representations and then annotate these concepts using GPT annotations. Our study involved several 12-layered transformer models, including Bert-cased, RoBERTa, XLNet, and Albert. For more details, please refer to the paper

# Load data 
you can use the __read_data.py__ file to print the words and the label for a latent concept. You can specify the path to data, layer that the concept belongs to, and the concept id.
```
python read_data.py -p $path -l $layer -c $concept_id
```

The output is the list of words along with the chatgpt provided label for the concept
# Load data into display 

You can view the data in a web application by running the __run.sh__ file. 

# Concept probing and Neuron Analysis

We used the NeuroX package to train linear probes and perform neuron analysis. You can view the documentation of the package [here](https://neurox.readthedocs.io/en/latest/index.html)

# Citation

If you used the dataset please cite 

```
@misc{mousi2023llms,
      title={Can LLMs facilitate interpretation of pre-trained language models?}, 
      author={Basel Mousi and Nadir Durrani and Fahim Dalvi},
      year={2023},
      eprint={2305.13386},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
