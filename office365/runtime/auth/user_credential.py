class UserCredential(object):
    def __init__(self, user_name, password, upn=None):
        """

        :type password: str
        :type user_name str
        :type upn: str
        """
        self.userName = user_name
        self.password = password
        self.upn = upn
