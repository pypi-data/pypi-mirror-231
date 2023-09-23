"""
Module: xpwptz.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
# none.

# our package imports.
from .xpwcapability import XPWCapability
from .xpwcollection import XPWCollection
from .xpwpreset import XPWPreset


# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWPtz:
    """
    Camera PTZ information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fCapabilities:XPWCollection = XPWCollection((XPWCapability))
        self._fEditPreset:bool = False
        self._fIsCenterOnPositionInViewSupported:bool = False
        self._fIsPtzCenterAndZoomToRectangleSupported:bool = False
        self._fIsPtzDiagonalSupported:bool = False
        self._fIsPtzHomeSupported:bool = False
        self._fPresets:XPWCollection = XPWCollection((XPWPreset))
        self._fPtzEnabled:bool = False


    @property
    def Capabilities(self) -> XPWCollection:
        """ 
        Gets the Capabilities property value.

        Returns:
            The Capabilities property value.
        """
        return self._fCapabilities


    @property
    def EditPreset(self) -> bool:
        """ 
        Gets the EditPreset property value.

        Returns:
            The EditPreset property value.
        """
        return self._fEditPreset

    @EditPreset.setter
    def EditPreset(self, value:bool) -> None:
        """ 
        Sets the EditPreset property value.
        """
        if value != None:
            self._fEditPreset = value


    @property
    def IsCenterOnPositionInViewSupported(self) -> bool:
        """ 
        Gets the IsCenterOnPositionInViewSupported property value.

        Returns:
            The IsCenterOnPositionInViewSupported property value.
        """
        return self._fIsCenterOnPositionInViewSupported

    @IsCenterOnPositionInViewSupported.setter
    def IsCenterOnPositionInViewSupported(self, value:bool) -> None:
        """ 
        Sets the IsCenterOnPositionInViewSupported property value.
        """
        if value != None:
            self._fIsCenterOnPositionInViewSupported = value


    @property
    def IsPtzCenterAndZoomToRectangleSupported(self) -> bool:
        """ 
        Gets the IsPtzCenterAndZoomToRectangleSupported property value.

        Returns:
            The IsPtzCenterAndZoomToRectangleSupported property value.
        """
        return self._fIsPtzCenterAndZoomToRectangleSupported

    @IsPtzCenterAndZoomToRectangleSupported.setter
    def IsPtzCenterAndZoomToRectangleSupported(self, value:bool) -> None:
        """ 
        Sets the IsPtzCenterAndZoomToRectangleSupported property value.
        """
        if value != None:
            self._fIsPtzCenterAndZoomToRectangleSupported = value


    @property
    def IsPtzDiagonalSupported(self) -> bool:
        """ 
        Gets the IsPtzDiagonalSupported property value.

        Returns:
            The IsPtzDiagonalSupported property value.
        """
        return self._fIsPtzDiagonalSupported

    @IsPtzDiagonalSupported.setter
    def IsPtzDiagonalSupported(self, value:bool) -> None:
        """ 
        Sets the IsPtzDiagonalSupported property value.
        """
        if value != None:
            self._fIsPtzDiagonalSupported = value


    @property
    def IsPtzHomeSupported(self) -> bool:
        """ 
        Gets the IsPtzHomeSupported property value.

        Returns:
            The IsPtzHomeSupported property value.
        """
        return self._fIsPtzHomeSupported

    @IsPtzHomeSupported.setter
    def IsPtzHomeSupported(self, value:bool) -> None:
        """ 
        Sets the IsPtzHomeSupported property value.
        """
        if value != None:
            self._fIsPtzHomeSupported = value


    @property
    def Presets(self) -> XPWCollection:
        """ 
        Gets the Presets property value.

        Returns:
            The Presets property value.
        """
        return self._fPresets


    @property
    def PtzEnabled(self) -> bool:
        """ 
        Gets the PtzEnabled property value.

        Returns:
            The PtzEnabled property value.
        """
        return self._fPtzEnabled

    @PtzEnabled.setter
    def PtzEnabled(self, value:bool) -> None:
        """ 
        Sets the PtzEnabled property value.
        """
        if value != None:
            self._fPtzEnabled = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "EditPreset = {EditPreset}"
        """
        return str.format("EditPreset = {0}", self.EditPreset or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.EditPreset == other.EditPreset
        except Exception as ex:
            if (isinstance(self, XPWPtz)) and (isinstance(other, XPWPtz)):
                return self.EditPreset == other.EditPreset
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(EditPreset=lambda x: x.EditPreset or "", reverse=False)     <- GOOD syntax
            # epColl.sort(EditPreset=lambda x: x.EditPreset, reverse=False)           <- BAD syntax, as the "x.EditPreset" property may be None, and will cause this to fail!
            return self.EditPreset < other.EditPreset
        except Exception as ex:
            if (isinstance(self, XPWPtz)) and (isinstance(other, XPWPtz)):
                return self.EditPreset < other.EditPreset
            return False
