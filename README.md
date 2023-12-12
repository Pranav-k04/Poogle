# Information Retrieval Mini Project 
# Poogle 
This Project is a document retrivel project, contains 2 parts CLient side and server side 

For corpus refer to this link to download the zip file & EXTRACT IT and name the data as 'files' :
corpus zip file : total files around 60,000 files.
https://drive.google.com/file/d/1jF-hBvxCBHOaT62jUueBItD8Q45BKG_Z/view?usp=sharing

if above takes too much time directly download assets that is indexed data from the corpus.
https://drive.google.com/file/d/1jF-hBvxCBHOaT62jUueBItD8Q45BKG_Z/view?usp=sharing

Set up for Client Side of the project follow the below codes : 
`$ npm i`

Set up for Server Side of the Project (open new terminal):
`pip install fastapi`
`pip install "uvicorn[standard]`
`python -m venv .venv`
`pip install -r requirements.txt`
# this set up might take some time please wait patiently

TO run the whole Project : 
`npm run dev`
    
    
Project Decription : 
The client side of this project is made in React.js and uses FastAPI to send requests to the backend of the project that is the server side.
There are 4 main folders in the server side of this project, 
Assets: these are Indexed data from the corpus, code in server/core/tfidf.py 
Core: There folders have all the computation code for creating IDF and tf-idf.py and query_processing.py 
Routes: The Routes link the front end of the server to server side.
Utils: have the source code to start the server essentially uvicorn, FastAPi code.


Further improvements in Poogle :
Updating retrieval scores based on the Relevance FeedBack given by the client.
