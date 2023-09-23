"""
Module: xpwconfiguration.py

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
from .xpwalerttype import XPWAlertType
from .xpwalerttypegroup import XPWAlertTypeGroup
from .xpwapplicationsecurity import XPWApplicationSecurity
from .xpwaudiomessage import XPWAudioMessage
from .xpwbookmarksettings import XPWBookmarkSettings
from .xpwcameragroup import XPWCameraGroup
from .xpwcollection import XPWCollection
from .xpwdevicemapping import XPWDeviceMapping
from .xpweventtype import XPWEventType
from .xpweventtypegroup import XPWEventTypeGroup
from .xpwinputgroup import XPWInputGroup
from .xpwlicense import XPWLicense
from .xpwmatrixmonitor import XPWMatrixMonitor
from .xpwmicrophonegroup import XPWMicrophoneGroup
from .xpwoutputgroup import XPWOutputGroup
from .xpwrecorder import XPWRecorder
from .xpwretentionoption import XPWRetentionOption
from .xpwserveroption import XPWServerOption
from .xpwspeakergroup import XPWSpeakerGroup
from .xpwsystemeventtype import XPWSystemEventType

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWConfiguration:
    """
    Represents configuration information for an XProtect Management server.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fAlertTypeGroups:XPWCollection = XPWCollection((XPWAlertTypeGroup))
        self._fAlertTypes:XPWCollection = XPWCollection((XPWAlertType))
        self._fApplicationAccess:XPWApplicationSecurity = XPWApplicationSecurity()
        self._fAudioMessages:XPWAudioMessage = XPWAudioMessage()
        self._fBookmarkSettings:XPWBookmarkSettings = XPWBookmarkSettings()
        self._fCameraGroups:XPWCollection = XPWCollection((XPWCameraGroup))
        self._fDeviceMappings:XPWCollection = XPWCollection((XPWDeviceMapping))
        self._fEventTypeGroups:XPWCollection = XPWCollection((XPWEventTypeGroup))
        self._fEventTypes:XPWCollection = XPWCollection((XPWEventType))
        self._fFailoverCheckInterval:int = None
        self._fInputGroups:XPWCollection = XPWCollection((XPWInputGroup))
        self._fLicenses:XPWCollection = XPWCollection((XPWLicense))
        self._fMatrixMonitors:XPWCollection = XPWCollection((XPWMatrixMonitor))
        self._fMicrophoneGroups:XPWCollection = XPWCollection((XPWMicrophoneGroup))
        self._fOutputGroups:XPWCollection = XPWCollection((XPWOutputGroup))
        self._fRecorders:XPWCollection = XPWCollection((XPWRecorder))
        self._fRetentionOptions:XPWCollection = XPWCollection((XPWRetentionOption))
        self._fServerDescription:str = None
        self._fServerId:str = None
        self._fServerName:str = None
        self._fServerOptions:XPWCollection = XPWCollection((XPWServerOption))
        self._fSpeakerGroups:XPWCollection = XPWCollection((XPWSpeakerGroup))
        self._fSystemEventTypes:XPWCollection = XPWCollection((XPWSystemEventType))

        # I could not find docs on the following property, but the web-service wsdl lists it as being returned.
        # I would think it
        # https://doc.developer.milestonesys.com/html/MIPhelp/class_video_o_s_1_1_platform_1_1_configuration_items_1_1_metadata_group.html
        #<MetadataDeviceGroups/>  


    @property
    def AlertTypeGroups(self) -> XPWCollection:
        """ 
        A collection of XPWAlertTypeGroup objects.

        Returns:
            The AlertTypeGroups property value.
        """
        return self._fAlertTypeGroups


    @property
    def AlertTypes(self) -> XPWCollection:
        """ 
        A collection of XPWAlertType objects.

        Returns:
            The AlertTypes property value.
        """
        return self._fAlertTypes


    @property
    def AudioMessages(self) -> XPWAudioMessage:
        """ 
        Audio Message information.

        Returns:
            The AudioMessages property value.
        """
        return self._fAudioMessages


    @property
    def ApplicationAccess(self) -> XPWApplicationSecurity:
        """ 
        Application Access Security settings.

        Returns:
            The ApplicationAccess property value.
        """
        return self._fApplicationAccess


    @property
    def BookmarkSettings(self) -> XPWBookmarkSettings:
        """ 
        Bookmark settings.

        Returns:
            The BookmarkSettings property value.
        """
        return self._fCameraGroups


    @property
    def CameraGroups(self) -> XPWCollection:
        """ 
        A collection of XPWCameraGroup objects.

        Returns:
            The CameraGroups property value.
        """
        return self._fCameraGroups


    @property
    def DeviceMappings(self) -> XPWCollection:
        """ 
        A collection of XPWDeviceMapping objects.

        Returns:
            The DeviceMappings property value.
        """
        return self._fDeviceMappings


    @property
    def EventTypeGroups(self) -> XPWCollection:
        """ 
        A collection of XPWEventTypeGroup objects.

        Returns:
            The EventTypeGroups property value.
        """
        return self._fEventTypeGroups


    @property
    def EventTypes(self) -> XPWCollection:
        """ 
        A collection of XPWEventType objects.

        Returns:
            The EventTypes property value.
        """
        return self._fEventTypes


    @property
    def FailoverCheckInterval(self) -> int:
        """ 
        The FailoverCheckInterval property value.

        Returns:
            The FailoverCheckInterval property value.
        """
        return self._fFailoverCheckInterval

    @FailoverCheckInterval.setter
    def FailoverCheckInterval(self, value:int) -> None:
        """ 
        Sets the FailoverCheckInterval property value.
        """
        if value != None:
            self._fFailoverCheckInterval = value


    @property
    def InputGroups(self) -> XPWCollection:
        """ 
        A collection of XPWInputGroup objects.

        Returns:
            The InputGroups property value.
        """
        return self._fInputGroups


    @property
    def Licenses(self) -> XPWCollection:
        """ 
        A collection of XPWLicense objects.

        Returns:
            The Licenses property value.
        """
        return self._fLicenses


    @property
    def MatrixMonitors(self) -> XPWCollection:
        """ 
        A collection of XPWMatrixMonitor objects.

        Returns:
            The MatrixMonitors property value.
        """
        return self._fMatrixMonitors


    @property
    def MicrophoneGroups(self) -> XPWCollection:
        """ 
        A collection of XPWMicrophoneGroup objects.

        Returns:
            The MicrophoneGroups property value.
        """
        return self._fMicrophoneGroups


    @property
    def OutputGroups(self) -> XPWCollection:
        """ 
        A collection of XPWOutputGroup objects.

        Returns:
            The OutputGroups property value.
        """
        return self._fOutputGroups


    @property
    def Recorders(self) -> XPWCollection:
        """ 
        A collection of XPWRecorder objects that represent configured
        XProtect Recording Servers.

        Returns:
            The Recorders property value.
        """
        return self._fRecorders


    @property
    def RetentionOptions(self) -> XPWCollection:
        """ 
        A collection of XPWRetentionOption objects.

        Returns:
            The RetentionOptions property value.
        """
        return self._fRetentionOptions


    @property
    def ServerDescription(self) -> str:
        """ 
        A short description of the server.

        Returns:
            The ServerDescription property value.
        """
        return self._fServerDescription

    @ServerDescription.setter
    def ServerDescription(self, value:str) -> None:
        """ 
        Sets the ServerDescription property value.
        """
        if value != None:
            self._fServerDescription = value


    @property
    def ServerId(self) -> str:
        """ 
        Globally unique identifier of the server.

        Returns:
            The ServerId property value.
        """
        return self._fServerId

    @ServerId.setter
    def ServerId(self, value:str) -> None:
        """ 
        Sets the ServerId property value.
        """
        if value != None:
            self._fServerId = value


    @property
    def ServerName(self) -> str:
        """ 
        Name of the server.

        Returns:
            The ServerName property value.
        """
        return self._fServerName

    @ServerName.setter
    def ServerName(self, value:str) -> None:
        """ 
        Sets the ServerName property value.
        """
        if value != None:
            self._fServerName = value


    @property
    def ServerOptions(self) -> XPWCollection:
        """ 
        A collection of XPWServerOption objects.

        Returns:
            The ServerOptions property value.
        """
        return self._fServerOptions


    @property
    def SpeakerGroups(self) -> XPWCollection:
        """ 
        A collection of XPWSpeakerGroup objects.

        Returns:
            The SpeakerGroups property value.
        """
        return self._fSpeakerGroups


    @property
    def SystemEventTypes(self) -> XPWCollection:
        """ 
        A collection of XPWSystemEventType objects.

        Returns:
            The SystemEventTypes property value.
        """
        return self._fSystemEventTypes


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "ServerName - ServerDescription"
        """
        return str.format("{0} - {1}", self.ServerName or "", self.ServerDescription or "")
