import sys
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain

# Get the text and target language from command-line arguments
text = sys.argv[1]
target_language = sys.argv[2]

# Initialize the model with a specific model name
ollama_llm = OllamaLLM(model="llama3.2")

# Define the translation prompt template
prompt_template = PromptTemplate(
    input_variables=["text", "target_language"],
    template="Translate the following text to {target_language}: {text}"
)

# Set up streaming for real-time output
streaming_handler = StreamingStdOutCallbackHandler()

# Create the translation chain using LLMChain
translation_chain = LLMChain(
    llm=ollama_llm,
    prompt=prompt_template,
    callbacks=[streaming_handler]
)

# Define a function to perform translation
def translate_text(text, target_language="Spanish"):
    # Use run method (deprecated but functional)
    response = translation_chain.run({
        "text": text,
        "target_language": target_language
    })
    return response

# Get the translated text and print it (stdout will be sent to Node.js)
translated_text = translate_text(text, target_language)
print(translated_text)
