from __future__ import print_function

from googleapiclient.discovery import build

service = build('docs', 'v1')
def generate_google_doc(template, title):
    """
    Generates a google document from given template and title
    and returns the document ID.
    """
    return None

def create_blank_doc(title):
    """
    Generates a blank google document with the given title and
    returns the document instance.
    """
    body = {
        'title': title
    }
    doc = service.documents().create(body).execute()
    return doc
    # can return doc.get('documentId') to return doc id


def create_blank_table(nrows, ncols):
    """
    Generates and returns a table StructuralElement given the number of
    rows and cols
    """
    return None

def create_and_fill_table(tablerows):
    """

    :param tablerows:
    :return:
    """


