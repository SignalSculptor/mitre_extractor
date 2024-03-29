import re
from collections import Counter
import requests
import fitz
import argparse
import sys



def extract_technique_text_file(file: str, pattern: str) -> list:
    found_ids = []
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        content = content.lower()        
        matches = re.findall(pattern, content, re.IGNORECASE)
        found_ids.append(matches)
    return found_ids

def extract_techniques_url(url:str, pattern: str) -> list:
    found_ids = []
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text.lower()
        matches = re.findall(pattern, content, re.IGNORECASE)
        found_ids.append(matches)
    else:
        return None
    return found_ids

def extract_techniques_pdf(file:str, pattern:str) -> list:
    found_ids = []
    pdf_doc = fitz.open(file)
    for page in pdf_doc:
        content = page.get_text()
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            found_ids.append(matches)
    return found_ids

def resolution_pattern(resolution:str) -> str:
    if resolution == "st":
        return r'(T\d{4}\.\d{3})'
    else:
        return r'T\d{4}'
    
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script Inputs")
    parser.add_argument("--text", help="Provide path for text based file to extract techniques")
    parser.add_argument("--url", help="Provide URL for web based report to extract techniques")
    parser.add_argument("--pdf", help="Provide path for PDF file to extract techniques")
    parser.add_argument("--res", default="t", help="The desired technique resolution technique (t), sub-technique (st). Defaults to t")
    args = parser.parse_args()


    pattern = resolution_pattern(args.res)
    
    if args.url:
        extracted_ids = extract_techniques_url(args.url, pattern)
    elif args.pdf:
        extracted_ids = extract_techniques_pdf(args.pdf, pattern)
    elif args.text:
        extracted_ids = extract_technique_text_file(args.text,pattern)
    else:
        print("No valid arguments provided. Please use --text, --url, or --pdf.")
        sys.exit(1)
    
    try:
        counts = Counter(extracted_ids[0])
        sorted_counts = dict(sorted(counts.items(),key=lambda item:item[1],reverse=True))
        total_sum = 0
        total_techniques = len(sorted_counts)
        
        
        for key,value in sorted_counts.items():
            print(f"Technique ID: {key.ljust(10)} Incidence: {str(value).ljust(4)}")
            total_sum = total_sum + value

        print(f"Unique Number of MITRE ATTCK Techniques found: {total_techniques}.\nTotal Instances of MITRE ATTCK Techniques found: {total_sum}")
    except IndexError as e:
        print(f"Error: {e}. This likely means that no results were found.")