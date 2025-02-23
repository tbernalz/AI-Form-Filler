from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config import CHUNK_SIZE, CHUNK_OVERLAP


def process_data(
    directory: str, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
) -> FAISS:
    """
    Process and index PDF documents from a specified directory. This function reads PDF documents from the given directory, splits the text into manageable chunks,
    generates embeddings using a specified model, and indexes the documents using FAISS for efficient retrieval.

    Args:
        directory (str): The directory path containing the PDF documents to be processed.
        model_name (str, optional): The name of the HuggingFace model to use for generating embeddings.

    Returns:
        FAISS: A FAISS index containing the embedded document chunks.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        Exception: If any other error occurs during the processing.
    """
    try:
        loader = PyPDFDirectoryLoader(directory)
        docs = loader.load()

        if not docs:
            print("No documents found in the specified directory.")
            return None

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        )
        texts = text_splitter.split_documents(docs)
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        db = FAISS.from_documents(texts, embeddings)

        return db

    except FileNotFoundError as e:
        print(f"Directory not found: {directory}")
        raise FileNotFoundError(f"Directory not found: {directory}") from e
    except Exception as e:
        print(f"An error occurred during document processing: {e}")
        raise Exception(f"An error occurred during document processing: {e}") from e
