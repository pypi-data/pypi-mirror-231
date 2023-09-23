"""
Module: xpwrecordersequencetype.py

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
class XPWRecorderSequenceType:
    """
    Represents a sequence type.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    # Sequence Type constants.
    RECORDING_SEQUENCE:str = "F9C62604-D0C5-4050-AE25-72DE51639B14"
    """ 
    Recording sequence type id (F9C62604-D0C5-4050-AE25-72DE51639B14). 
    """
    MOTION_SEQUENCE:str = "53CB5E33-2183-44bd-9491-8364D2457480"
    """ 
    Motion sequence type id (53CB5E33-2183-44bd-9491-8364D2457480). 
    """
    RECORDING_WITH_TRIGGER_SEQUENCE:str = "0601D294-B7E5-4d93-9614-9658561AD5E4"
    """ 
    Recording with trigger sequence type id (0601D294-B7E5-4d93-9614-9658561AD5E4). 
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fId:str = None
        self._fName:str = None

        # example:

        #<SequenceType>
        #  <Id>0601d294-b7e5-4d93-9614-9658561ad5e4</Id>
        #  <Name>RecordingWithTriggerSequence</Name>
        #</SequenceType>

    @property
    def Id(self) -> str:
        """ 
        Gets the Id property value.

        Returns:
            The unique identifier of the sequence type.
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
        Gets the Name property value.

        Returns:
            The name of the sequence type.
        """
        return self._fName

    @Name.setter
    def Name(self, value:str) -> None:
        """ 
        Sets the Name property value.
        """
        if value != None:
            self._fName = value


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
            if (isinstance(self, XPWRecorderSequenceType)) and (isinstance(other, XPWRecorderSequenceType)):
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
            if (isinstance(self, XPWRecorderSequenceType)) and (isinstance(other, XPWRecorderSequenceType)):
                return self.Name < other.Name
            return False
