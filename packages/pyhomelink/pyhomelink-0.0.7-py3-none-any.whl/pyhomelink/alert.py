"""Python module for accessing HomeLINK Alert."""
# import logging

from .auth import AbstractAuth

# from .utils import ApiComponent


class Alert:
    """Alert is the instantiation of a HomeLINK Alert"""

    def __init__(self, raw_data: dict, auth: AbstractAuth):
        """Initialize the property."""
        # super().__init__(
        #     parent
        # )
        self._raw_data = raw_data
        self._auth = auth

    @property
    def alertid(self) -> str:
        """Return the alertid of the Alert"""
        return self._raw_data["id"]

    @property
    def createdat(self) -> str:
        """Return the createdat of the Property"""
        return self._raw_data["createdAt"]

    @property
    def updatedat(self) -> str:
        """Return the updatedat of the Propery"""
        return self._raw_data["updatedAt"]

    @property
    def serialnumber(self) -> str:
        """Return the serialnumber of the Alert"""
        return self._raw_data["serialNumber"]

    @property
    def description(self) -> str:
        """Return the description of the Alert"""
        return self._raw_data["description"]

    @property
    def eventtype(self) -> str:
        """Return the eventtype of the Alert"""
        return self._raw_data["eventType"]

    @property
    def propertyreference(self) -> str:
        """Return the propertyreference of the Alert"""
        return self._raw_data["propertyReference"]

    @property
    def model(self) -> str:
        """Return the model of the Alert"""
        return self._raw_data["model"]

    @property
    def modeltype(self) -> str:
        """Return the modeltype of the Alert"""
        return self._raw_data["modelType"]

    @property
    def location(self) -> str:
        """Return the location of the Alert"""
        return self._raw_data["location"]

    @property
    def locationnickname(self) -> str:
        """Return the locationnickname of the Alert"""
        return self._raw_data["locationNickname"]

    @property
    def severity(self) -> str:
        """Return the severity of the Alert"""
        return self._raw_data["severity"]

    @property
    def category(self) -> str:
        """Return the category of the Alert"""
        return self._raw_data["category"]

    @property
    def hl_type(self) -> str:
        """Return the type of the Alert"""
        return self._raw_data["type"]

    @property
    def status(self) -> str:
        """Return the status of the Alert"""
        return self._raw_data["status"]

    @property
    def rel(self) -> any:
        """Return the tags of the Alert"""
        return self.Rel(self._raw_data["_rel"])

    class Rel:
        """Relative URLs for property."""

        def __init__(self, raw_data):
            """Initialise _Rel."""
            self._raw_data = raw_data

        @property
        def self(self) -> str:
            """Return the self url of the Alert"""
            return self._raw_data["_self"]

        @property
        def hl_property(self) -> str:
            """Return the property url of the Alert"""
            return self._raw_data["property"]

        @property
        def device(self) -> str:
            """Return the device url of the Alert"""
            return self._raw_data["device"]
