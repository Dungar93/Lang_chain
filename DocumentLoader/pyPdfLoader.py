from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:\\Users\\DUNGAR SONI\\OneDrive\\Desktop\\Langchain models\\srs_template-ieee.pdf")
documents = loader.load()

print(len(documents))
print(documents[0].page_content)   
print(documents[0].metadata) 