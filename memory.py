from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

memory_db = Chroma(
    collection_name="workout_memory",
    embedding_function=embeddings,
    persist_directory="./memory_db",
)

def save_workout(workout_text: str):
    memory_db.add_texts([workout_text])

def get_last_workout() -> str:
    docs = memory_db.similarity_search("last workout", k=1)
    if docs:
        return docs[0].page_content
    return "No workout history found"