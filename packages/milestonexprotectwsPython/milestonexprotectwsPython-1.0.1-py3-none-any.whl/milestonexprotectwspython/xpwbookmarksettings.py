"""
Module: xpwbookmarksettings.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | DefaultPostTimeSec
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
class XPWBookmarkSettings:
    """
    Bookmark Settings information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fDefaultPostTimeSec:int = None
        self._fDefaultPreTimeSec:int = None


    @property
    def DefaultPostTimeSec(self) -> int:
        """ 
        Specifies the bookmark default stop time (in seconds).

        Returns:
            The DefaultPostTimeSec property value.
        """
        return self._fDefaultPostTimeSec

    @DefaultPostTimeSec.setter
    def DefaultPostTimeSec(self, value:int) -> None:
        """ 
        Sets the DefaultPostTimeSec property value.
        """
        if value != None:
            self._fDefaultPostTimeSec = value


    @property
    def DefaultPreTimeSec(self) -> int:
        """ 
        Specifies the bookmark default start time (in seconds).

        Returns:
            The DefaultPreTimeSec property value.
        """
        return self._fDefaultPreTimeSec

    @DefaultPreTimeSec.setter
    def DefaultPreTimeSec(self, value:int) -> None:
        """ 
        Sets the DefaultPreTimeSec property value.
        """
        if value != None:
            self._fDefaultPreTimeSec = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Bookmark Time: Pre={0}, Post={1}"
        """
        return str.format("Bookmark Time: Pre={0}, Post={1}", self.DefaultPreTimeSec or "", self.DefaultPostTimeSec or "")
