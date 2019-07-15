from __future__ import print_function

import pickle
import os.path
import logging

from django.conf import settings

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GoogleDocument():
    def __init__(self):
        self.creds = None

    def authenticate(self):
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        SCOPES = ['https://www.googleapis.com/auth/documents']

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:

                if os.path.exists(os.path.join(settings.BASE_DIR, 'credentials.json')):
                    flow = InstalledAppFlow.from_client_secrets_file(
                        os.path.join(settings.BASE_DIR, 'credentials.json'), SCOPES)
                else:
                    logging.error("credentials.json file is missing from the project root directory. Google Docs API cannot be authenticated. Please refer to README.md for more information.")
                    return False
                
                self.creds = flow.run_local_server()
            
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        
        return True

    def create(self, title = "New Note", template = None):
        """
        Generates a google document from given template and title
        and returns the document ID.
        """
        service = build('docs', 'v1', credentials=self.creds)

        body = {
            'title': title
        }
        doc = service.documents().create(body=body).execute()
        return doc.get('documentId')

    def insert_blank_table(self, doc_id, nrows, ncols):
        """
        Inserts a table of dimensions nrows x ncols into document
        with ID doc_id.
        """
        service = build('docs', 'v1', credentials=self.creds)
        requests = [{
            'insertTable': {
                'rows': nrows,
                'columns': ncols,
                'endOfSegmentLocation': {
                    'segmentId': ''
                }
            },
        }]

        result = service.documents().batchUpdate(documentId=doc_id,
                                                 body={'requests': requests}).execute()

