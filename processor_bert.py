import joblib
from sentence_transformers import SentenceTransformer 
import numpy as np

# load the sentence transformer model to compute log message embeddings 
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

# load the saved logistic regression log classifier model 
classifier_model = joblib.load('/home/madhuka/ML/NLP/Repos/Hybrid-Log-Classification-/models/log_classifier.joblib')

# bert classification function 
def classify_with_bert(log_message): 
    # generate embeddings for the log message
    embeddings = transformer_model.encode(log_message)
    
    # get the probabilities from the classifier model so we can mark the lower probability results as unclassified
    probabilities = classifier_model.predict_proba([embeddings])[0]
    max_prob = np.max(probabilities)
    
    if max_prob < 0.5: 
        return 'Unclassified'
    
    # perform classification using the loaded model 
    result = classifier_model.predict([embeddings])[0] 
    
    # return the predicted class 
    return result

if __name__ == '__main__': 
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer",
        "IP 192.168.133.114 blocked due to potential attack"
    ]
        
    for log in logs: 
        label = classify_with_bert(log)
        print(f'{log} --> {label}')