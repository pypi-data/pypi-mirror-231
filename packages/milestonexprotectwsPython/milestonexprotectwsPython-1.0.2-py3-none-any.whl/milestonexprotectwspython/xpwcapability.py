"""
Module: xpwcapability.py

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
# none

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWCapability:
    """
    Camera Capability information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fAbsolute:bool = False
        self._fAutomatic:bool = None
        self._fCapabilityId:str = None
        self._fName:str = None
        self._fRelative:bool = None
        self._fSpeed:bool = None
        self._fStart:bool = None
        self._fStop:bool = None


    @property
    def Absolute(self) -> bool:
        """ 
        Gets the Absolute property value.

        Returns:
            The Absolute property value.
        """
        return self._fAbsolute

    @Absolute.setter
    def Absolute(self, value:bool) -> None:
        """ 
        Sets the Absolute property value.
        """
        if value != None:
            self._fAbsolute = value


    @property
    def Automatic(self) -> bool:
        """ 
        Gets the Automatic property value.

        Returns:
            The Automatic property value.
        """
        return self._fAutomatic

    @Automatic.setter
    def Automatic(self, value:bool) -> None:
        """ 
        Sets the Automatic property value.
        """
        if value != None:
            self._fAutomatic = value


    @property
    def CapabilityId(self) -> str:
        """ 
        Gets the CapabilityId property value.

        Returns:
            The globally unique identifier of the capability.
        """
        return self._fCapabilityId

    @CapabilityId.setter
    def CapabilityId(self, value:str) -> None:
        """ 
        Sets the CapabilityId property value.
        """
        if value != None:
            self._fCapabilityId = value


    @property
    def Name(self) -> str:
        """ 
        Gets the Name property value.

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
    def Relative(self) -> bool:
        """ 
        Gets the Relative property value.

        Returns:
            The Relative property value.
        """
        return self._fRelative

    @Relative.setter
    def Relative(self, value:bool) -> None:
        """ 
        Sets the Relative property value.
        """
        if value != None:
            self._fRelative = value


    @property
    def Speed(self) -> bool:
        """ 
        Gets the Speed property value.

        Returns:
            The Speed property value.
        """
        return self._fSpeed

    @Speed.setter
    def Speed(self, value:bool) -> None:
        """ 
        Sets the Speed property value.
        """
        if value != None:
            self._fSpeed = value


    @property
    def Start(self) -> bool:
        """ 
        Gets the Start property value.

        Returns:
            The Start property value.
        """
        return self._fStart

    @Start.setter
    def Start(self, value:bool) -> None:
        """ 
        Sets the Start property value.
        """
        if value != None:
            self._fStart = value


    @property
    def Stop(self) -> bool:
        """ 
        Gets the Stop property value.

        Returns:
            The Stop property value.
        """
        return self._fStop

    @Stop.setter
    def Stop(self, value:bool) -> None:
        """ 
        Sets the Stop property value.
        """
        if value != None:
            self._fStop = value


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
            if (isinstance(self, XPWCapability)) and (isinstance(other, XPWCapability)):
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
            if (isinstance(self, XPWCapability)) and (isinstance(other, XPWCapability)):
                return self.Name < other.Name
            return False
