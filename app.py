from dotenv import load_dotenv

load_dotenv()

import re
import base64
from flask import Flask, request, render_template
import os
import io
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        
        first_page = images[0]

        #Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() #encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
input_prompt1 = '''
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of job role Data Science, Big Data Engineering, Data Analyst, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. Give me percentage only.'''

input_prompt2 = '''
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of job role from Data Science, Big Data Engineering, Data Analyst, 
your task is to evaluate the resume against the provided job description. As a Human Resource manager,
 assess the compatibility of the resume with the role. Give me what are the keywords that are missing in the resume in bullet points.'''

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('home.html')
    else:
        job_description = request.form['job_description']
        uploaded_file = request.files['resume_pdf']

        pdf_content = input_pdf_setup(uploaded_file)

        response1 = get_gemini_response(input_prompt1, pdf_content, job_description)
        response1 = re.findall(r'\d+', response1)
        
        response2 = get_gemini_response(input_prompt2, pdf_content, job_description)
        response2 = response2.split('\n')

        return render_template('home.html', result1=response1[0],result2=response2)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)