"""
Module: xpwservice.py

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
from .xpwcollection import XPWCollection
from .xpwserviceendpoint import XPWServiceEndpoint

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWService:
    """
    Service information returned by a ServiceRegistrationService GetService call.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fDescription:str = None
        self._fEnabled:bool = None
        self._fEndpointDefinition:str = None
        self._fEndpoints:XPWCollection = XPWCollection((XPWServiceEndpoint))
        self._fInstance:str = None
        self._fName:str = None
        self._fTrusted:bool = None
        self._fType:str = None
        self._fUri:list[str] = []

        # example:

        #<ServiceInfo>
        #  <type>3d6f1153-92ad-43f1-b467-9482ffd291b2</type>
        #  <instance>ef702e59-bf99-4b48-8b54-24d81053c3db</instance>
        #  <uri>
        #    <string>http://win10vm:22337/LogServer/</string>
        #  </uri>
        #  <name>Log server</name>
        #  <description>The log server for handling VMS system logging</description>
        #  <trusted>true</trusted>
        #  <enabled>true</enabled>
        #  <endpoints />
        #  <endpointdefinition>&lt;endpoints&gt;&lt;/endpoints&gt;</endpointdefinition>
        #</ServiceInfo>


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
    def Enabled(self) -> bool:
        """ 
        Gets the Enabled property value.

        Returns:
            The enabled status of the service.
        """
        return self._fEnabled

    @Enabled.setter
    def Enabled(self, value:bool) -> None:
        """ 
        Sets the Enabled property value.
        """
        if value != None:
            self._fEnabled = value


    @property
    def EndpointDefinition(self) -> str:
        """ 
        Gets the EndpointDefinition property value.

        Returns:
            All defined endpoint definitions as a string.  These endpoints are
            also represented as a collection of items by the EndPoints property.
        """
        return self._fEndpointDefinition

    @EndpointDefinition.setter
    def EndpointDefinition(self, value:str) -> None:
        """ 
        Sets the EndpointDefinition property value.
        """
        if value != None:
            self._fEndpointDefinition = value


    @property
    def Endpoints(self) -> XPWCollection:
        """ 
        Gets the Endpoints property value.

        Returns:
            All defined endpoint definitions as a collection.  These endpoints are
            also represented as a single string by the EndPointDefinition property.
        """
        return self._fEndpoints


    @property
    def Instance(self) -> str:
        """ 
        Gets the Instance property value.

        Returns:
            The instance ID of the service endpoint.
        """
        return self._fInstance

    @Instance.setter
    def Instance(self, value:str) -> None:
        """ 
        Sets the Instance property value.
        """
        if value != None:
            self._fInstance = value


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
    def Trusted(self) -> bool:
        """ 
        Gets the Trusted property value.

        Returns:
            The trusted status of the service.
        """
        return self._fTrusted

    @Trusted.setter
    def Trusted(self, value:bool) -> None:
        """ 
        Sets the Trusted property value.
        """
        if value != None:
            self._fTrusted = value


    @property
    def Type(self) -> str:
        """ 
        Gets the Type property value.

        Returns:
            The service type identifier.
        """
        return self._fType

    @Type.setter
    def Type(self, value:str) -> None:
        """ 
        Sets the Type property value.
        """
        if value != None:
            self._fType = value


    @property
    def Uri(self) -> list[str]:
        """ 
        Gets the Uri property value.

        Returns:
            The URI at which the service endpoint can be accessed at.
        """
        return self._fUri


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "XPWService: Name - Uri"
        """
        return str.format("{0} - {1}", self.Name or "", self.Uri or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWService)) and (isinstance(other, XPWService)):
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
            if (isinstance(self, XPWService)) and (isinstance(other, XPWService)):
                return self.Name < other.Name
            return False
