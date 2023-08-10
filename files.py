from pyodide import pyodide

import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

async def download(url, filename):
    response = await pyodide.pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

# Run the asynchronous download function
import asyncio
asyncio.run(download(filename, "example1.txt"))

print("done")




with open("C:/Users/Victor/Desktop/Python/Pythonfile.txt","w") as file1:
    file1.write("hello\n")
    file1.write("Python is weird\n")
    print("File closed")


with open ("C:/Users/Victor/Desktop/Python/Pythonfile.txt", "r") as file2:
    print( file2.readline())
    print(file2.readline())
    print("File closed")