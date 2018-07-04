import json

from examples.settings import settings
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.runtime.client_request import ClientRequest
from office365.runtime.utilities.http_method import HttpMethod
from office365.runtime.utilities.request_options import RequestOptions


def read_list_items(context, list_title):
    """Read list items example"""
    request = ClientRequest(context)
    options = RequestOptions("web/lists/getbyTitle('{0}')/items".format(list_title))
    options.set_header('Accept', 'application/json; odata=nometadata')

    print("Retrieving list items from List {0}".format(list_title))
    response = request.execute_request_direct(options)
    data = json.loads(response.content)
    for item in data['value']:
        print("Item title: {0}".format(item["Title"]))


def create_list_item(context, list_title):
    """Create list item example"""
    request = ClientRequest(context)
    options = RequestOptions("web/lists/getbyTitle('{0}')/items".format(list_title))
    options.set_header('Accept', 'application/json; odata=nometadata')  # JSON Light nometadata mode!
    options.data = {'Title': 'New Task'}
    options.method = HttpMethod.Post
    print("Creating list item...")
    response = request.execute_request_direct(options)
    item = json.loads(response.content)
    print("Task {0} has been successfully [created]".format(item['Title']))
    return item


def update_list_item(context, list_title, item_id):
    """Update list item example"""
    request = ClientRequest(context)
    options = RequestOptions(
        "web/lists/getbyTitle('{0}')/items({1})".format(list_title, item_id))
    options.set_header('Accept', 'application/json; odata=nometadata')  # JSON Light nometadata mode!
    options.set_header('IF-MATCH', '*')
    options.set_header('X-HTTP-Method', 'MERGE')
    options.data = {'Title': 'New Task (updated)'}
    options.method = HttpMethod.Post
    print("Updating list item...")
    request.execute_request_direct(options)
    print("Task has been successfully [updated]")


def delete_list_item(context, list_title, item_id):
    """Delete list item example"""
    request = ClientRequest(context)
    options = RequestOptions(
        "web/lists/getbyTitle('{0}')/items({1})".format(list_title, item_id))
    options.set_header('Accept', 'application/json; odata=nometadata')  # JSON Light nometadata mode!
    options.set_header('IF-MATCH', '*')
    options.set_header('X-HTTP-Method', 'DELETE')
    options.data = {'Title': 'New Task (updated)'}
    options.method = HttpMethod.Post
    print("Deleting list item...")
    request.execute_request_direct(options)
    print("Task has been successfully [deleted]")


if __name__ == '__main__':
    ctx_auth = AuthenticationContext(url=settings['url'])
    if ctx_auth.acquire_token_for_user(username=settings['user_credentials']['username'],
                                       password=settings['user_credentials']['password']):
        target_list_title = "Tasks"
        # ctx = ClientContext(settings['url'], ctx_auth)  # Initialize client context
        read_list_items(ctx, target_list_title)
        task_item = create_list_item(ctx, target_list_title)
        update_list_item(ctx, target_list_title, task_item['Id'])
        delete_list_item(ctx, target_list_title, task_item['Id'])

    else:
        print(ctx_auth.get_last_error())
