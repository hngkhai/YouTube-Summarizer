from langchain_community.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def summarize_youtube_video(url):
    # Load the transcript
    loader = YoutubeLoader.from_youtube_url(url,language=['zh-Hans', 'zh-Hant', 'en',"en-US"])
    #loader = YoutubeLoader.from_youtube_url(url, language=["en", "en-US"])
    transcript = loader.load()

    # Initialize the language model
    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-1.5-pro")

    # Load the summarization chain
    chain = load_summarize_chain(llm, chain_type="stuff")

    # Generate the summary
    summary = chain.invoke(transcript, return_only_outputs=True)
    return summary['output_text']