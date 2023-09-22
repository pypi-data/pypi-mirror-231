from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import BytesIO, TextIOWrapper
from typing import Optional

class AzureBlobConnector:
    """
    A class for interacting with Azure Blob Storage.

    Attributes:
        container_client (ContainerClient): The Azure Blob Storage container client.
    """

    def __init__(self, container_name: str, connection_string: str):
        """
        Initialize the BlobConnector class with the Azure Blob Storage container and connection string.

        Args:
            container_name (str): The name of the container in Azure Blob Storage.
            connection_string (str): The connection string to access Azure Blob Storage.
        """
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = blob_service_client.get_container_client(container_name)

    def blob_uploader(self, file_stream: str, filename: str):
        """
        Upload a file stream to Azure Blob Storage.

        Args:
            file_stream (str): The file stream to upload.
            filename (str): The name of the blob in Azure Blob Storage.
        """
        blob_client = self.container_client.get_blob_client(filename)
        blob_client.upload_blob(data=file_stream, overwrite=True)

    def blob_deleter(self, filename: str):
        """
        Delete a blob from Azure Blob Storage.

        Args:
            filename (str): The name of the blob to delete.
        """
        blob_client = self.container_client.get_blob_client(filename)
        blob_client.delete_blob()

    def blob_dataframe_uploader(self, df: pd.DataFrame, filename: str, index: Optional[bool] = False, filetype: Optional[str] = 'csv'):
        """
        Upload a DataFrame as a CSV or Excel blob to Azure Blob Storage.

        Args:
            df (pd.DataFrame): The DataFrame to upload.
            filename (str): The name of the blob in Azure Blob Storage.
            index (bool, optional): Whether to include the index in the CSV or Excel file. Defaults to False.
            filetype (str, optional): The file type ('csv', 'excel', or 'txt'). Defaults to 'csv'.
        """
        stream_file = BytesIO()
        if filetype == 'csv' or filetype == 'txt':
            df.to_csv(stream_file, index=index)
        elif filetype == 'excel':
            df.to_excel(stream_file, index=index)
        file_to_blob = stream_file.getvalue()
        blob_client = self.container_client.get_blob_client(filename)
        blob_client.upload_blob(data=file_to_blob, overwrite=True)

    def stream_blob(self, file_name: str):
        """
        Stream the content of a blob from Azure Blob Storage.

        Args:
            file_name (str): The name of the blob to stream.

        Returns:
            bytes: A bytes object containing the blob's content.
        """
        blob_client = self.container_client.get_blob_client(blob=file_name)
        return (blob_client.download_blob()).readall()

    def list_blobs(self, folder_path: str):
        """
        List the names of blobs within a specified folder path in Azure Blob Storage.

        Args:
            folder_path (str): The folder path to list blobs from.

        Returns:
            list: A list of blob names within the specified folder path.
        """
        blob_names = []
        for blob in self.container_client.list_blobs(name_starts_with=folder_path):
            blob_names.append(blob.name)
        return blob_names

    def list_blobs_metadata(self, folder_path: str):
        """
        List the metadata of blobs within a specified folder path in Azure Blob Storage.

        Args:
            folder_path (str): The folder path to list blobs from.

        Returns:
            list: A list of blob metadata within the specified folder path.
        """
        blob_list_meta = self.container_client.list_blobs(name_starts_with=folder_path)
        return blob_list_meta

    def stream_blob_csv_into_dataframe(self, file_name: str):
        """
        Stream a CSV blob from Azure Blob Storage into a Pandas DataFrame.

        Args:
            file_name (str): The name of the CSV blob to stream.

        Returns:
            pd.DataFrame: A Pandas DataFrame containing the CSV data.
        """
        blob_client = self.container_client.get_blob_client(blob=file_name)
        blob_file = blob_client.download_blob()
        csv = BytesIO(blob_file.readall())
        df = pd.read_csv(csv)
        return df

    def stream_blob_txt_into_dataframe(self, file_name: str):
        """
        Stream a text blob from Azure Blob Storage into a Pandas DataFrame.

        Args:
            file_name (str): The name of the text blob to stream.

        Returns:
            pd.DataFrame: A Pandas DataFrame containing the text data.
        """
        blob_client = self.container_client.get_blob_client(blob=file_name)
        blob_file = blob_client.download_blob()
        txt = BytesIO(blob_file.readall())
        df = pd.read_fwf(txt)
        return df

    def stream_blob_excel_into_dataframe(self, file_name: str, sheet_name: Optional[str] = None):
        """
        Stream an Excel blob from Azure Blob Storage into a Pandas DataFrame.

        Args:
            file_name (str): The name of the Excel blob to stream.
            sheet_name (str, optional): The name of the sheet to read from in the Excel file.

        Returns:
            pd.DataFrame: A Pandas DataFrame containing the Excel data.
        """
        blob_client = self.container_client.get_blob_client(blob=file_name)
        blob_file = blob_client.download_blob()
        excel = BytesIO(blob_file.readall())
        if sheet_name is None:
            df = pd.read_excel(excel)
        else:
            df = pd.read_excel(excel, sheet_name=sheet_name)
        return df

    def stream_blob_to_iterate(self, file_name: str):
        """
        Stream a text blob from Azure Blob Storage for iteration line by line.

        Args:
            file_name (str): The name of the text blob to stream.

        Returns:
            TextIOWrapper: A text file stream for iteration.
        """
        blob_client = self.container_client.get_blob_client(blob=file_name)
        blob_file = blob_client.download_blob()
        text_file = TextIOWrapper(BytesIO(blob_file.readall()))
        return text_file

    def stream_blob_to_upload(self, file_name: str):
        """
        Stream a blob from Azure Blob Storage for potential upload or processing.

        Args:
            file_name (str): The name of the blob to stream.

        Returns:
            bytes: A bytes object containing the blob's content.
        """
        blob_client = self.container_client.get_blob_client(blob=file_name)
        blob_file = blob_client.download_blob()
        return blob_file.readall()
