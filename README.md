
```
# QuLab Earnings Call Transcript Summarizer

## Description

The QuLab Earnings Call Transcript Summarizer is a Streamlit application designed to analyze earnings call transcripts using Natural Language Processing (NLP) techniques. This application allows users to quickly gain insights from lengthy transcripts by providing:

- **Text Summarization:**  Generates a concise summary of the earnings call transcript, highlighting the most important information.
- **Topic Extraction:**  Identifies and visualizes the key topics discussed in the transcript using topic modeling.

This tool is inspired by the concepts discussed in QuantUniversity's "AI and Big Data in Investments" course, Module 4, demonstrating practical applications of NLP in finance and investment analysis. It's designed to be user-friendly and provides interactive visualizations to enhance understanding of the extracted information.

## Installation

To run this Streamlit application, you need to have Python installed on your system along with the required libraries. Follow these steps to set up your environment:

1. **Prerequisites:**
    - Python 3.8 or higher is recommended. You can download Python from [python.org](https://www.python.org/).
    - Ensure you have `pip` installed (Python package installer).

2. **Clone the repository (Optional):**
    If you have access to the application code in a repository, clone it to your local machine. If you only have the Python script, proceed to the next step.

    ```bash
    git clone [repository_url]
    cd [repository_directory]
    ```

3. **Create a virtual environment (Recommended):**
    It's good practice to create a virtual environment to manage dependencies for your project.

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install required libraries:**
    Install the necessary Python libraries using `pip`.  Make sure you are in the virtual environment if you created one.

    ```bash
    pip install streamlit transformers gensim plotly
    ```
    This command will install:
    - `streamlit`: For creating the web application.
    - `transformers`: For using pre-trained models for text summarization.
    - `gensim`: For topic modeling.
    - `plotly`: For interactive visualizations.

## Usage

1. **Run the Streamlit application:**
    Navigate to the directory containing the Python script (e.g., `app.py`) in your terminal and run the Streamlit app using the following command:

    ```bash
    streamlit run app.py
    ```

2. **Access the application in your browser:**
    Streamlit will provide a local URL (usually `http://localhost:8501` or `http://your_network_ip:8501`) in your terminal. Open this URL in your web browser to access the application.

3. **Input Earnings Call Transcript:**
    The application provides three input methods:
    - **Direct Text Input:** Paste the transcript text directly into the text area provided.
    - **File Upload:** Upload a transcript file in TXT format.
    - **URL Input (Simplified - Paste Text from URL):**  Copy the transcript text from a URL and paste it into the text area.  (Note: This application does not automatically fetch content from URLs; you need to copy and paste the text.)

    Choose your preferred input method and provide the transcript text.

4. **View Generated Summary:**
    Once the transcript text is provided, the application will process it and display a concise summary in the "Generated Summary" section. This summary is created using a pre-trained Transformer model and aims to capture the key points of the earnings call.

5. **Explore Topic Extraction:**
    In the "Topic Extraction" section:
    - **Adjust the number of topics:** Use the slider to select the number of topics you want to extract from the transcript.
    - **View Extracted Topics:** The application will display a list of extracted topics, each represented by a set of keywords.
    - **Topic Visualization:** An interactive bar chart visualizes the distribution of keywords across the extracted topics, providing a graphical representation of the main themes discussed in the earnings call.

6. **Interact with Visualizations:**
    Use the interactive features of the Plotly charts (zoom, pan, hover) to explore the topic distributions and keyword weights in more detail.

7. **Educational Use:**
    Remember that this application is for educational and illustrative purposes to demonstrate NLP techniques in finance as taught in QuantUniversity courses.

## Credits

Developed by **QuantUniversity**.

This application is inspired by and demonstrates concepts from the **"AI and Big Data in Investments" course, Module 4**, available at [QuantUniversity](https://www.quantuniversity.com/).

## License

© 2025 QuantUniversity. All Rights Reserved.

This demonstration is for educational use and illustration only. Any reproduction or commercial use of this application requires prior written consent from QuantUniversity. For full legal documentation and licensing information, please contact QuantUniversity.
```
