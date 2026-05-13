def calculate_score(extracted_data, match_data):
    score = 0
    
    # 20 points for having contact info
    if extracted_data.get('email') != "Not Found":
        score += 10
    if extracted_data.get('phone') != "Not Found":
        score += 10
        
    # Up to 40 points for having skills listed (5 points per skill)
    skills = extracted_data.get('skills', [])
    score += min(40, len(skills) * 5)
    
    # Up to 40 points for matching target skills
    matched_skills = match_data.get('matched', [])
    score += min(40, len(matched_skills) * 10)
    
    return score