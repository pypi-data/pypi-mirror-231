"""
Module: xpwserviceendpoint.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
# none

# our package imports.
# none.

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWServiceEndpoint:
    """
    Service Endpoint information returned by a ServiceRegistrationService GetService call.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fAuthentication:str = None
        self._fDescription:str = None
        self._fName:str = None
        self._fUri:str = None


    @property
    def Authentication(self) -> str:
        """ 
        Gets the Authentication property value.

        Returns:
            The type of authentication used (e.g. Basic, Windows, etc) by the service endpoint.
        """
        return self._fAuthentication

    @Authentication.setter
    def Authentication(self, value:str) -> None:
        """ 
        Sets the Authentication property value.
        """
        if value != None:
            self._fAuthentication = value


    @property
    def Description(self) -> str:
        """ 
        Gets the Description property value.

        Returns:
            A short description of what the service endpoint provides.
        """
        return self._fDescription

    @Description.setter
    def Description(self, value:str) -> None:
        """ 
        Sets the Description property value.
        """
        if value != None:
            self._fDescription = value


    @property
    def Name(self) -> str:
        """ 
        Gets the Name property value.

        Returns:
            The name of the service endpoint.
        """
        return self._fName

    @Name.setter
    def Name(self, value:str) -> None:
        """ 
        Sets the Name property value.
        """
        if value != None:
            self._fName = value


    @property
    def Uri(self) -> str:
        """ 
        Gets the Uri property value.

        Returns:
            The URI at which the service endpoint can be accessed at.
        """
        return self._fUri

    @Uri.setter
    def Uri(self, value:str) -> None:
        """ 
        Sets the Uri property value.
        """
        if value != None:
            self._fUri = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Name - Uri"
        """
        return str.format("{0} - {1}", self.Name or "", self.Uri or "")

    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWServiceEndpoint)) and (isinstance(other, XPWServiceEndpoint)):
                return self.Name == other.Name
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(key=lambda x: x.Uri or "", reverse=False)     <- GOOD syntax
            # epColl.sort(key=lambda x: x.Uri, reverse=False)           <- BAD syntax, as the "x.Uri" property may be None, and will cause this to fail!
            return self.Name < other.Name
        except Exception as ex:
            if (isinstance(self, XPWServiceEndpoint)) and (isinstance(other, XPWServiceEndpoint)):
                return self.Name < other.Name
            return False
