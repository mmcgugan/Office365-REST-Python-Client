from datetime import datetime, timedelta, timezone
from enum import Enum
from uuid import UUID
from office365.runtime.client_value import ClientValue


class TokenScope(Enum):
    ContentDB = 0
    SiteCollection = 1
    Site = 2
    List = 3


class ChangeToken(ClientValue):
    """Represents the unique sequential location of a change within the change log. Client applications can use the
    change token as a starting point for retrieving changes."""

    version = 1
    scope = TokenScope.List
    _guid = UUID(int=0)
    _timestamp = datetime(1, 1, 1, tzinfo=timezone.utc)
    changed = -1

    def __init__(self, string_value=None, **kwargs):
        """
        :param str string_value: Contains the serialized representation of the change token generated
            by the protocol server. When setting StringValue, the protocol client MUST use a value previously returned
            by the protocol server.

            Represented as a semicolon-separated list containing the following, in order:
              - The version number of the change token.
              - The change token's collection scope.
              - The collection scope GUID.
              - The time of the change token in ticks.
              - The change number.
        """
        super(ChangeToken, self).__init__()
        if string_value is not None:
            self.string_value = string_value

        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def __str__(self):
        return self.StringValue or ""

    def __repr__(self):
        return self.StringValue or ""

    def __iter__(self):
        yield_props = {
            "StringValue": self.StringValue,
            "__metadata": {"type": "SP.ChangeToken"},
        }
        for k, v in yield_props.items():
            yield k, v

    @property
    def entity_type_name(self):
        return "SP.ChangeToken"

    @property
    def string_value(self):
        return "{0};{1};{2};{3};{4}".format(
            self.version,
            self.scope,
            self.guid,
            self.timestamp,
            self.changed,
        )
    
    @string_value.setter
    def string_value(self, value):
        version, scope, guid, timestamp, changed = value.split(";")
        self.version = int(version)
        self.scope = TokenScope(int(scope))
        self.guid = guid
        self.timestamp = int(timestamp)
        self.changed = int(changed)

    @property
    def StringValue(self):
        return self.string_value
    
    @StringValue.setter
    def StringValue(self, value):
        self.string_value = value

    @property
    def guid(self):
        return str(self._guid)
    
    @guid.setter
    def guid(self, value):
        self._guid = UUID(value)

    @property
    def timestamp(self):
        time_base = datetime(1, 1, 1, tzinfo=timezone.utc)
        secs = (self._timestamp - time_base).total_seconds()
        return int(secs * 10**7)

    @timestamp.setter
    def timestamp(self, value):
        if type(value) is str or type(value) is int:
            time_base = datetime(1, 1, 1, tzinfo=timezone.utc)
            self._timestamp = time_base + timedelta(
                microseconds=int(value) // 10)
        elif type(value) is datetime:
            if value.tzinfo is None:
                value = value.replace(tzinfo=timezone.utc)
            self._timestamp = value
        else:
            raise TypeError("Invalid type for timestamp: %s" % type(value))
