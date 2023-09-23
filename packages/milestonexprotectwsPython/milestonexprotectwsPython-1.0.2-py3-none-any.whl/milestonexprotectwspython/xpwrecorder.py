"""
Module: xpwrecorder.py

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
from .xpwcamera import XPWCamera
from .xpwcollection import XPWCollection
from .xpwhardware import XPWHardware
from .xpwinput import XPWInput
from .xpwmetadatadevice import XPWMetadataDevice
from .xpwmicrophone import XPWMicrophone
from .xpwoutput import XPWOutput
from .xpwspeaker import XPWSpeaker

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWRecorder:
    """
    Recording Server information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fCameras:XPWCollection = XPWCollection((XPWCamera))
        self._fDefaultRecordingTimeSeconds:int = None
        self._fDescription:str = None
        self._fHardware:XPWCollection = XPWCollection((XPWHardware))
        self._fHostName:str = None
        self._fInputs:XPWCollection = XPWCollection((XPWInput))
        self._fLastModified:datetime = None
        self._fName:str = None
        self._fMetadataDevices:XPWCollection = XPWCollection((XPWMetadataDevice))
        self._fMicrophones:XPWCollection = XPWCollection((XPWMicrophone))
        self._fOutputs:XPWCollection = XPWCollection((XPWOutput))
        self._fRecorderId:str = None
        self._fServiceId:str = None
        self._fSpeakers:XPWCollection = XPWCollection((XPWSpeaker))
        self._fTimeZoneName:str = None
        self._fWebServerUri:str = None
        self._fXmlEncoding:str = None


    @property
    def Cameras(self) -> XPWCollection:
        """ 
        Gets the Cameras property value.

        Returns:
            A collection of XPCamerInfo objects that contain camera device definitions.
        """
        return self._fCameras


    @property
    def DefaultRecordingTimeSeconds(self) -> int:
        """ 
        Gets the DefaultRecordingTimeSeconds property value.

        Returns:
            The default amount of time (in seconds) of a recording.
        """
        return self._fDefaultRecordingTimeSeconds

    @DefaultRecordingTimeSeconds.setter
    def DefaultRecordingTimeSeconds(self, value:int) -> None:
        """ 
        Sets the DefaultRecordingTimeSeconds property value.
        """
        if value != None:
            self._fDefaultRecordingTimeSeconds = value


    @property
    def Description(self) -> str:
        """ 
        Gets the Description property value.

        Returns:
            A description of what the recording server provides.
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
    def Hardware(self) -> XPWCollection:
        """ 
        Gets the Hardware property value.

        Returns:
            A collection of XPWHardware objects that are managed by the Recording server.
        """
        return self._fHardware


    @property
    def HostName(self) -> str:
        """ 
        Gets the HostName property value.

        Returns:
            The computer name that hosts the recording server.
        """
        return self._fHostName

    @HostName.setter
    def HostName(self, value:str) -> None:
        """ 
        Sets the HostName property value.
        """
        if value != None:
            self._fHostName = value


    @property
    def Inputs(self) -> XPWCollection:
        """ 
        Gets the Inputs property value.

        Returns:
            A collection of XPWInput objects that contain Input device definitions.
        """
        return self._fInputs


    @property
    def LastModified(self) -> datetime:
        """ 
        Gets the LastModified property value.

        Returns:
            The date and time the recording server was last modified, in UTC format.
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
            A user-friendly name of the recording server.
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
    def MetadataDevices(self) -> XPWCollection:
        """ 
        Gets the MetadataDevices property value.

        Returns:
            A collection of XPWMetadataDevice objects that contain Metadata device definitions.
        """
        return self._fMetadataDevices


    @property
    def Microphones(self) -> XPWCollection:
        """ 
        Gets the Microphones property value.

        Returns:
            A collection of XPWMicrophone objects that contain microphone device definitions.
        """
        return self._fMicrophones


    @property
    def Outputs(self) -> XPWCollection:
        """ 
        Gets the Outputs property value.

        Returns:
            A collection of XPWOutput objects that contain Input device definitions.
        """
        return self._fOutputs


    @property
    def RecorderId(self) -> str:
        """ 
        Gets the RecorderId property value.

        Returns:
            The globally unique identifier of the recoring server.
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
    def ServiceId(self) -> str:
        """ 
        Gets the ServiceId property value.

        Returns:
            The globally unique identifier of the recoring server service task.
        """
        return self._fServiceId

    @ServiceId.setter
    def ServiceId(self, value:str) -> None:
        """ 
        Sets the ServiceId property value.
        """
        if value != None:
            self._fServiceId = value


    @property
    def Speakers(self) -> XPWCollection:
        """ 
        Gets the Speakers property value.

        Returns:
            A collection of XPWSpeaker objects that contain speaker device definitions.
        """
        return self._fSpeakers


    @property
    def TimeZoneName(self) -> str:
        """ 
        Gets the TimeZoneName property value.

        Returns:
            The time-zone name the recording server is running in.
        """
        return self._fTimeZoneName

    @TimeZoneName.setter
    def TimeZoneName(self, value:str) -> None:
        """ 
        Sets the TimeZoneName property value.
        """
        if value != None:
            self._fTimeZoneName = value


    @property
    def WebServerUri(self) -> str:
        """ 
        Gets the WebServerUri property value.

        Returns:
            The URI used to access web-services hosted by the recording server.
        """
        return self._fWebServerUri

    @WebServerUri.setter
    def WebServerUri(self, value:str) -> None:
        """ 
        Sets the WebServerUri property value.
        """
        if value != None:
            self._fWebServerUri = value


    @property
    def XmlEncoding(self) -> str:
        """ 
        Gets the XmlEncoding property value.

        Returns:
            The supported XML encoding value (e.g. "utf-8", etc).
        """
        return self._fXmlEncoding

    @XmlEncoding.setter
    def XmlEncoding(self, value:str) -> None:
        """ 
        Sets the XmlEncoding property value.
        """
        if value != None:
            self._fXmlEncoding = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Name = Description"
        """
        return str.format("{0} = {1}", self.Name or "", self.Description or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWRecorder)) and (isinstance(other, XPWRecorder)):
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
            if (isinstance(self, XPWRecorder)) and (isinstance(other, XPWRecorder)):
                return self.Name < other.Name
            return False
