from dotenv import load_dotenv
from groq import Groq
load_dotenv()
import re

groq = Groq() 

def classify_with_LLM(log_message): 
    prompt = f'''
        classify the provided log message into one of these tow categories. (1) Workflow error, (2) Deprecation Warning.
        If you couldn't figure out a category, return 'Unclassified'. No need to include think part, only return the category name. 
        No preamble. 
        Log Message: {log_message}
    '''
    chat_comppletion = groq.chat.completions.create(
        model='deepseek-r1-distill-llama-70b',
        temperature=0.5,
        messages=[
            {
                'role': 'user', 
                'content': prompt
            }
        ]
    )
    
    content = chat_comppletion.choices[0].message.content.strip().split()
    match = content[-2:]
    category = 'Unclassified'
    if match: 
        if 'Unclassified' in match: 
            return category
        else: 
            category = ' '.join(match)
    
    return category

if __name__ == '__main__': 
    print(classify_with_LLM(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_LLM(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_LLM("System reboot initiated by user 12345."))