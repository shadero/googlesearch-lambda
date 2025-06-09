import json
from googlesearch import search

MAX_RESULTS = 100


def lambda_handler(event, context):
    query = str(event.get("queryStringParameters", {}).get("query", ""))
    size = int(event.get("queryStringParameters", {}).get("size", 10))
    if query == "":
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Query parameter is required"}),
        }
    if size < 1 or size > MAX_RESULTS:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": f"Size must be between 1 and {MAX_RESULTS}"}),
        }

    results = search(
        query,
        advanced=True,
        num_results=size,
        unique=True,
        sleep_interval=1,
        lang="ja",
        region="jp",
    )
    output = [
        {"url": v.url, "title": v.title, "description": v.description} for v in results
    ]
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(output, ensure_ascii=False),
    }
