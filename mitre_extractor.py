import re
from collections import Counter
import requests
import fitz



def extract_technique_text_file(file):
    id_pattern = r'T\d{4}'
    found_ids = []
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        content = content.lower()        
        matches = re.findall(id_pattern, content, re.IGNORECASE)
        found_ids.append(matches)
    return found_ids

def extract_techniques_url(url):
    id_pattern = r'T\d{4}'
    found_ids = []
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text.lower()
        matches = re.findall(id_pattern, content, re.IGNORECASE)
        found_ids.append(matches)
    else:
        return None
    return found_ids

def extract_techniques_pdf(file):
    print(file)
    id_pattern = r'T\d{4}'
    found_ids = []
    pdf_doc = fitz.open(file)
    for page in pdf_doc:
        content = page.get_text()
        matches = re.findall(id_pattern, content, re.IGNORECASE)
        found_ids.append(matches)
    
    return found_ids


if __name__ == "__main__":
    file_path = input("Enter report: ")
    if "http" in file_path:
        extracted_ids = extract_techniques_url(file_path)
    elif ".pdf" in file_path:
        extracted_ids = extract_techniques_pdf(file_path)
    else:
        extracted_ids = extract_technique_text_file(file_path)
    
    counts = Counter(extracted_ids[0])
    sorted_counts = dict(sorted(counts.items(),key=lambda item:item[1],reverse=True))
    total_sum = 0
    total_techniques = len(sorted_counts)
    
    for key,value in sorted_counts.items():
        print(f"Technique ID: {key} Incidence: {value}")
        total_sum = total_sum + value

    print(f"Unique Number of MITRE TEchniques found: {total_techniques}.\nTotal MITRE Techniques found: {total_sum}")