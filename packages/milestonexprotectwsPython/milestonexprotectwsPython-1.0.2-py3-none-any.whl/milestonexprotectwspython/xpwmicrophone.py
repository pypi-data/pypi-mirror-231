"""
Module: xpwmicrophone.py

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
from .xpwdevice import XPWDevice
from .xpwmicrophonesecurity import XPWMicrophoneSecurity
from .xpwtrack import XPWTrack

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWMicrophone(XPWDevice):
    """
    Microphone device information.
    
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
        self._fCoverageDepth:float = None
        self._fCoverageDirection:float = None
        self._fCoverageFieldOfView:float = None
        self._fEdgeStoragePlayback:bool = False
        self._fEdgeStorageSupported:bool = False
        self._fMicrophoneSecurity:XPWMicrophoneSecurity = XPWMicrophoneSecurity()
        self._fMulticastEnabled:bool = False
        self._fStopManualRecordingSeconds:int = None
        self._fTracks:XPWCollection = XPWCollection((XPWTrack))


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
    def MicrophoneSecurity(self) -> XPWMicrophoneSecurity:
        """ 
        Security settings.

        Returns:
            The MicrophoneSecurity property value.
        """
        return self._fMicrophoneSecurity


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
            if (isinstance(self, XPWMicrophone )) and (isinstance(other, XPWMicrophone )):
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
            if (isinstance(self, XPWMicrophone )) and (isinstance(other, XPWMicrophone )):
                return self.Name < other.Name
            return False
