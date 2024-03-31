# ATS Tester LLM Project

Welcome to the ATS Tester LLM Project! This project aims to assist users in analyzing job descriptions and candidate resumes to optimize their application process. The project is implemented as a Flask web application with two main functionalities:

1. **Percentage Match Resume with Job Description**: This functionality calculates the percentage match between the candidate's resume and the job description. It utilizes the Gemini algorithm to analyze the similarity between the two documents and provides a quantitative measure of their compatibility.

2. **What Are the Keywords That Are Missing**: This function identifies keywords or skills present in the job description but missing from the candidate's resume. It highlights areas where the candidate may need to improve or update their resume to align with the job requirements.

## Getting Started

To run the ATS Tester LLM project locally, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask app by executing the following command:
    ```bash
    python app.py
    ```
5. Access the web application through your browser at the provided local URL.
