from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
import os

# Replace these values with your Azure Storage Account information


def uploadToBlobStorage(file_path, file_name,storage_account_key,storage_account_name,container_name,connection_string):
    try:
        storage_account_key = storage_account_key
        storage_account_name=storage_account_name
        container_name = container_name
        connection_string=connection_string
        
        blob_service_client=BlobServiceClient.from_connection_string(connection_string)
        blob_client=blob_service_client.get_blob_client(container=container_name,blob=file_name)

        with open(file_path,"rb") as data:
            blob_client.upload_blob(data)
        return True
    except ResourceExistsError:
        # Handle the case where the blob already exists, e.g., by renaming the blob
        new_file_name = generate_unique_file_name(file_name)
        uploadToBlobStorage(file_path, new_file_name)
        print(f"A blob with the name '{file_name}' already exists. Renamed to '{new_file_name}' and uploaded.")
        return True
    except Exception as e:
        return False
    
AZURE_STORAGE_ACCOUNT_KEY='6Sk0BZtTdYTtDipeNH4vb3w4mq7cd1J42bK5uc3PCfpYArOGgFkl2FqRsEi+LTLqgx+mN90ndozy+AStu36UrQ=='
AZURE_STORAGE_ACCOUNT_NAME="pythonacceleratorsg"
AZURE_CONTAINER_NAME="files"
AZURE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=pythonacceleratorsg;AccountKey=wRAQ3vet2DjEf4vcPpXz7tB3XJ5nl3kmKLwU1cyTGBCUimlt9I2iFyzj2vpVFKg9qTKdl59HCCwg+AStUKJ9og==;EndpointSuffix=core.windows.net"

def uploadBlob(AZURE_STORAGE_ACCOUNT_KEY,AZURE_STORAGE_ACCOUNT_NAME,AZURE_CONTAINER_NAME,AZURE_CONNECTION_STRING):

    pass
# Function to generate a unique blob name by appending a timestamp or random string
def generate_unique_file_name(file_name):
    import datetime
    import uuid

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4()).replace("-", "")[:8]
    return f"{file_name}_{timestamp}_{unique_id}"

# uploadToBlobStorage(os.path.join(os.getcwd(),'sampleDataFile.txt'),"smapleFileTesting")

