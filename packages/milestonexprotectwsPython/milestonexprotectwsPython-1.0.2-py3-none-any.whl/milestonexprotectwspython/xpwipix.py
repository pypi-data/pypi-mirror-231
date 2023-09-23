"""
Module: xpwipix.py

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
from .xpwhemisphere import XPWHemisphere
from .xpwposition import XPWPosition

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWIpix:
    """
    Camera IPix information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fCeilingMounted:bool = False
        self._fHemisphere:XPWHemisphere = XPWHemisphere()
        self._fHomeposition:XPWPosition = XPWPosition()
        self._fIpixEnabled:bool = None

 
    @property
    def CeilingMounted(self) -> bool:
        """ 
        Gets the CeilingMounted property value.

        Returns:
            The CeilingMounted property value.
        """
        return self._fCeilingMounted

    @CeilingMounted.setter
    def CeilingMounted(self, value:bool) -> None:
        """ 
        Sets the CeilingMounted property value.
        """
        if value != None:
            self._fCeilingMounted = value


    @property
    def Hemisphere(self) -> XPWHemisphere:
        """ 
        Gets the Hemisphere property value.

        Returns:
            The Hemisphere property value.
        """
        return self._fHemisphere

    @property
    def Homeposition(self) -> XPWPosition:
        """ 
        Gets the Homeposition property value.

        Returns:
            The Homeposition property value.
        """
        return self._fHomeposition

    @property
    def IpixEnabled(self) -> bool:
        """ 
        Gets the IpixEnabled property value.

        Returns:
            The IpixEnabled property value.
        """
        return self._fIpixEnabled

    @IpixEnabled.setter
    def IpixEnabled(self, value:bool) -> None:
        """ 
        Sets the IpixEnabled property value.
        """
        if value != None:
            self._fIpixEnabled = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "CeilingMounted = {0}"
        """
        return str.format("CeilingMounted = {0}", self.CeilingMounted or "")
