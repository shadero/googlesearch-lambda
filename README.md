# googlesearch-lambda

Google Search API running on AWS Lambda.

## Setup

1. Type the following command
```sh
pip install -r requirements.txt --target ./dist
cp ./lambda_function.py ./dist
```

2. Zip the files in the "dist" file
3. Upload zip file to AWS Lambda
