from dotenv import load_dotenv

load_dotenv()

import base64
from flask import Flask, request, render_template
import os, sys, io, re
from PIL import Image
import pdf2image
import google.generativeai as genai

# Check if the GOOGLE_API_KEY is provided via command line argument
if len(sys.argv) < 2:
    print("Please provide the Google API key as a command line argument.")
    sys.exit(1)

# Extract the API key from command line argument
google_api_key = sys.argv[1]

genai.configure(api_key=google_api_key)

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert pdf to images
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        
        # Determine the dimensions of the combined image
        max_width = max(image.width for image in images)
        total_height = sum(image.height for image in images)
        
        # Create a new blank image to hold the combined pages
        combined_image = Image.new('RGB', (max_width, total_height))
        
        # Paste each page onto the combined image
        current_y = 0
        for image in images:
            combined_image.paste(image, (0, current_y))
            current_y += image.height
        
        # Save the combined image as bytes
        combined_image_bytes = io.BytesIO()
        combined_image.save(combined_image_bytes, format='JPEG')
        combined_image_bytes.seek(0)
        
        # Encode combined image to base64
        combined_image_base64 = base64.b64encode(combined_image_bytes.getvalue()).decode()
        
        pdf_parts = [{
            "mime_type": "image/jpeg",
            "data": combined_image_base64
        }]
        
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