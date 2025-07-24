import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse 
from classify import classify

app = FastAPI() 

@app.post('/classify/')
async def classify_logs(file: UploadFile): 
    if not file.filename.endswith('.csv'): 
        raise HTTPException(status_code=400, detail='File must be a CSV')
    
    try: 
        # read the upload file 
        df = pd.read_csv(file.file)
        
        if 'source' not in df.columns or 'log_message' not in df.columns: 
            raise HTTPException(status_code=400, detail='CSV must contains \'source\' and \'log message\' columns')
        
        # perform the classification
        df['target_label'] = classify(list(zip(df['source'], df['log_message'])))
        
        print(f'Dataframe: {df.to_dict()}')
        
        # save the modified file to the resources folder
        output_file = '/home/madhuka/ML/NLP/Repos/Hybrid-Log-Classification-/resources/classified_data.csv'
        df.to_csv(output_file, index=False)
        
        print('File saved to resources folder')
        
        return FileResponse(output_file, media_type='text/csv')
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
    finally: 
        file.file.close() 