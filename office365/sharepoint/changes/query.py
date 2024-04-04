from office365.runtime.client_value import ClientValue


class ChangeQuery(ClientValue):
    """Defines a query that is performed against the change log."""

    def __init__(
        self,
        activity=False,
        add=True,
        alert=False,
        content_type=False,
        delete_object=True,
        field=False,
        file=False,
        folder=False,
        group=False,
        group_membership_add=False,
        group_membership_delete=False,
        item=False,
        latest_first=False,
        list_=False,
        move=False,
        navigation=False,
        rename=False,
        restore=False,
        role_assignment_add=True,
        role_assignment_delete=True,
        role_definition_add=False,
        role_definition_delete=False,
        role_definition_update=False,
        security_policy=False,
        site=False,
        system_update=False,
        update=True,
        user=False,
        view=False,
        web=False,
        change_token_start=None,
        change_token_end=None,
        fetch_limit=None,
    ):
        """
        :param bool activity:
        :param bool add: Gets or sets a value that specifies whether add changes are included in the query.
        :param bool alert: Gets or sets a value that specifies whether changes to alerts are included in the query.
        :param bool content_type: Gets or sets a value that specifies whether changes to content types are included in the query.
        :param bool delete_object: Gets or sets a value that specifies whether delete changes are included in the query.
        :param bool field: Gets or sets a value that specifies whether changes to site columns are included in the query.
        :param bool file: Gets or sets a value that specifies whether changes to files are included in the query.
        :param bool folder: Gets or sets value that specifies whether changes to folders are included in the query.
        :param bool group: Gets or sets a value that specifies whether changes to groups are included in the query.
        :param bool group_membership_add: Gets or sets a value that specifies whether adding users to groups is included in the query.
        :param bool group_membership_delete: Gets or sets a value that specifies whether deleting users from the groups is included in the query.
        :param bool item: Gets or sets a value that specifies whether general changes to list items are included in the query.
        :param bool latest_first: Gets or sets a value that specifies whether to order the results by Modified By date, most recent first.
        :param bool list_: Gets or sets a value that specifies whether changes to lists are included in the query.
        :param bool move: Gets or sets a value that specifies whether move changes are included in the query.
        :param bool navigation: Gets or sets a value that specifies whether changes to the navigation structure of a site collection are included in the query.
        :param bool rename: Gets or sets a value that specifies whether renaming changes are included in the query.
        :param bool restore: Gets or sets a value that specifies whether restoring items from the recycle bin or from backups is included in the query.
        :param bool role_assignment_add: Specifies whether adding role assignments is included in the query.
        :param bool role_assignment_delete: Specifies whether deleting role assignments is included in the query.
        :param bool role_definition_add: Gets or sets a value that specifies whether adding role definitions is included in the query.
        :param bool role_definition_delete: Gets or sets a value that specifies whether deleting role definitions is included in the query.
        :param bool role_definition_update: Gets or sets a value that specifies whether modifying role definitions is included in the query.
        :param bool security_policy: Gets or sets a value that specifies whether modifications to security policies are included in the query.
        :param bool site: Gets or sets a value that specifies whether changes to site collections are included in the query.
        :param bool system_update: Gets or sets a value that specifies whether updates made using the item SystemUpdate method are included in the query.
        :param bool update: Gets or sets a value that specifies whether update changes are included in the query.
        :param bool user: Gets or sets a value that specifies whether changes to users are included in the query.
        :param bool view: Gets or sets a value that specifies whether changes to views are included in the query.
        :param bool web: Gets or sets a value that specifies whether changes to Web sites are included in the query.
        :param change_token_start: office365.sharepoint.changes.changeToken.ChangeToken
        :param change_token_end: office365.sharepoint.changes.changeToken.ChangeToken
        :param int fetch_limit:
        """
        super(ChangeQuery, self).__init__()
        self.Activity = activity
        self.Add = add
        self.Alert = alert
        self.ContentType = content_type
        self.DeleteObject = delete_object
        self.FetchLimit = fetch_limit
        self.Field = field
        self.File = file
        self.Folder = folder
        self.Group = group
        self.GroupMembershipAdd = group_membership_add
        self.GroupMembershipDelete = group_membership_delete
        self.Item = item
        self.LatestFirst = latest_first
        self.List = list_
        self.Move = move
        self.Navigation = navigation
        self.Rename = rename
        self.Restore = restore
        self.RoleAssignmentAdd = role_assignment_add
        self.RoleAssignmentDelete = role_assignment_delete
        self.RoleDefinitionAdd = role_definition_add
        self.RoleDefinitionDelete = role_definition_delete
        self.RoleDefinitionUpdate = role_definition_update
        self.SecurityPolicy = security_policy
        self.Site = site
        self.SystemUpdate = system_update
        self.Update = update
        self.User = user
        self.View = view
        self.Web = web

        if self.FetchLimit is not None:
            self.FetchLimit = str(self.FetchLimit)

        if change_token_start is not None:
            self.ChangeTokenStart = dict(change_token_start)
        if change_token_end is not None:
            self.ChangeTokenEnd = dict(change_token_end)

    @property
    def entity_type_name(self):
        return "SP.ChangeQuery"
