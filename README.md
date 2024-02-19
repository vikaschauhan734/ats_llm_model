# ATS Tester LLM Project

Welcome to the ATS Tester LLM Project! This project aims to assist users in analyzing job descriptions and candidate resumes to optimize their application process. The project is implemented as a Streamlit web application with four main functionalities:

1. **Tell Me About the Resume**: This functionality provides insights into the candidate's resume. It offers a summary or analysis of the resume content, such as key skills, experience, and qualifications.

2. **How Can I Improvise My Skills**: Users can utilize this feature to receive recommendations on how to enhance their skills based on the job description and their resume. This can help candidates tailor their resumes to better fit the desired job requirements.

3. **What Are the Keywords That Are Missing**: This function identifies keywords or skills present in the job description but missing from the candidate's resume. It highlights areas where the candidate may need to improve or update their resume to align with the job requirements.

4. **Percentage Match Resume with Job Description**: This functionality calculates the percentage match between the candidate's resume and the job description. It utilizes the Gemini algorithm to analyze the similarity between the two documents and provides a quantitative measure of their compatibility.

## Getting Started

To run the ATS Tester LLM project locally, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit app by executing the following command:
    ```bash
    streamlit run app.py
    ```
5. Access the web application through your browser at the provided local URL.

## Usage

Once the Streamlit application is running, you can interact with the following buttons to utilize the various functionalities:

- **Tell Me About the Resume**: Click this button to receive insights about the resume.
- **How Can I Improvise My Skills**: Use this button to get recommendations on improving your skills based on the job description.
- **What Are the Keywords That Are Missing**: Click here to identify keywords missing from the resume compared to the job description.
- **Percentage Match Resume with Job Description**: This button triggers the calculation of the percentage match between the resume and the job description.
