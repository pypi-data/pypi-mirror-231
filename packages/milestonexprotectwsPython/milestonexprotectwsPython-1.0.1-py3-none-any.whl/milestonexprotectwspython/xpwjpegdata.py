"""
Module: xpwjpegdata.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
from datetime import datetime
from smartinspectpython.siauto import SISession, SILevel, SIAuto

# our package imports.
from .xpwappmessages import XPWAppMessages
from .xpwexception import XPWException

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWJpegData:
    """
    JPEG data returned by a RecorderCommandService JPEGGetLive call.
    
    Threadsafety:
        This class is fully thread-safe.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # initialize instance.
        self._fData:bytes = None
        self._fDataEncoded:str = None
        self._fSaveToFilePath:str = None
        self._fTime:datetime = None
        self._fTitle:str = None


    @property
    def Data(self) -> bytes:
        """ 
        JPEG data, represented as raw bytes.

        Returns:
            The Data property value.
        """
        return self._fData

    @Data.setter
    def Data(self, value:bytes) -> None:
        """ 
        Sets the Data property value.
        """
        if value != None:
            self._fData = value


    @property
    def DataEncoded(self) -> str:
        """ 
        JPEG data, represented as a base64 ASCII encoded string.

        Returns:
            The Data property value.
        """
        return self._fDataEncoded

    @DataEncoded.setter
    def DataEncoded(self, value:str) -> None:
        """ 
        Sets the DataEncoded property value.
        """
        if value != None:
            self._fDataEncoded = value


    @property
    def HasData(self) -> bool:
        """ 
        True if the Data property contains valid data; otherwise, false.

        Returns:
            The HasData property value.
        """
        if (self._fDataEncoded != None) and (len(self._fDataEncoded) > -1):
            return True
        return False


    @property
    def SaveToFilePath(self) -> str:
        """ 
        File path the image data was written to if the SaveToFile method has been called successfully;
        otherwise, null / None.

        Returns:
            The SaveToFilePath property value.
        """
        return self._fSaveToFilePath

    @SaveToFilePath.setter
    def SaveToFilePath(self, value:str) -> None:
        """ 
        Sets the SaveToFilePath property value.
        """
        if value != None:
            self._fSaveToFilePath = value


    @property
    def Time(self) -> datetime:
        """ 
        Date and Time (UTC) of the image.

        Returns:
            The Time property value.
        """
        return self._fTime

    @Time.setter
    def Time(self, value:datetime) -> None:
        """ 
        Sets the Time property value.
        """
        if value != None:
            self._fTime = value


    @property
    def Title(self) -> str:
        """ 
        Title of the image, as specified by the user.
        
        Returns:
            The Title property value.

        This property is assigned by the user, and is not derived from XProtect web-services results.
        """
        return self._fTitle

    @Title.setter
    def Title(self, value:str) -> None:
        """ 
        Sets the Title property value.
        """
        if value != None:
            self._fTitle = value


    def __str__(self) -> str:
        """
        A string in the form of "{Title} (image time={time})"
        
        Returns:
            A string representation of the object.
        """
        return str.format("{0} (image time={1})", self.Title, self.Time.strftime("%Y-%m-%d %H:%M:%S"))


    def SaveToFile(self, filePath:str, timeFormat:str="%Y%m%d_%H%M%S_%Z") -> None:
        """
        Saves the JPEG image data (Data property) to the specified file path.

        Args:
            filePath:
                File path to save the JPEG data to.
            timeFormat:
                Date format string to use if the "{time}" placeholder was specified in the filePath argument.  
                Default is "%Y%m%d_%H%M%S_%Z" (e.g. 20230716_193747_UTC).

        Raises:
            XPWException:
                filepath argument is null or an empty string.  
                timeFormat argument is null or an empty string.  
                The method fails for any other reason.  

        If the Data property is empty then nothing is saved and no exception is raised.

        Use the "{time}" placeholder (case-sensitive) to insert the formatted Time property 
        value in the filePath.  The formatting is controlled by the timeFormat argument.
        Example filePath: ".\tests\iPadCam01_{time}.jpg".  

        Use the "{title}" placeholder (case-sensitive) to insert the Title property 
        value in the filePath.  
        Example filePath: ".\tests\{title}_{time}.jpg".  

        The resolved filePath argument will be stored in the SaveToFilePath property if
        the file is successfully saved.
        """
        # get smartinspect logger reference.
        _logsi:SISession = SIAuto.Main

        serviceMethodName:str = "SaveToFile"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)
            _logsi.LogVerbose("Saving JPEG data to file: \"{0}\"".format(filePath))

            # validations.
            if (self.Data == None) or (len(self.Data) == 0):
                _logsi.LogVerbose("JPEG Data property is empty - nothing to save")
                return
            if (filePath == None) or (len(filePath) == 0):
                raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("filepath"), None, _logsi)
            if (timeFormat == None) or (len(timeFormat) == 0):
                raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("timeFormat"), None, _logsi)

            TIME_KEY:str = "{time}"
            TITLE_KEY:str = "{title}"

            # was the {time} placeholder present?
            if (filePath.find(TIME_KEY) > -1):

                # add formatted time to file path if specified.
                timeFormat = timeFormat.replace(":","-")
                fmtDate = self.Time.strftime(timeFormat)
                filePath = filePath.replace(TIME_KEY, fmtDate)

            # was the {title} placeholder present?  if so, then override with Title property.
            if (filePath.find(TITLE_KEY) > -1):
                filePath = filePath.replace(TITLE_KEY, self._fTitle + "")

            # save to file.
            with open(filePath, 'wb') as outfile:
                outfile.write(self._fData)

            # store path we saved the image to.
            self._fSaveToFilePath = filePath
            
            # trace.
            _logsi.LogMessage("JPEG data saved to file: \"{0}\"".format(filePath))
            _logsi.LogJpegFile(SILevel.Verbose, "JPEG file image: \"{0}\"".format(filePath), filePath)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)
