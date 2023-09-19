from os import environ
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
import json
from typing import Optional, List, Union, Type
# from pydantic import BaseModel, Field
from langchain.chains import create_extraction_chain
from pathlib import Path
from . import schemas

class QueryDocumentV3:
    def __init__(self, openai_key: Optional[str] = None, schema: Optional[dict] = None) -> None:
        
        if openai_key:
            environ["OPENAI_API_KEY"] = openai_key
            
        if not environ.get('OPENAI_API_KEY'):
            raise ValueError("No OpenAI key provided")
            
        self.llm = ChatOpenAI(temperature=0,  model="gpt-4")

        #if no schema provided, use default
        if schema == None:
            self.properties = schemas.default_schema_enbridge()
            self.chain = create_extraction_chain(self.properties, llm=self.llm)
            
        #if a schema provided
        else:
            self.properties = schema
            self.chain = create_extraction_chain(self.properties, llm=self.llm)
                

    #Search
    def search_v3(self, file_path: str, level: str):     
        chain = self.chain
        try:
            #Convert PDF content into chunks of text
            loader = PyMuPDFLoader(file_path)
            docs = loader.load()
            text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=0)
            docs = text_splitter.split_documents(docs)
            result = chain.run(docs)
            
            #Add 2 other fields
            pred = result[0]
            if not isinstance(pred,dict):
                pred = pred.__dict__
            pred['level'] = level
            path = Path(file_path)
            pred['document_id'] = path.name[:-4]
            return pred
        
        except Exception as e:
            print(e)

