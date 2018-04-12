"""Demonstrate basic usage of the Python client for Google Drive API v3

Created by Craig Finch (cfinch@ieee.org)
https://www.shocksolution.com
GPLv3 License
"""

import tempfile

from apiclient import discovery
from apiclient.http import MediaFileUpload

def credentials_from_file():
    """Load credentials from a service account file
    Args:
        None
    Returns: service account credential object
    
    https://developers.google.com/identity/protocols/OAuth2ServiceAccount
    """
    
    from google.oauth2 import service_account
    import googleapiclient.discovery

    # https://developers.google.com/identity/protocols/googlescopes#drivev3
    SCOPES = [
        'https://www.googleapis.com/auth/drive'
    ]
    SERVICE_ACCOUNT_FILE = './name-of-service-account-key.json'

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            
    return credentials

# Set your Google email address here
userEmail = 'craig@example.com'

credentials = credentials_from_file()
service = discovery.build('drive', 'v3', credentials=credentials)

# Create a folder
# https://developers.google.com/drive/v3/web/folder

folder_metadata = {
    'name': 'My Test Folder',
    'mimeType': 'application/vnd.google-apps.folder'
}
cloudFolder = service.files().create(body=folder_metadata).execute()

# Upload a file in the folder
# https://developers.google.com/api-client-library/python/guide/media_upload
# https://developers.google.com/drive/v3/reference/files/create

file_metadata = {
    'name': 'A Test File',
    'parents': [cloudFolder['id']]
}

with tempfile.NamedTemporaryFile(mode='w') as tf:
    tf.write("This is some test data")

    # https://developers.google.com/api-client-library/python/guide/media_upload
    media = MediaFileUpload(tf.name, mimetype='text/plain')
    # https://developers.google.com/drive/v3/web/manage-uploads
    cloudFile = service.files().create(body=file_metadata).execute()

# Share file with a human user
# https://developers.google.com/drive/v3/web/manage-sharing
# https://developers.google.com/drive/v3/reference/permissions/create

cloudPermissions = service.permissions().create(fileId=cloudFile['id'], 
    body={'type': 'user', 'role': 'reader', 'emailAddress': userEmail}).execute()

cp = service.permissions().list(fileId=cloudFile['id']).execute()
print(cp)

# List files in our folder
# https://developers.google.com/drive/v3/web/search-parameters
# https://developers.google.com/drive/v3/reference/files/list

query = "'{}' in parents".format(cloudFolder['id'])
filesInFolder = service.files().list(q=query, orderBy='folder', pageSize=10).execute()
items = filesInFolder.get('files', [])

# Print the paged results
if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print('{0} ({1})'.format(item['name'], item['id']))
        # service.files().delete(fileId=item['id']).execute()  # Optional cleanup