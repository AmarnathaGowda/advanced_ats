from sentence_transformers import SentenceTransformer, util
import torch

# Load the pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_ats_score(resume_text, job_description):
    """
    Compute the ATS score by calculating cosine similarity between
    resume and job description embeddings using Sentence-BERT.
    """
    if not resume_text or not job_description:
        return 0.0  # Return 0 if any of the inputs are empty
    
    # Generate embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    # Compute cosine similarity
    similarity_score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
    
    return round(similarity_score, 2)  # Round to 2 decimal places
