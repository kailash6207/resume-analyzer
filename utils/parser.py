import re

def extract_email(text):
    email = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    return email[0] if email else "Not Found"

def extract_phone(text):
    # Matches common phone number formats
    phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    return phone[0] if phone else "Not Found"

def extract_skills(text):
    # Expanded database to catch specialized engineering and software skills
    skills_db = [
        'python', 'c', 'c++', 'c/c++', 'java', 'javascript', 'html', 'css', 'sql',
        'vlsi', 'vlsi design', 'cmos', 'sram', 'matlab', 'streamlit',
        'machine learning', 'computer vision', 'data analysis', 'git', 'linux',
        'microcontrollers', '8051', '8086', 'dsp', 'digital signal processing',
        'robotics', 'kinematics', 'wiener filtering', 'random processes'
    ]
    
    found_skills = set() # Using a set prevents duplicate entries
    text_lower = text.lower()
    
    for skill in skills_db:
        # We use a custom boundary check (?<![a-z0-9]) instead of \b 
        # so that it safely detects symbols like '+' or '/' in C++
        pattern = r'(?<![a-z0-9])' + re.escape(skill) + r'(?![a-z0-9])'
        
        if re.search(pattern, text_lower):
            # Keep the formatting clean for the UI
            if skill == 'c/c++':
                found_skills.add('C/C++')
            elif skill == 'c++':
                found_skills.add('C++')
            elif skill == 'vlsi':
                found_skills.add('VLSI')
            elif skill == 'cmos':
                found_skills.add('CMOS')
            elif skill == 'dsp':
                found_skills.add('DSP')
            else:
                found_skills.add(skill.title())
            
    return sorted(list(found_skills))