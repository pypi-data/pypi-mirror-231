"""
Module: xpwdevice.py

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
class XPWDevice :
    """
    Device information base class.
    
    Supplemental documentation can be found at:
    https://doc.milestonesys.com/latest/en-US/standard_features/sf_mc/sf_ui/mc_devicestabs_devices.htm#MC_InfoTabExplained.htm

    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fDescription:str = None
        self._fDeviceId:str = None
        self._fDeviceIndex:int = None
        self._fGisPoint:str = None
        self._fHardwareId:str = None
        self._fIcon:int = None
        self._fName:str = None
        self._fRecorderId:str = None
        self._fShortName:str = None


    @property
    def Description(self) -> str:
        """ 
        A description of the device.

        Returns:
            The Description property value.
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
    def DeviceIndex(self) -> int:
        """ 
        The index of the device.

        Returns:
            The DeviceIndex property value.
        """
        return self._fDeviceIndex

    @DeviceIndex.setter
    def DeviceIndex(self, value:int) -> None:
        """ 
        Sets the DeviceIndex property value.
        """
        if value != None:
            self._fDeviceIndex = value


    @property
    def GisPoint(self) -> str:
        """ 
        Geographic location of the device in the format latitude, longitude, and potentially altitude.  

        Returns:
            The GisPoint property value.

        The format is "POINT (LATITUDE LONGITUDE)" and if you want to clear the 
        coordinates, the value to use is "POINT EMPTY".  
        Examples: "POINT (55.656932878513 12.3763545558449)" "POINT EMPTY".
        Can also include altitude; if so the format is "POINT (LATITUDE LONGITUDE ALTITUDE)".

        The value determines the position of the device icon on the smart map in XProtect Smart Client.
        """
        return self._fGisPoint

    @GisPoint.setter
    def GisPoint(self, value:str) -> None:
        """ 
        Sets the GisPoint property value.
        """
        if value != None:
            self._fGisPoint = value


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
    def Icon(self) -> int:
        """ 
        Icon identifier. The relevant device icon to show.

        Returns:
            The Icon property value.
        """
        return self._fIcon

    @Icon.setter
    def Icon(self, value:int) -> None:
        """ 
        Sets the Icon property value.
        """
        if value != None:
            self._fIcon = value


    @property
    def Name(self) -> str:
        """ 
        Name of the device.

        Returns:
            The Name property value.
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


    @property
    def ShortName(self) -> str:
        """ 
        Short name. Used as name in the user interface where appropriate.

        Returns:
            The ShortName property value.

        The maximum length of characters is 128.
        """
        return self._fShortName

    @ShortName.setter
    def ShortName(self, value:str) -> None:
        """ 
        Sets the ShortName property value.
        """
        if value != None:
            self._fShortName = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Name - Description"
        """
        return str.format("{0} - {1}", self.Name or "", self.Description or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWDevice )) and (isinstance(other, XPWDevice )):
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
            if (isinstance(self, XPWDevice )) and (isinstance(other, XPWDevice )):
                return self.Name < other.Name
            return False
