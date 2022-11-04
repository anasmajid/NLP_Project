import nltk
import re

def clean_content(content_list):
    cleaned_list=[]
    for content in content_list:
        content=re.sub('#','',content)
        content = re.sub(r'@[^(JohnFetterman)][^(DrOz)]\w+', '', content)
        content = re.sub('@', '', content)
        content = re.sub(r'\\u\w+', '', content)
        content = re.sub(r"http\S+", "", content)
        content = re.sub("\n", "", content)
        cleaned_list.append(content)
        # content = re.sub(r'[^\w\s\.]', '', content)
        # content=' '.join(s for s in content.split() if not any(c.isdigit() for c in s))
        # content=content.lower()
    return cleaned_list