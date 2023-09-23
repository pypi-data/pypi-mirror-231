"""
Module: xpwcamera.py

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
from .xpwcamerasecurity import XPWCameraSecurity
from .xpwdevice import XPWDevice
from .xpwpanoramiclens import XPWPanoramicLens
from .xpwipix import XPWIpix
from .xpwstream import XPWStream
from .xpwtrack import XPWTrack
from .xpwptz import XPWPtz

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWCamera(XPWDevice):
    """
    Camera device information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize base class instance.
        super().__init__()

        # initialize instance.
        self._fBrowsableStream:bool = False
        self._fCameraSecurity:XPWCameraSecurity = XPWCameraSecurity()
        self._fCoverageDepth:float = None
        self._fCoverageDirection:float = None
        self._fCoverageFieldOfView:float = None
        self._fEdgeStoragePlayback:bool = False
        self._fEdgeStorageSupported:bool = False
        self._fIpixSettings:XPWIpix = XPWIpix()
        self._fMaxFPS:int = None
        self._fMulticastEnabled:bool = False
        self._fPanoramicLensSettings:XPWPanoramicLens = XPWPanoramicLens()
        self._fPtzSettings:XPWPtz = XPWPtz()
        self._fStopManualRecordingSeconds:int = None
        self._fStreams:XPWCollection = XPWCollection((XPWStream))
        self._fTracks:XPWCollection = XPWCollection((XPWTrack))


    @property
    def BrowsableStream(self) -> bool:
        """ 
        Gets the BrowsableStream property value.

        Returns:
            The BrowsableStream property value.
        """
        return self._fBrowsableStream

    @BrowsableStream.setter
    def BrowsableStream(self, value:bool) -> None:
        """ 
        Sets the BrowsableStream property value.
        """
        if value != None:
            self._fBrowsableStream = value


    @property
    def CameraSecurity(self) -> XPWCameraSecurity:
        """ 
        Security settings.

        Returns:
            The CameraSecurity property value.
        """
        return self._fCameraSecurity


    @property
    def CoverageDepth(self) -> float:
        """ 
        Depth. Indicates the viewing depth of the device.

        Returns:
            The CoverageDepth property value.
        """
        return self._fCoverageDepth

    @CoverageDepth.setter
    def CoverageDepth(self, value:float) -> None:
        """ 
        Sets the CoverageDepth property value.
        """
        if value != None:
            self._fCoverageDepth = value


    @property
    def CoverageDirection(self) -> float:
        """ 
        Direction. Indicate the viewing direction of the device.

        Returns:
            The CoverageDirection property value.
        """
        return self._fCoverageDirection

    @CoverageDirection.setter
    def CoverageDirection(self, value:float) -> None:
        """ 
        Sets the CoverageDirection property value.
        """
        if value != None:
            self._fCoverageDirection = value


    @property
    def CoverageFieldOfView(self) -> float:
        """ 
        Field of view. Indicate the field of view of the device.

        Returns:
            The CoverageFieldOfView property value.
        """
        return self._fCoverageFieldOfView

    @CoverageFieldOfView.setter
    def CoverageFieldOfView(self, value:float) -> None:
        """ 
        Sets the CoverageFieldOfView property value.
        """
        if value != None:
            self._fCoverageFieldOfView = value


    @property
    def EdgeStoragePlayback(self) -> bool:
        """ 
        Gets the EdgeStoragePlayback property value.

        Returns:
            The EdgeStoragePlayback property value.
        """
        return self._fEdgeStoragePlayback

    @EdgeStoragePlayback.setter
    def EdgeStoragePlayback(self, value:bool) -> None:
        """ 
        Sets the EdgeStoragePlayback property value.
        """
        if value != None:
            self._fEdgeStoragePlayback = value


    @property
    def EdgeStorageSupported(self) -> bool:
        """ 
        Gets the EdgeStorageSupported property value.

        Returns:
            The EdgeStorageSupported property value.
        """
        return self._fEdgeStorageSupported

    @EdgeStorageSupported.setter
    def EdgeStorageSupported(self, value:bool) -> None:
        """ 
        Sets the EdgeStorageSupported property value.
        """
        if value != None:
            self._fEdgeStorageSupported = value


    @property
    def IpixSettings(self) -> XPWIpix:
        """ 
        Gets the IpixSettings property value.

        Returns:
            Camera IPix settings.
        """
        return self._fIpixSettings


    @property
    def MaxFPS(self) -> int:
        """ 
        Gets the MaxFPS property value.

        Returns:
            Maximum number of frames per second (FPS) the device supports.
        """
        return self._fMaxFPS

    @MaxFPS.setter
    def MaxFPS(self, value:int) -> None:
        """ 
        Sets the MaxFPS property value.
        """
        if value != None:
            self._fMaxFPS = value


    @property
    def MulticastEnabled(self) -> bool:
        """ 
        Gets the MulticastEnabled property value.

        Returns:
            True if the device has multicast support enabled; otherwise, False.
        """
        return self._fMulticastEnabled

    @MulticastEnabled.setter
    def MulticastEnabled(self, value:bool) -> None:
        """ 
        Sets the MulticastEnabled property value.
        """
        if value != None:
            self._fMulticastEnabled = value


    @property
    def PanoramicLensSettings(self) -> XPWPanoramicLens:
        """ 
        Gets the PanoramicLensSettings property value.

        Returns:
            The PanoramicLensSettings property value.
        """
        return self._fPanoramicLensSettings


    @property
    def PtzSettings(self) -> XPWPtz:
        """ 
        Gets the PtzSettings property value.

        Returns:
            Camera PtzSettings settings.
        """
        return self._fPtzSettings


    @property
    def StopManualRecordingSeconds(self) -> int:
        """ 
        Gets the StopManualRecordingSeconds property value.

        Returns:
            The StopManualRecordingSeconds property value.
        """
        return self._fStopManualRecordingSeconds

    @StopManualRecordingSeconds.setter
    def StopManualRecordingSeconds(self, value:int) -> None:
        """ 
        Sets the StopManualRecordingSeconds property value.
        """
        if value != None:
            self._fStopManualRecordingSeconds = value


    @property
    def Streams(self) -> XPWCollection:
        """ 
        Gets the Streams property value.

        Returns:
            A collection of XPStreamsInfo objects.
        """
        return self._fStreams


    @property
    def Tracks(self) -> XPWCollection:
        """ 
        Gets the Tracks property value.

        Returns:
            A collection of XPWTrack objects.
        """
        return self._fTracks


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWCamera)) and (isinstance(other, XPWCamera)):
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
            if (isinstance(self, XPWCamera)) and (isinstance(other, XPWCamera)):
                return self.Name < other.Name
            return False
