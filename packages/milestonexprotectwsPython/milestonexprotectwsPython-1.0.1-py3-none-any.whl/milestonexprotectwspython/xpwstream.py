"""
Module: xpwstream.py

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
class XPWStream:
    """
    Stream information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fDefault:bool = None
        self._fName:str = None
        self._fStreamId:str = None


    @property
    def Default(self) -> bool:
        """ 
        Gets the Default property value.

        Returns:
            The track Default value.
        """
        return self._fDefault

    @Default.setter
    def Default(self, value:bool) -> None:
        """ 
        Sets the Default property value.
        """
        if value != None:
            self._fDefault = value


    @property
    def Name(self) -> str:
        """ 
        Gets the Name property value.

        Returns:
            The user-friendly name of the stream.
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
    def StreamId(self) -> str:
        """ 
        Gets the StreamId property value.

        Returns:
            The globally unique identifier of the track.
        """
        return self._fStreamId

    @StreamId.setter
    def StreamId(self, value:str) -> None:
        """ 
        Sets the StreamId property value.
        """
        if value != None:
            self._fStreamId = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Name - StreamId"
        """
        return str.format("{0} - {1}", self.Name or "", self.StreamId or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWStream)) and (isinstance(other, XPWStream)):
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
            if (isinstance(self, XPWStream)) and (isinstance(other, XPWStream)):
                return self.Name < other.Name
            return False
