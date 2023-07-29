import json
import requests
import boto3
import os
import datetime
import uuid
from aws_lambda_powertools.logging import Logger

bucket_name = os.environ.get("BUCKET_NAME")

s3 = boto3.client("s3")

url = "https://edamam-recipe-search.p.rapidapi.com/search"

headers = {
    "x-RapidAPI-Host": "edamam-recipe-search.p.rapidapi.com",
    "x-RapidAPI-key": os.environ.get("RAPIDAPI_KEY"),
}

logger = Logger()


def get_recipe_data(recipe):
    try:
        response = requests.request(
            "GET", url, headers=headers, params={"q": recipe}
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        logger.exception(f"Request to {url} failed with error: {err}")
        return None
    return response.json()


def upload_to_s3(data, recipe):
    timestamp = datetime.datetime.now().isoformat()
    recipe = recipe.replace(" ", "-")
    unique_id = str(uuid.uuid4())  # generate a unique id
    filename = f"{unique_id}-{timestamp}-{recipe}-data.json"
    s3.put_object(Bucket=bucket_name, Key=filename, Body=json.dumps(data))


def lambda_handler(event, context):
    """
    Events:
        - recipe: str
    """
    recipe = event.get("recipe")
    data = get_recipe_data(recipe)

    if data is not None:
        upload_to_s3(data, recipe)
        return {
            "status": "success",
            "message": f"Data for {recipe} uploaded successfully.",
        }
    else:
        return {
            "status": "error",
            "message": f"Failed to get data for {recipe}",
        }
