"""
Module: xpwhardware.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
from datetime import datetime

# our package imports.
# none

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWHardware:
    """
    Hardware information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fDescription:str = None
        self._fDeviceIds:list[str] = []
        self._fHardwareId:str = None
        self._fInterconnected:bool = None
        self._fLastModified:datetime = None
        self._fName:str = None
        self._fRecorderId:str = None
        self._fUri:str = None


    @property
    def Description(self) -> str:
        """ 
        Gets the Description property value.

        Returns:
            The user-friendly description of the hardware.
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
    def DeviceIds(self) -> list[str]:
        """ 
        A list of device identifiers associated with this hardware.

        Returns:
            The DeviceIds property value.
        """
        return self._fDeviceIds


    @property
    def HardwareId(self) -> str:
        """ 
        Gets the HardwareId property value.

        Returns:
            The globally unique identifier of the hardware.
        """
        return self._fHardwareId

    @HardwareId.setter
    def HardwareId(self, value:str) -> None:
        """ 
        Sets the HardwareId property value.
        """
        if value != None:
            self._fHardwareId = value


    @property
    def Interconnected(self) -> bool:
        """ 
        Gets the Interconnected property value.

        Returns:
            The Interconnected value.
        """
        return self._fInterconnected

    @Interconnected.setter
    def Interconnected(self, value:bool) -> None:
        """ 
        Sets the Interconnected property value.
        """
        if value != None:
            self._fInterconnected = value


    @property
    def LastModified(self) -> datetime:
        """ 
        Gets the LastModified property value.

        Returns:
            The date and time the hardware was last modified, in UTC format.
        """
        return self._fLastModified

    @LastModified.setter
    def LastModified(self, value:datetime) -> None:
        """ 
        Sets the LastModified property value.
        """
        if value != None:
            self._fLastModified = value


    @property
    def Name(self) -> str:
        """ 
        Gets the Name property value.

        Returns:
            The user-friendly name of the hardware.
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
    def RecorderId(self) -> str:
        """ 
        Gets the RecorderId property value.

        Returns:
            The globally unique identifier of the recoring server that owns this hardware item.
        """
        return self._fRecorderId

    @RecorderId.setter
    def RecorderId(self, value:str) -> None:
        """ 
        Sets the RecorderId property value.
        """
        if value != None:
            self._fRecorderId = value


    @property
    def Uri(self) -> str:
        """ 
        Gets the Uri property value.

        Returns:
            The URI used to access the hardware via the network.
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
            A string in the form of "Name - HardwareId"
        """
        return str.format("{0} - {1}", self.Name or "", self.HardwareId or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWHardware)) and (isinstance(other, XPWHardware)):
                return self.Name == other.Name
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(Name=lambda x: x.Name or "", reverse=False)     <- GOOD syntax
            # epColl.sort(Name=lambda x: x.Name, reverse=False)           <- BAD syntax, as the "x.Name" property may be None, and will cause this to fail!
            return self.Name < other.Name
        except Exception as ex:
            if (isinstance(self, XPWHardware)) and (isinstance(other, XPWHardware)):
                return self.Name < other.Name
            return False
