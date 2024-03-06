# from flask import Flask,render_template,url_for,request,redirect
# import json
# import pandas as pd
# import os
# from langchain_community.document_loaders import UnstructuredURLLoader
# from langchain.text_splitter import CharacterTextSplitter
# import pickle
# import faiss
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.chains.question_answering import load_qa_chain
# from openai import OpenAI
# app=Flask(__name__)
# def fetchData(question):
#     df = pd.read_csv('C:\\Users\\drbin\\Desktop\\TEST\\data\\urlbooks (2).csv')
#     column_list = df['Link'].tolist()
#     loaders = UnstructuredURLLoader(urls=column_list)
#     data = loaders.load()
#     text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200)
#     docs = text_splitter.split_documents(data)
#     os.environ["OPENAI_API_KEY"] = "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"
#     embeddings = OpenAIEmbeddings()
#     faiss='faiss_db'
#     vectorStore_openAI = FAISS.from_documents(docs, embeddings)
#     vectorStore_openAI.save_local(faiss)
#     reload_faiss=FAISS.load_local(faiss, embeddings)
#     llm=OpenAI(temperature=0, model_name='gpt-3.5-turbo-instruct')
#     chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=reload_faiss.as_retriever())
#     return chain({"question": f'{question}'}, return_only_outputs=True)
# @app.route("/")
# def home():
#     if request.method == 'POST':
#         question=request.form['question']
#         raw= fetchData(question)
#         print(raw)
#         return redirect(url_for("home"))
#     return render_template("home.html")

# @app.route("/MOM",methods=['POST'])
# def generate():
#     return render_template("mom.html")

# if __name__=="__main__":
#     app.run(debug=True)