"""
Module: xpwsystemeventtype.py

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
# none

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWSystemEventType:
    """
    System Event Type information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fName:str = None
        self._fDescription:str = None
        self._fEventSource:str = None
        self._fEventTypeId:str = None


    @property
    def Description(self) -> str:
        """ 
        Gets the Description property value.

        Returns:
            A short description of what the system event type provides.
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
    def EventSource(self) -> str:
        """ 
        Gets the EventSource property value.

        Returns:
            The source of the event type (e.g. "Recorder", "Device", etc).
        """
        return self._fEventSource

    @EventSource.setter
    def EventSource(self, value:str) -> None:
        """ 
        Sets the EventSource property value.
        """
        if value != None:
            self._fEventSource = value


    @property
    def EventTypeId(self) -> str:
        """ 
        Gets the EventTypeId property value.

        Returns:
            The event type identifier.
        """
        return self._fEventTypeId

    @EventTypeId.setter
    def EventTypeId(self, value:str) -> None:
        """ 
        Sets the EventTypeId property value.
        """
        if value != None:
            self._fEventTypeId = value


    @property
    def Name(self) -> str:
        """ 
        Gets the Name property value.

        Returns:
            The name of the event type (e.g. "SmokeAndFireEnd", "ArchivingFailed", etc).
        """
        return self._fName

    @Name.setter
    def Name(self, value:str) -> None:
        """ 
        Sets the Name property value.
        """
        if value != None:
            self._fName = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "XPWSystemEventType: Name - EventTypeId"
        """
        return str.format("\"{0}\" - {1}", self.Name or "", self.EventTypeId or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWSystemEventType)) and (isinstance(other, XPWSystemEventType)):
                return self.Name == other.Name
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(key=lambda x: x.Name or "", reverse=False)     <- GOOD syntax
            # epColl.sort(key=lambda x: x.Name, reverse=False)           <- BAD syntax, as the "x.Name" property may be None, and will cause this to fail!
            return self.Name < other.Name
        except Exception as ex:
            if (isinstance(self, XPWSystemEventType)) and (isinstance(other, XPWSystemEventType)):
                return self.Name < other.Name
            return False
