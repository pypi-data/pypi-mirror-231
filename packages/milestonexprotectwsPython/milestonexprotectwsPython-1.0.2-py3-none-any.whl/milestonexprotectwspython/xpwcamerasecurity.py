"""
Module: xpwcamerasecurity.py

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
from .xpwptzsecurity import XPWPtzSecurity

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWCameraSecurity:
    """
    Camera device Security information.
    
    Supplemental documentation can be found at:
    https://doc.milestonesys.com/2023R2/en-US/standard_features/sf_mc/sf_ui/mc_roles_security.htm?cshid=9902#Camerarelatedpermissions

    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fBookmarkAdd:bool = False
        self._fBookmarkDelete:bool = False
        self._fBookmarkEdit:bool = False
        self._fBookmarkView:bool = False
        self._fBrowse:bool = False
        self._fExportAvi:bool = False
        self._fExportDatabase:bool = False
        self._fExportJpeg:bool = False
        self._fGetSequences:bool = False
        self._fLive:bool = False
        self._fManagePatrollingProfiles:bool = False
        self._fManagePresetLocks:bool = False
        self._fManagePresets:bool = False
        self._fPtzSecurity:XPWPtzSecurity = XPWPtzSecurity()
        self._fRestrictedMediaCreate:bool
        self._fRestrictedMediaRemove:bool = False
        self._fRestrictedMediaView:bool = False
        self._fRetentionCreate:bool = False
        self._fRetentionRemove:bool = False
        self._fRetentionView:bool = False
        self._fRetrieveEdgeRecordings = False
        self._fSmartSearch:bool = False
        self._fStartRecording:bool = False
        self._fStopRecording:bool = False

    @property
    def BookmarkAdd(self) -> bool:
        """ 
        True if the user has access to add a new bookmark for the device; otherwise, False.

        Returns:
            The BookmarkAdd property value.
        """
        return self._fBookmarkAdd

    @BookmarkAdd.setter
    def BookmarkAdd(self, value:bool) -> None:
        """ 
        Sets the BookmarkAdd property value.
        """
        if value != None:
            self._fBookmarkAdd = value


    @property
    def BookmarkDelete(self) -> bool:
        """ 
        True if the user has access to delete an existing bookmark for the device; otherwise, False.

        Returns:
            The BookmarkDelete property value.
        """
        return self._fBookmarkDelete

    @BookmarkDelete.setter
    def BookmarkDelete(self, value:bool) -> None:
        """ 
        Sets the BookmarkDelete property value.
        """
        if value != None:
            self._fBookmarkDelete = value


    @property
    def BookmarkEdit(self) -> bool:
        """ 
        True if the user has access to edit an existing bookmark for the device; otherwise, False.

        Returns:
            The BookmarkEdit property value.
        """
        return self._fBookmarkEdit

    @BookmarkEdit.setter
    def BookmarkEdit(self, value:bool) -> None:
        """ 
        Sets the BookmarkEdit property value.
        """
        if value != None:
            self._fBookmarkEdit = value


    @property
    def BookmarkView(self) -> bool:
        """ 
        True if the user has access to view an existing bookmark for the device; otherwise, False.

        Returns:
            The BookmarkView property value.
        """
        return self._fBookmarkView

    @BookmarkView.setter
    def BookmarkView(self, value:bool) -> None:
        """ 
        Sets the BookmarkView property value.
        """
        if value != None:
            self._fBookmarkView = value


    @property
    def Browse(self) -> bool:
        """ 
        True if the user has access to browse media for the device; otherwise, False.

        Returns:
            The Browse property value.
        """
        return self._fBrowse

    @Browse.setter
    def Browse(self, value:bool) -> None:
        """ 
        Sets the Browse property value.
        """
        if value != None:
            self._fBrowse = value


    @property
    def ExportAvi(self) -> bool:
        """ 
        True if the user has access to export AVI media for the device; otherwise, False.

        Returns:
            The ExportAvi property value.
        """
        return self._fExportAvi

    @ExportAvi.setter
    def ExportAvi(self, value:bool) -> None:
        """ 
        Sets the ExportAvi property value.
        """
        if value != None:
            self._fExportAvi = value


    @property
    def ExportDatabase(self) -> bool:
        """ 
        True if the user has access to export database objects for the device; otherwise, False.

        Returns:
            The ExportDatabase property value.
        """
        return self._fExportDatabase

    @ExportDatabase.setter
    def ExportDatabase(self, value:bool) -> None:
        """ 
        Sets the ExportDatabase property value.
        """
        if value != None:
            self._fExportDatabase = value


    @property
    def ExportJpeg(self) -> bool:
        """ 
        True if the user has access to export JPEG media for the device; otherwise, False.

        Returns:
            The ExportJpeg property value.
        """
        return self._fExportJpeg

    @ExportJpeg.setter
    def ExportJpeg(self, value:bool) -> None:
        """ 
        Sets the ExportJpeg property value.
        """
        if value != None:
            self._fExportJpeg = value


    @property
    def GetSequences(self) -> bool:
        """ 
        True if the user has access to get sequence data for the device; otherwise, False.

        Returns:
            The GetSequences property value.
        """
        return self._fGetSequences

    @GetSequences.setter
    def GetSequences(self, value:bool) -> None:
        """ 
        Sets the GetSequences property value.
        """
        if value != None:
            self._fGetSequences = value


    @property
    def Live(self) -> bool:
        """ 
        True if the user has access to get live data for the device; otherwise, False.

        Returns:
            The Live property value.
        """
        return self._fLive

    @Live.setter
    def Live(self, value:bool) -> None:
        """ 
        Sets the Live property value.
        """
        if value != None:
            self._fLive = value


    @property
    def ManagePatrollingProfiles(self) -> bool:
        """ 
        True if the user has access to manage patrolling profiles for the device; otherwise, False.

        Returns:
            The ManagePatrollingProfiles property value.
        """
        return self._fManagePatrollingProfiles

    @ManagePatrollingProfiles.setter
    def ManagePatrollingProfiles(self, value:bool) -> None:
        """ 
        Sets the ManagePatrollingProfiles property value.
        """
        if value != None:
            self._fManagePatrollingProfiles = value


    @property
    def ManagePresetLocks(self) -> bool:
        """ 
        True if the user has access to manage preset locks for the device; otherwise, False.

        Returns:
            The ManagePresetLocks property value.
        """
        return self._fManagePresetLocks

    @ManagePresetLocks.setter
    def ManagePresetLocks(self, value:bool) -> None:
        """ 
        Sets the ManagePresetLocks property value.
        """
        if value != None:
            self._fManagePresetLocks = value


    @property
    def ManagePresets(self) -> bool:
        """ 
        True if the user has access to manage presets for the device; otherwise, False.

        Returns:
            The ManagePresets property value.
        """
        return self._fManagePresets

    @ManagePresets.setter
    def ManagePresets(self, value:bool) -> None:
        """ 
        Sets the ManagePresets property value.
        """
        if value != None:
            self._fManagePresets = value


    @property
    def PtzSecurity(self) -> XPWPtzSecurity:
        """ 
        PTZ Security settings.

        Returns:
            Camera PTZ Security settings.
        """
        return self._fPtzSecurity


    @property
    def RestrictedMediaCreate(self) -> bool:
        """ 
        True if the user has access to create restricted media for the device; otherwise, False.

        Returns:
            The RestrictedMediaCreate property value.
        """
        return self._fRestrictedMediaCreate

    @RestrictedMediaCreate.setter
    def RestrictedMediaCreate(self, value:bool) -> None:
        """ 
        Sets the RestrictedMediaCreate property value.
        """
        if value != None:
            self._fRestrictedMediaCreate = value


    @property
    def RestrictedMediaRemove(self) -> bool:
        """ 
        True if the user has access to remove restricted media for the device; otherwise, False.

        Returns:
            The RestrictedMediaRemove property value.
        """
        return self._fRestrictedMediaRemove

    @RestrictedMediaRemove.setter
    def RestrictedMediaRemove(self, value:bool) -> None:
        """ 
        Sets the RestrictedMediaRemove property value.
        """
        if value != None:
            self._fRestrictedMediaRemove = value


    @property
    def RestrictedMediaView(self) -> bool:
        """ 
        True if the user has access to view restricted media for the device; otherwise, False.

        Returns:
            The RestrictedMediaView property value.
        """
        return self._fRestrictedMediaView

    @RestrictedMediaView.setter
    def RestrictedMediaView(self, value:bool) -> None:
        """ 
        Sets the RestrictedMediaView property value.
        """
        if value != None:
            self._fRestrictedMediaView = value


    @property
    def RetentionCreate(self) -> bool:
        """ 
        True if the user has access to create retention settings for the device; otherwise, False.

        Returns:
            The RetentionCreate property value.
        """
        return self._fRetentionCreate

    @RetentionCreate.setter
    def RetentionCreate(self, value:bool) -> None:
        """ 
        Sets the RetentionCreate property value.
        """
        if value != None:
            self._fRetentionCreate = value


    @property
    def RetentionRemove(self) -> bool:
        """ 
        True if the user has access to remove retention settings for the device; otherwise, False.

        Returns:
            The RetentionRemove property value.
        """
        return self._fRetentionRemove

    @RetentionRemove.setter
    def RetentionRemove(self, value:bool) -> None:
        """ 
        Sets the RetentionRemove property value.
        """
        if value != None:
            self._fRetentionRemove = value


    @property
    def RetentionView(self) -> bool:
        """ 
        True if the user has access to view retention settings for the device; otherwise, False.

        Returns:
            The RetentionView property value.
        """
        return self._fRetentionView

    @RetentionView.setter
    def RetentionView(self, value:bool) -> None:
        """ 
        Sets the RetentionView property value.
        """
        if value != None:
            self._fRetentionView = value


    @property
    def RetrieveEdgeRecordings(self) -> bool:
        """ 
        True if the user has access to retrieve edge recordings for the device; otherwise, False.

        Returns:
            The RetrieveEdgeRecordings property value.
        """
        return self._fRetrieveEdgeRecordings

    @RetrieveEdgeRecordings.setter
    def RetrieveEdgeRecordings(self, value:bool) -> None:
        """ 
        Sets the RetrieveEdgeRecordings property value.
        """
        if value != None:
            self._fRetrieveEdgeRecordings = value


    @property
    def SmartSearch(self) -> bool:
        """ 
        True if the user has access to perform smart searches for the device; otherwise, False.

        Returns:
            The SmartSearch property value.
        """
        return self._fSmartSearch

    @SmartSearch.setter
    def SmartSearch(self, value:bool) -> None:
        """ 
        Sets the SmartSearch property value.
        """
        if value != None:
            self._fSmartSearch = value


    @property
    def StartRecording(self) -> bool:
        """ 
        True if the user has access to start recording for the device; otherwise, False.

        Returns:
            The StartRecording property value.
        """
        return self._fStartRecording

    @StartRecording.setter
    def StartRecording(self, value:bool) -> None:
        """ 
        Sets the StartRecording property value.
        """
        if value != None:
            self._fStartRecording = value


    @property
    def StopRecording(self) -> bool:
        """ 
        True if the user has access to stop recording for the device; otherwise, False.

        Returns:
            The StopRecording property value.
        """
        return self._fStopRecording

    @StopRecording.setter
    def StopRecording(self, value:bool) -> None:
        """ 
        Sets the StopRecording property value.
        """
        if value != None:
            self._fStopRecording = value


    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        
        Returns:
            A string in the form of "Browse = {0}"
        """
        return str.format("Browse = {0}", self.Browse or "")
