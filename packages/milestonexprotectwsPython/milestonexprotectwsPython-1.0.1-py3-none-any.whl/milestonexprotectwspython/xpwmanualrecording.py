"""
Module: xpwmanualrecording.py

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
class XPWManualRecording:
    """
    Manual recording information for a device.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fDeviceId:str = None
        self._fIsManualRecording:bool = False


    @property
    def DeviceId(self) -> str:
        """ 
        Gets the DeviceId property value.

        Returns:
            The device id that was queried for the manual recording status.
        """
        return self._fDeviceId

    @DeviceId.setter
    def DeviceId(self, value:str) -> None:
        """ 
        Sets the DeviceId property value.
        """
        if value != None:
            self._fDeviceId = value


    @property
    def IsManualRecording(self) -> bool:
        """ 
        Gets the IsManualRecording property value.

        Returns:
            The enabled status of the service.
        """
        return self._fIsManualRecording

    @IsManualRecording.setter
    def IsManualRecording(self, value:bool) -> None:
        """ 
        Sets the IsManualRecording property value.
        """
        if value != None:
            self._fIsManualRecording = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "DeviceId: IsManualRecording"
        """
        return str.format("{0} - {1}", self.DeviceId or "", self.IsManualRecording)


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.DeviceId == other.DeviceId
        except Exception as ex:
            if (isinstance(self, XPWManualRecording)) and (isinstance(other, XPWManualRecording)):
                return self.DeviceId == other.DeviceId
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(key=lambda x: x.DeviceId or "", reverse=False)     <- GOOD syntax
            # epColl.sort(key=lambda x: x.DeviceId, reverse=False)           <- BAD syntax, as the "x.DeviceId" property may be None, and will cause this to fail!
            return self.DeviceId < other.DeviceId
        except Exception as ex:
            if (isinstance(self, XPWManualRecording)) and (isinstance(other, XPWManualRecording)):
                return self.DeviceId < other.DeviceId
            return False
