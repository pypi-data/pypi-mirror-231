"""
Module: xpwmetadatatype.py

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
class XPWMetadataType:
    """
    Metadata Type information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fId:str = None
        self._fName:str = None
        self._fDisplayId:str = None
        self._fDisplayName:str = None
        self._fValidTime:str = None


    @property
    def Id(self) -> str:
        """ 
        Globally unique identifier of the metadata type.

        Returns:
            The Id property value.
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
    def Name(self) -> str:
        """ 
        Name of the metadata type.

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
    def DisplayId(self) -> str:
        """ 
        DisplayId of the metadata type.

        Returns:
            The DisplayId property value.
        """
        return self._fDisplayId

    @DisplayId.setter
    def DisplayId(self, value:str) -> None:
        """ 
        Sets the DisplayId property value.
        """
        if value != None:
            self._fDisplayId = value


    @property
    def DisplayName(self) -> str:
        """ 
        DisplayName of the metadata type.

        Returns:
            The DisplayName property value.
        """
        return self._fDisplayName

    @DisplayName.setter
    def DisplayName(self, value:str) -> None:
        """ 
        Sets the DisplayName property value.
        """
        if value != None:
            self._fDisplayName = value


    @property
    def ValidTime(self) -> str:
        """ 
        ValidTime of the metadata type.

        Returns:
            The ValidTime property value.
        """
        return self._fValidTime

    @ValidTime.setter
    def ValidTime(self, value:str) -> None:
        """ 
        Sets the ValidTime property value.
        """
        if value != None:
            self._fValidTime = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "{Name}: {Id}"
        """
        return str.format("{0}: {1}", self.Name or "", self.Id or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.Name == other.Name
        except Exception as ex:
            if (isinstance(self, XPWMetadataType)) and (isinstance(other, XPWMetadataType)):
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
            if (isinstance(self, XPWMetadataType)) and (isinstance(other, XPWMetadataType)):
                return self.Name < other.Name
            return False
