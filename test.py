import streamlit as st
from minio import Minio
import os

# we use this as data location
BUCKET_NAME = "test"

def save_file(infile):
  with open(infile.name, "wb") as f:
    f.write(infile.getbuffer())
  return infile.name


# pull secrets from a non-tracked secrets file
con = Minio(
    "http://172.31.2.211:38687/",
    access_key=os.getenv("MINIO_ACCESS_KEY", USERNAME),
    secret_key=os.getenv("MINIO_SECRET_KEY", PASSWORD),
    secure=True,
)

input_file = st.file_uploader("Drag your input file here")

if input_file is not None:
  name_file = save_file(input_file)

# Upload file as object name
if name_file:

  con.fput_object(BUCKET_NAME,"testupload.txt" , name_file)
