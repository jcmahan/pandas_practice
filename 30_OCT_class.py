# embedding omdels
# similar strings will create a list of similar numbers when you run text 
# through an embedding model

# embeddings allow you to measure similarity (open ai has one; they cost $$)

# free options: hugging face (all-MiniLM-L6-v2); spacy(en-core-web-md)
# paid options: text=embedding-3-small, text-embedding-3-large (openAI); gemini=embedding-001 (google)

# allows for similarity search in 3 steps (search engines/recommendation models are 
#   built on embeddings)
# 1) save (turn every item into an embedding and store it)
# 2) search = turn the search into an embedding
# 3) match = return the stored items with the closes embeddings
