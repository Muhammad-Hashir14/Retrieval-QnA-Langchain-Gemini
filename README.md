# Code Basics FAQs Bot

---

## Overview

This bot is created using **LangChain** and **Google's Gemini API**, designed to answer frequently asked questions (FAQs) from students of **CodeBasics**. It utilizes **Streamlit** for the user interface (UI) and uses data from a CSV file containing student-related queries and answers, enabling the bot to respond with relevant and specific information.

---

## Key Components

1. **LangChain**: 
   - Handles embeddings and vectorized search from the CSV data.
   - Converts CSV data into embeddings for efficient similarity searches when users ask questions.

2. **Google Gemini API**: 
   - Uses the **ChatGoogleGenerativeAI** model (`gemini-pro`) for advanced question-answering capabilities.
   - Provides intelligent and context-aware answers based on user queries.

3. **Streamlit for UI**: 
   - Streamlit provides the interactive user interface, allowing students to type their questions and get immediate responses.
   - The UI features input boxes, chat history, and sidebar widgets for a seamless user experience.

4. **CSV Data Source**: 
   - The bot retrieves information from a CSV file that contains structured data with questions and answers.
   - This CSV file is processed into embeddings using LangChain helper functions, allowing for efficient querying and retrieval.

---

## Workflow

1. **Embedding Creation**:
   - Using `createEmbeddings`, the data from the CSV file is processed into embeddings (vectorized representations).
   - These embeddings are stored in a **FAISS** database for fast lookup during similarity searches.

2. **Vector Database (FAISS)**:
   - **FAISS (Facebook AI Similarity Search)** is used to store and retrieve embeddings for efficient querying.
   - When a user asks a question, FAISS searches for the closest match in the vector database based on the query.

3. **Question-Answering Chain**:
   - The bot uses `get_qa_chain` to process the user's question and retrieve the most relevant answer.
   - The chain fetches the best match from the FAISS database and then generates a response using the **Google Gemini API**.

4. **Streamlit Interface**:
   - Users interact with the bot through a text input field located at the bottom of the page.
   - The chat history is displayed in a sidebar, allowing users to view previous conversations while focusing on the current question.
   - The interface mimics a chat experience where user questions and bot responses are displayed interactively.

---

## How to Use the Bot

1. **Ask a Question**:
   - Type your question into the input box at the bottom of the interface.
   - Press enter or click submit to send your question.

2. **View Responses**:
   - The bot will retrieve and display the most relevant answer based on the CSV data.
   - Chat history is available in the sidebar for easy reference to previous interactions.

3. **CSV Data Integration**:
   - The bot retrieves answers from a CSV file containing FAQs and related responses.
   - Ensure that the CSV file is structured properly with clear question-answer pairs before running the bot.

---

## Requirements

- **LangChain**: The core framework for handling embeddings, vector searches, and chain management.
- **Google Gemini API**: Requires an API key to access the **ChatGoogleGenerativeAI** model.
- **Streamlit**: The UI framework for building the chatbot interface.
- **FAISS**: A similarity search engine used for efficient embedding lookups.
- **CSV Data**: A CSV file containing structured question-answer data relevant to CodeBasics students.

---

## Example Usage

- **Student Question**: "How do I access the CodeBasics GitHub repository?"
- **Bot Response**: "You can access the CodeBasics GitHub repository by visiting [GitHub Projects](https://github.com/codebasics)."

The bot retrieves this answer from the CSV file where FAQs are stored, ensuring responses are relevant and tied to the specific dataset.

---

## Customization

- You can update the CSV file with new questions and answers to extend the bot's knowledge base.
- Modify the LangChain helper functions (e.g., `createEmbeddings`, `createVectorDB`) to adapt the bot for other types of data sources or formats beyond CSV.

---

## Deployment

1. Ensure the API keys and environment variables (like `GOOGLE_API_KEY`) are properly configured in **Streamlit Secrets**.
2. Deploy the bot on a platform like **Streamlit Cloud** for easy sharing and accessibility by students.

---

## Conclusion

This specialized chatbot is an efficient tool for answering student questions using the available CodeBasics FAQs data. Built with LangChain, Google Gemini API, and Streamlit, the bot is adaptable and scalable, making it a valuable resource for student queries.

![sample_image](https://github.com/user-attachments/assets/1cec2aed-2fbc-46ee-80fb-0e789872e4ba)
