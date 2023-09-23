"""
Module: xpwdevicedisabled.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | DeviceType
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
class XPWDeviceDisabled():
    """
    Device Disabled information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fDeviceId:str = None
        self._fDeviceName:str = None
        self._fDeviceType:str = None
        self._fHardwareId:str = None
        self._fRecorderId:str = None


    @property
    def DeviceId(self) -> str:
        """ 
        The globally unique identifier of the device.

        Returns:
            The DeviceId property value.
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
    def DeviceName(self) -> str:
        """ 
        DeviceName of the device.

        Returns:
            The DeviceName property value.
        """
        return self._fDeviceName

    @DeviceName.setter
    def DeviceName(self, value:str) -> None:
        """ 
        Sets the DeviceName property value.
        """
        if value != None:
            self._fDeviceName = value


    @property
    def DeviceType(self) -> str:
        """ 
        A DeviceType of the device.

        Returns:
            The DeviceType property value.
        """
        return self._fDeviceType

    @DeviceType.setter
    def DeviceType(self, value:str) -> None:
        """ 
        Sets the DeviceType property value.
        """
        if value != None:
            self._fDeviceType = value


    @property
    def HardwareId(self) -> str:
        """ 
        The globally unique identifier of the hardware, with which the device is connected.

        Returns:
            The HardwareId property value.
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
    def RecorderId(self) -> str:
        """
        Globally unique identifier of the recording server holding this item.

        Returns:
            The RecorderId property value.
        """
        return self._fRecorderId

    @RecorderId.setter
    def RecorderId(self, value:str) -> None:
        """ 
        Sets the RecorderId property value.
        """
        if value != None:
            self._fRecorderId = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "DeviceName - DeviceType"
        """
        return str.format("{0} - {1}", self.DeviceName or "", self.DeviceType or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.DeviceName == other.DeviceName
        except Exception as ex:
            if (isinstance(self, XPWDeviceDisabled )) and (isinstance(other, XPWDeviceDisabled )):
                return self.DeviceName == other.DeviceName
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(DeviceName=lambda x: x.DeviceName or "", reverse=False)     <- GOOD syntax
            # epColl.sort(DeviceName=lambda x: x.DeviceName, reverse=False)           <- BAD syntax, as the "x.DeviceName" property may be None, and will cause this to fail!
            return self.DeviceName < other.DeviceName
        except Exception as ex:
            if (isinstance(self, XPWDeviceDisabled )) and (isinstance(other, XPWDeviceDisabled )):
                return self.DeviceName < other.DeviceName
            return False
