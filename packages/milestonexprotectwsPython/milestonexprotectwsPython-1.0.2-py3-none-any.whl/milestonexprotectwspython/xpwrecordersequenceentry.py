"""
Module: xpwrecordersequenceentry.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""

# external package imports.
from datetime import datetime

# our package imports.
# none

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWRecorderSequenceEntry:
    """
    Represents a sequence type.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fTimeTrigged:datetime = None
        self._fTimeBegin:datetime = None
        self._fTimeEnd:datetime = None

        # example:

        #<SequenceEntry>
        #  <TimeBegin>2023-07-20T18:52:49.0530000Z</TimeBegin>
        #  <TimeTrigged>2023-07-20T18:52:49.0530000Z</TimeTrigged>
        #  <TimeEnd>2023-07-20T18:53:01.0290000Z</TimeEnd>
        #</SequenceEntry>

    @property
    def TimeTrigged(self) -> datetime:
        """ 
        Gets the TimeTrigged property value.

        Returns:
            The date and time the recording was triggered, in UTC format.
        """
        return self._fTimeTrigged

    @TimeTrigged.setter
    def TimeTrigged(self, value:datetime) -> None:
        """ 
        Sets the TimeTrigged property value.
        """
        if value != None:
            self._fTimeTrigged = value


    @property
    def TimeBegin(self) -> datetime:
        """ 
        Gets the TimeBegin property value.

        Returns:
            The date and time the recording began, in UTC format.
        """
        return self._fTimeBegin

    @TimeBegin.setter
    def TimeBegin(self, value:datetime) -> None:
        """ 
        Sets the TimeBegin property value.
        """
        if value != None:
            self._fTimeBegin = value


    @property
    def TimeEnd(self) -> datetime:
        """ 
        Gets the TimeEnd property value.

        Returns:
            The date and time the recording ended, in UTC format.
        """
        return self._fTimeEnd

    @TimeEnd.setter
    def TimeEnd(self, value:datetime) -> None:
        """ 
        Sets the TimeEnd property value.
        """
        if value != None:
            self._fTimeEnd = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "{TimeBegin} to {TimeEnd}"
        """
        return str.format("{0} to {1}", self.TimeBegin or "", self.TimeEnd or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.TimeBegin == other.TimeBegin
        except Exception as ex:
            if (isinstance(self, XPWRecorderSequenceEntry)) and (isinstance(other, XPWRecorderSequenceEntry)):
                return self.TimeBegin == other.TimeBegin
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(key=lambda x: x.TimeBegin or "", reverse=False)     <- GOOD syntax
            # epColl.sort(key=lambda x: x.TimeBegin, reverse=False)           <- BAD syntax, as the "x.TimeBegin" property may be None, and will cause this to fail!
            return self.TimeBegin < other.TimeBegin
        except Exception as ex:
            if (isinstance(self, XPWRecorderSequenceEntry)) and (isinstance(other, XPWRecorderSequenceEntry)):
                return self.TimeBegin < other.TimeBegin
            return False
