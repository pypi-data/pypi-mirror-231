"""
Module: xpwpanoramiclens.py

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
from .xpwimmervision import XPWImmerVision

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWPanoramicLens:
    """
    Camera Panoramic Lense information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fCameraMount:str = None
        self._fImmerVision:XPWImmerVision = XPWImmerVision()
        self._fPanoramicLensEnabled:bool = None
        self._fPanoramicLensType:str = None


    @property
    def CameraMount(self) -> str:
        """ 
        Gets the CameraMount property value.

        Returns:
            The camera mount type (e.g. "ceiling", "wall", "ground", etc).
        """
        return self._fCameraMount

    @CameraMount.setter
    def CameraMount(self, value:str) -> None:
        """ 
        Sets the CameraMount property value.
        """
        if value != None:
            self._fCameraMount = value


    @property
    def ImmerVision(self) -> str:
        """ 
        Gets the ImmerVision property value.

        Returns:
            The ImmerVision property value.
        """
        return self._fImmerVision


    @property
    def PanoramicLensEnabled(self) -> bool:
        """ 
        Gets the PanoramicLensEnabled property value.

        Returns:
            The PanoramicLensEnabled property value.
        """
        return self._fPanoramicLensEnabled

    @PanoramicLensEnabled.setter
    def PanoramicLensEnabled(self, value:bool) -> None:
        """ 
        Sets the PanoramicLensEnabled property value.
        """
        if value != None:
            self._fPanoramicLensEnabled = value


    @property
    def PanoramicLensType(self) -> str:
        """ 
        Gets the PanoramicLensType property value.

        Returns:
            The type of panoramic lens (e.g. "immervision", etc).
        """
        return self._fPanoramicLensType

    @PanoramicLensType.setter
    def PanoramicLensType(self, value:str) -> None:
        """ 
        Sets the PanoramicLensType property value.
        """
        if value != None:
            self._fPanoramicLensType = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "CameraMount = {0}"
        """
        return str.format("CameraMount = {0}", self.CameraMount or "")
