import os
# 1. Force Windows to completely ignore symlinks
os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

print("Loading AI Model (Downloading directly to your project folder)...")
# 2. Force the model to download locally into a new folder called 'ai_brain'
model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='./ai_brain')
print("AI Brain loaded and ready!")

def match_skills(resume_skills, target_skills=None):
    # Fallback to default skills if no JD is provided
    if target_skills is None:
        target_skills = ['Python', 'Matlab', 'Git', 'Vlsi', 'Sql']

    matched_skills = []
    
    # Clean up the target skills
    clean_targets = [t.strip() for t in target_skills if t.strip()]

    # If the resume is empty or there are no targets, fail gracefully
    if not clean_targets or not resume_skills:
        return {'matched': [], 'match_count': 0, 'total_target': len(clean_targets)}

    # 2. CONVERT WORDS TO VECTORS (The Magic)
    target_embeddings = model.encode(clean_targets)
    resume_embeddings = model.encode(resume_skills)

    # 3. CALCULATE DISTANCE (Cosine Similarity)
    # This creates a grid comparing every target skill against every resume skill
    similarity_matrix = cosine_similarity(target_embeddings, resume_embeddings)

    for i, target in enumerate(clean_targets):
        # Find the single highest match score for this specific target
        best_score = np.max(similarity_matrix[i])
        
        # Cosine similarity is scored from -1 to 1. 
        # 0.55 is a highly tuned threshold for this specific AI model to catch synonyms!
        if best_score >= 0.35:
            matched_skills.append(target.title())

    # Remove duplicates and sort
    matched_skills = sorted(list(set(matched_skills)))

    return {
        'matched': matched_skills,
        'match_count': len(matched_skills),
        'total_target': len(clean_targets)
    }

def calculate_score(extracted_data, match_data):
    # 1. Base Score for having contact info (Max 20 points)
    base_score = 0
    if extracted_data.get('email') and extracted_data.get('email') != "Not Found": 
        base_score += 10
    if extracted_data.get('phone') and extracted_data.get('phone') != "Not Found": 
        base_score += 10
    
    # 2. THE KNOCKOUT PARAMETER 
    if match_data['total_target'] > 0 and match_data['match_count'] == 0:
        return 10 

    # 3. Calculate the skill score (Max 80 points)
    if match_data['total_target'] > 0:
        skill_score = (match_data['match_count'] / match_data['total_target']) * 80
    else:
        skill_score = 50 
        
    return int(base_score + skill_score)