import uvicorn
from fastapi import FastAPI, Request, UploadFile, File
from app import verify_xml

app = FastAPI()

@app.get("/health")
def health():
    return "OK"

acceptedFileFormats = ["application/xml"]

@app.post("/verify")
async def verify_file(file: UploadFile = File(...)):
    contentType = file.content_type
    if not contentType in acceptedFileFormats:
        return "Invalid file format. Accepted File Formats: " + "".join(acceptedFileFormats)

    filename = file.filename
    content = await file.read()
    result = verify_xml(content)

    return {
        "filename": file.filename,
        "content_type": contentType,
        "result": result
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)
