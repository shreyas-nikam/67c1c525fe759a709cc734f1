import streamlit as st
from transformers import pipeline
import gensim
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import plotly.express as px
from io import StringIO

st.set_page_config(page_title="QuCreate Streamlit Lab - Earnings Call Transcript Summarizer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab - Earnings Call Transcript Summarizer")
st.divider()

# Explanation of the App and NLP Concepts
st.header("About this Application")
st.write(
    "This application demonstrates the power of Natural Language Processing (NLP) in finance, specifically for analyzing earnings call transcripts. "
    "As discussed in Module 4 of 'AI and Big Data in Investments,' NLP techniques like summarization and topic extraction can transform lengthy transcripts into actionable insights."
)
st.markdown(
    """
    **Key Features:**
    - **Text Summarization:** Condenses long transcripts into concise summaries, highlighting key financial and strategic information.
    - **Topic Extraction:** Identifies and visualizes the main topics discussed in the earnings call using topic modeling.
    - **Interactive Visualizations:** Provides dynamic charts and graphs to explore the summarized data and extracted topics.

    **Reference:** This application is inspired by the concepts discussed in the QuantUniversity course "AI and Big Data in Investments," Module 4, page 12, focusing on NLP applications in asset management.
    """
)
st.divider()

# Initialize summarization pipeline - using a smaller model for performance
@st.cache_resource
def load_summarization_model():
    """Loads the summarization pipeline using a pre-trained model."""
    return pipeline("summarization", model="facebook/bart-large-cnn") # Using bart-large-cnn for better summarization, consider smaller models like 'sshleifer/distilbart-cnn-12-6' for faster performance if needed

summarizer = load_summarization_model()

# Initialize topic extraction resources
@st.cache_resource
def prepare_topic_extraction_resources(text_data):
    """Prepares resources for topic extraction: dictionary and corpus."""
    processed_text = gensim.parsing.preprocessing.preprocess_string(text_data)
    dictionary = Dictionary([processed_text])
    corpus = [dictionary.doc2bow(processed_text)]
    return dictionary, corpus

def extract_topics_lda(text_data, num_topics=5):
    """
    Extracts topics from text data using Latent Dirichlet Allocation (LDA).

    Args:
        text_data (str): The input text data.
        num_topics (int): The number of topics to extract.

    Returns:
        list: A list of tuples, where each tuple contains a topic ID and a list of words with their probabilities for that topic.
    """
    dictionary, corpus = prepare_topic_extraction_resources(text_data)
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary)
    topics = lda_model.print_topics(num_words=5) # Display top 5 words for each topic for brevity
    return topics

def display_topic_visualization(topics):
    """
    Displays topic weights in an interactive bar chart.

    Args:
        topics (list): List of topics from LDA model.
    """
    topic_words = []
    topic_weights = []
    topic_ids = []
    for topic_id, topic in enumerate(topics):
        words = topic.split('+')
        for word_prob in words:
            prob, word = word_prob.split('*')
            topic_words.append(word.strip())
            topic_weights.append(float(prob))
            topic_ids.append(f"Topic {topic_id+1}")

    if topic_words: # Check if topic_words is not empty
        fig = px.bar(
            x=topic_words,
            y=topic_weights,
            color=topic_ids,
            title="Topic Distribution in Earnings Call Transcript",
            labels={'x': 'Keywords', 'y': 'Topic Weight', 'color': 'Topic'},
            hover_name=topic_words,
            hover_data={'y': ':.4f'}
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No topics could be extracted. Please ensure the transcript is substantial enough for topic modeling.")


# Input Methods Tab
input_method = st.radio("Choose Input Method:", ["Direct Text Input", "File Upload", "URL Input (Simplified - Paste Text from URL)"], index=0)

transcript_text = ""

if input_method == "Direct Text Input":
    transcript_text = st.text_area("Enter Earnings Call Transcript Text Here:", height=300, placeholder="Paste your transcript text...")

elif input_method == "File Upload":
    uploaded_file = st.file_uploader("Upload a Transcript File (TXT)", type=["txt"])
    if uploaded_file is not None:
        # To convert to a string based on file type:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        transcript_text = stringio.read()

elif input_method == "URL Input (Simplified - Paste Text from URL)":
    st.info("For URL Input, please manually copy the transcript text from the URL and paste it below.")
    transcript_text = st.text_area("Paste Transcript Text from URL:", height=300, placeholder="Paste the transcript text you copied from the URL...")

if transcript_text:
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.header("Generated Summary")
        with st.spinner("Summarizing Transcript..."):
            try:
                summary_output = summarizer(transcript_text, max_length=150, min_length=30, do_sample=False) # Adjusted parameters, do_sample=False for deterministic output
                summary_text = summary_output[0]['summary_text']
                st.write(summary_text)
                st.info("This summary is generated using a Transformer-based model, focusing on extracting key sentences and phrases to provide a concise overview of the earnings call. It helps in quickly understanding the main points without reading the entire transcript.")
            except Exception as e:
                st.error(f"Error during summarization: {e}")
                st.warning("Ensure the transcript text is valid and substantial for summarization.")


    with col2:
        st.header("Topic Extraction")
        num_topics = st.slider("Number of Topics to Extract:", min_value=2, max_value=10, value=5, step=1,
                                    help="Adjust the number of topics to be extracted from the transcript. More topics can provide finer-grained analysis, but may also be less coherent.")
        with st.spinner("Extracting Topics..."):
            try:
                topics = extract_topics_lda(transcript_text, num_topics=num_topics)

                st.subheader("Extracted Topics:")
                topic_list_str = ""
                for topic_id, topic in enumerate(topics):
                    topic_list_str += f"**Topic {topic_id+1}:** {topic}\n\n"
                st.markdown(topic_list_str)

                st.info("Topic extraction is performed using Latent Dirichlet Allocation (LDA), an unsupervised learning technique. It identifies underlying topics in the transcript by analyzing word co-occurrence patterns. The bar chart below visualizes the weight distribution of the most significant words across these topics.")

                display_topic_visualization(topics)

            except Exception as e:
                st.error(f"Error during topic extraction: {e}")
                st.warning("Topic extraction may fail if the transcript is too short or does not contain enough thematic content. Adjust the input or try again.")


else:
    st.info("Please input transcript text to generate summary and topics.")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
