"""
Module: xpwmanualrecordingresult.py

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
class XPWManualRecordingResult:
    """
    Represents result of starting and stopping manual recording.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fDeviceId:str = None
        self._fResultCode:str = None
        self._fMessage:str = None


    @property
    def DeviceId(self) -> str:
        """ 
        Gets the DeviceId property value.

        Returns:
            The device id that executed the manual recording function.
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
    def ResultCode(self) -> str:
        """ 
        Gets the ResultCode property value.

        Returns:
            The result code of the manual recording function.
        """
        return self._fResultCode

    @ResultCode.setter
    def ResultCode(self, value:str) -> None:
        """ 
        Sets the ResultCode property value.
        """
        if value != None:
            self._fResultCode = value


    @property
    def Message(self) -> str:
        """ 
        Gets the Message property value.

        Returns:
            The status message of the manual recording function.
        """
        return self._fMessage

    @Message.setter
    def Message(self, value:str) -> None:
        """ 
        Sets the Message property value.
        """
        if value != None:
            self._fMessage = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "{DeviceId} - {ResultCode}: {Message}"
        """
        return str.format("{0} - {1}: {2}", self.DeviceId or "", self.ResultCode, self.Message)


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.DeviceId == other.DeviceId
        except Exception as ex:
            if (isinstance(self, XPWManualRecordingResult)) and (isinstance(other, XPWManualRecordingResult)):
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
            if (isinstance(self, XPWManualRecordingResult)) and (isinstance(other, XPWManualRecordingResult)):
                return self.DeviceId < other.DeviceId
            return False
