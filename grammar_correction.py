import requests
from google_t import translation
import nlpcloud

client = nlpcloud.Client("finetuned-llama-3-70b", "bca20fbd012d68656faa286b4ed059a8c48511fd", gpu=True, lang="hin_Deva")
ans=client.gs_correction("its working")
print(ans)  