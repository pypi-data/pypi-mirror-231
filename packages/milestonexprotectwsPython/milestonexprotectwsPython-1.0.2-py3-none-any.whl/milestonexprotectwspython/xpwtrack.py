"""
Module: xpwtrack.py

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
class XPWTrack:
    """
    Server Option information.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fTrackId:str = None
        self._fEdge:bool = None


    @property
    def Edge(self) -> bool:
        """ 
        Gets the Edge property value.

        Returns:
            The track edge value.
        """
        return self._fEdge

    @Edge.setter
    def Edge(self, value:bool) -> None:
        """ 
        Sets the Edge property value.
        """
        if value != None:
            self._fEdge = value


    @property
    def TrackId(self) -> str:
        """ 
        Gets the TrackId property value.

        Returns:
            The globally unique identifier of the track.
        """
        return self._fTrackId

    @TrackId.setter
    def TrackId(self, value:str) -> None:
        """ 
        Sets the TrackId property value.
        """
        if value != None:
            self._fTrackId = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "TrackId - Edge"
        """
        return str.format("{0} - {1}", self.TrackId or "", self.Edge or "")


    # implement sorting support.
    def __eq__(self, other):
        try:
            return self.TrackId == other.TrackId
        except Exception as ex:
            if (isinstance(self, XPWTrack)) and (isinstance(other, XPWTrack)):
                return self.TrackId == other.TrackId
            return False

    def __lt__(self, other):
        try:
            # the following comparison will fail if the property value is None!  
            # use the following syntax when calling a sort method that uses lambda searches:
            # epColl.sort(TrackId=lambda x: x.TrackId or "", reverse=False)     <- GOOD syntax
            # epColl.sort(TrackId=lambda x: x.TrackId, reverse=False)           <- BAD syntax, as the "x.TrackId" property may be None, and will cause this to fail!
            return self.TrackId < other.TrackId
        except Exception as ex:
            if (isinstance(self, XPWTrack)) and (isinstance(other, XPWTrack)):
                return self.TrackId < other.TrackId
            return False
