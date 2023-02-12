import concurrent.futures
import io
import os
import zipfile

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]
import requests

DOWNLOAD_FOLDER_NAME = "downloads"


def extract_zip(content):
    zip_file = zipfile.ZipFile(io.BytesIO(content))
    print("Extracting content...")
    zip_file.extractall(DOWNLOAD_FOLDER_NAME)


def download_file(url):
    response = requests.get(url)
    print("Downloading: ", url)

    if response.status_code != 200:
        print("failed to download ", response)
        return

    extract_zip(response.content)


def main():
    if not os.path.isdir(DOWNLOAD_FOLDER_NAME):
        os.makedirs(DOWNLOAD_FOLDER_NAME)

    with concurrent.futures.ThreadPoolExecutor(3) as executor:
        executor.map(download_file, download_uris)


if __name__ == '__main__':
    main()
