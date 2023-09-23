"""
Module: xpwpreset.py

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
from .xpwposition import XPWPosition

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWPreset:
    """
    Camera Preset information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fId:str = False
        self._fLocked:bool = None
        self._fName:str = False
        self._fPosition:XPWPosition = XPWPosition()
        self._fShortcut:str = False


    @property
    def Id(self) -> str:
        """ 
        Gets the Id property value.

        Returns:
            The globally unique identifier of the preset.
        """
        return self._fId

    @Id.setter
    def Id(self, value:str) -> None:
        """ 
        Sets the Id property value.
        """
        if value != None:
            self._fId = value


    @property
    def Locked(self) -> bool:
        """ 
        Gets the Locked property value.

        Returns:
            The Locked property value.
        """
        return self._fLocked

    @Locked.setter
    def Locked(self, value:bool) -> None:
        """ 
        Sets the Locked property value.
        """
        if value != None:
            self._fLocked = value


    @property
    def Name(self) -> str:
        """ 
        Gets the Name property value.

        Returns:
            The user-friendly name of the preset.
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
    def Position(self) -> XPWPosition:
        """ 
        Gets the Position property value.

        Returns:
            The Position property value.
        """
        return self._fPosition


    @property
    def Shortcut(self) -> str:
        """ 
        Gets the Shortcut property value.

        Returns:
            The user-friendly shortcut name of the preset.
        """
        return self._fShortcut

    @Shortcut.setter
    def Shortcut(self, value:str) -> None:
        """ 
        Sets the Shortcut property value.
        """
        if value != None:
            self._fShortcut = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Name = {0}"
        """
        return str.format("Name = {0}", self.Name or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWPreset)) and (isinstance(other, XPWPreset)):
                return self.Name == other.Name
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(key=lambda x: x.Name or "", reverse=False)     <- GOOD syntax
            # epColl.sort(key=lambda x: x.Name, reverse=False)           <- BAD syntax, as the "x.Name" property may be None, and will cause this to fail!
            return self.Name < other.Name
        except Exception as ex:
            if (isinstance(self, XPWPreset)) and (isinstance(other, XPWPreset)):
                return self.Name < other.Name
            return False
