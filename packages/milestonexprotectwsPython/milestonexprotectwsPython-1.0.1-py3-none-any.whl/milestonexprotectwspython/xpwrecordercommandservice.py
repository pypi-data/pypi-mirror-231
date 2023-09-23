"""
Module: xpwrecordercommandservice.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
import base64
from datetime import datetime
import inspect
import json
from requests import Request, Session
from smartinspectpython.sisourceid import SISourceId 

# our package imports.
from .xpwappmessages import XPWAppMessages
from .xpwauthenticationtype import XPWAuthenticationType
from .xpwcollection import XPWCollection
from .xpwexception import XPWException
from .xpwjpegdata import XPWJpegData
from .xpwlogininfo import XPWLoginInfo
from .xpwmanualrecording import XPWManualRecording
from .xpwmanualrecordingresult import XPWManualRecordingResult
from .xpwrecordersequencetype import XPWRecorderSequenceType
from .xpwrecordersequenceentry import XPWRecorderSequenceEntry
from .xpwwebservicebase import XPWWebServiceBase

# our package constants.
from .xpwconst import (
    MSG_TRACE_METHOD_REQUEST,
    MSG_TRACE_METHOD_REQUEST_BODY,
    MSG_TRACE_METHOD_REQUEST_HEADERS,
    MSG_TRACE_PROCESSING_DICTIONARY,
    MSG_TRACE_RESULT_OBJECT
)

# get smartinspect logger reference.
from smartinspectpython.siauto import SISession, SILevel, SIAuto
_logsi:SISession = SIAuto.Main

# auto-generate the "__all__" variable with classes decorated with "@export".
from .xpwutils import export


@export
class XPWRecorderCommandService(XPWWebServiceBase):
    """
    The Recorder Command Service SOAP web service provides access to XProtect
    Recording Server functions in a given installation.
    """

    def __init__(self, loginInfo:XPWLoginInfo=None) -> None:
        """
        Initializes a new instance of the class.

        Args:
            loginInfo (XPWLoginInfo):
                Login Information class that contains login token information.  This class is returned 
                on a successful call to any of the LoginX methods from classes that inherit from
                XPWWebServiceBase.  This allows you to share the same Login Information (token, etc)
                between service classes.  
                Specify null / None to not share Login Information; if doing so, then your first call
                must be to one of the Login methods (e.g. LoginBasicUser, LoginWindowsUser, etc).  
                Default is null / None.                                

        Raises:
            XPWException:
                The method fails for any reason.  
        """
        serviceMethodName:str = "__init__"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            # initialize the base class.
            super().__init__(loginInfo)

            # initialize instance storage.
            self._fRecordingServerUrlPrefix:str = None

            # trace.
            _logsi.LogObject(SILevel.Verbose, "XPWRecorderCommandService Object Initialized", self)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    @property
    def RecordingServerUrlPrefix(self) -> str:
        """ 
        URL prefix of the XProtect Recording Server.

        Returns:
            The RecordingServerUrlPrefix property value.

        This url prefix is used to call various web-services that are hosted by the 
        XProtect Recording Server.  These services include the RecorderCommandService.asmx, etc.  

        It should only contain the server name (and port number if required) portion of
        the server url (e.g. "https://xprotectrecordingserver.example.com", or
        "https://xprotectrecordingserver.example.com:443").  

        It should NOT contain any of the server web-service method names or paths (e.g. 
        "https://xprotectrecordingserver.example.com/RecorderCommandService/RecorderCommandService.asmx").
        """
        return self._fRecordingServerUrlPrefix

    @RecordingServerUrlPrefix.setter
    def RecordingServerUrlPrefix(self, value:str) -> None:
        """ 
        Sets the RecordingServerUrlPrefix property value.
        """
        if (value != None):
            if (value.endswith("/")):
                value = value[0:len(value)-1]
            if (value != None):
                self._fRecordingServerUrlPrefix = value


    def _Parse_JPEGGetAt(self, oDict:dict, serviceMethodName:str, title:str) -> XPWJpegData:
        """
        Parses dictionary data for JPEGGetAt details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "JPEGGetLive", "JPEGGetAt", "JPEGGetAtOrAfter", "JPEGGetAtOrbefore", etc.
            title (str):
                Title to assign to the image.  

        Returns:
            An XPWManualRecording class that represents the dictionary details.
        """
        oItem:XPWJpegData = None
        methodKeyName:str = "XPWJpegData"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            # <JPEGGetLiveResult>
            #   <Time>2023-07-16T01:27:47.5040000Z</Time>
            #   <Data>/9j/4AAQSkZJRgABAg ... t1mY3P/Z</Data>
            # </JPEGGetLiveResult>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWJpegData = XPWJpegData()
                oItem.DataEncoded = self.GetDictKeyValueString(oDict, "Data")
                oItem.Time = self.GetDictKeyValueDateTime(oDict, "Time")
                oItem.Title = title

                # if jpeg data was returned, then decode the data.
                if (oItem.DataEncoded != None):

                    # encode the xml response ASCII data to a UTF-8 string.
                    encoded_bytes:bytes = oItem.DataEncoded.encode('utf-8')

                    # decode the UTF-8 string to binary bytes.
                    oItem.Data = base64.decodebytes(encoded_bytes)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

            # return object to caller.
            return oItem

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_ManualRecordingInfo(self, oDict:dict, serviceMethodName:str) -> XPWManualRecording:
        """
        Parses dictionary data for ManualRecordingInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "IsManualRecording", etc.

        Returns:
            An XPWManualRecording class that represents the dictionary details.
        """
        oItem:XPWManualRecording = None
        methodKeyName:str = "ManualRecordingInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            # <ManualRecordingInfo>
            #   <DeviceId>71cab37e-8718-4383-8e86-146b38168e42</DeviceId>
            #   <IsManualRecording>false</IsManualRecording>
            # </ManualRecordingInfo>
        
            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWManualRecording = XPWManualRecording()
                oItem.DeviceId = self.GetDictKeyValueString(oDict, "DeviceId")
                oItem.IsManualRecording = self.GetDictKeyValueBool(oDict, "IsManualRecording")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

            # return object to caller.
            return oItem

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_ManualRecordingResult(self, oDict:dict, serviceMethodName:str) -> XPWManualRecordingResult:
        """
        Parses dictionary data for ManualRecordingResult details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "StartManualRecording", "StopManualRecording", etc.

        Returns:
            An XPWManualRecordingResult class that represents the dictionary details.
        """
        oItem:XPWManualRecordingResult = None
        methodKeyName:str = "ManualRecordingResult"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            # <ManualRecordingResult>
            #   <DeviceId>f0f31f69-36a2-46a3-80b6-48e4bf617db8</DeviceId>
            #   <ResultCode>0</ResultCode>
            #   <Message>Success</Message>
            # </ManualRecordingResult>
        
            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWManualRecordingResult = XPWManualRecordingResult()
                oItem.DeviceId = self.GetDictKeyValueString(oDict, "DeviceId")
                oItem.Message = self.GetDictKeyValueString(oDict, "Message")
                oItem.ResultCode = self.GetDictKeyValueString(oDict, "ResultCode")
                
                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

            # return object to caller.
            return oItem

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_SequenceEntry(self, oDict:dict, serviceMethodName:str) -> XPWRecorderSequenceEntry:
        """
        Parses dictionary data for SequenceEntry details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "SequencesGet", etc.

        Returns:
            An XPWRecorderSequenceEntry class that represents the dictionary details.
        """
        oItem:XPWRecorderSequenceEntry = None
        methodKeyName:str = "SequenceEntry"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            # <SequenceEntry>
            #   <TimeBegin>2023-07-20T18:52:49.0530000Z</TimeBegin>
            #   <TimeTrigged>2023-07-20T18:52:49.0530000Z</TimeTrigged>
            #   <TimeEnd>2023-07-20T18:53:01.0290000Z</TimeEnd>
            # </SequenceEntry>
                
            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWRecorderSequenceEntry = XPWRecorderSequenceEntry()
                oItem.TimeBegin = self.GetDictKeyValueDateTime(oDict, "TimeBegin")
                oItem.TimeEnd = self.GetDictKeyValueDateTime(oDict, "TimeEnd")
                oItem.TimeTrigged = self.GetDictKeyValueDateTime(oDict, "TimeTrigged")

                # remove timezone awareness from all datetimes, as they will always be in UTC format.
                # this prevents "can't subtract offset-naive and offset-aware datetimes" exceptions 
                # later when comparing datetimes!
                if (oItem.TimeBegin != None):
                    oItem.TimeBegin = oItem.TimeBegin.replace(tzinfo=None)
                if (oItem.TimeEnd != None):
                    oItem.TimeEnd = oItem.TimeEnd.replace(tzinfo=None)
                if (oItem.TimeTrigged != None):
                    oItem.TimeTrigged = oItem.TimeTrigged.replace(tzinfo=None)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

            # return object to caller.
            return oItem

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_SequenceType(self, oDict:dict, serviceMethodName:str) -> XPWRecorderSequenceType:
        """
        Parses dictionary data for SequenceType details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "SequencesGetTypes", etc.

        Returns:
            An XPWRecorderSequenceType class that represents the dictionary details.
        """
        oItem:XPWRecorderSequenceType = None
        methodKeyName:str = "SequenceType"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            # <SequenceType>
            #   <Id>0601d294-b7e5-4d93-9614-9658561ad5e4</Id>
            #   <Name>RecordingWithTriggerSequence</Name>
            # </SequenceType>
                
            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWRecorderSequenceType = XPWRecorderSequenceType()
                oItem.Id = self.GetDictKeyValueString(oDict, "Id")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

            # return object to caller.
            return oItem

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def IsManualRecording(self, deviceIds:list[str]) -> XPWCollection:
        """
        Returns the manual recording status of one or more specified device id's.

        Args:
            deviceIds (list[str]):
                A list of device id strings to query for manual recording status.

        Returns:
            A collection of XPWManualRecording objects that contain manual recording
            statuses for the specified device id(s).

        Raises:
            XPWException:
                deviceIds argument is null, or an empty list, or is not of type list.  
                Login authentication type "X" not implemented for this method.  
                The method fails for any other reason.  

        If manual recording on a device is not active (false), it does not necessarily mean that the
        device has stopped recording. The device might still record because of other recording 
        rules, just not because of manual recording. If a given device is not recognized then the
        value sent back for the device is false.  

        An XPWManualRecording item is still created if a device id is not found; in this case, it's
        IsManualRecording property will be set to False.  XProtect web-services does not treat this
        as an error condition, so neither do we.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/IsManualRecording.py
        ```
        </details>
        """
        serviceMethodName:str = "IsManualRecording"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Manual Recording statuses for device id(s)")

                # validations.
                if (deviceIds == None) or (len(deviceIds) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceIds"), None, _logsi)
                if (not isinstance(deviceIds, list)):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR.format("deviceIds", "list[str]", type(deviceIds).__name__))

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate device ids nodes.
                    deviceIdsNode:str = ""
                    for device in deviceIds:
                        deviceIdsNode = deviceIdsNode + "<deviceId>{0}</deviceId>\n                                ".format(device)

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSRecorderCommand/IsManualRecording",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <IsManualRecording xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceIds>
                                {deviceIds}
                              </deviceIds>
                            </IsManualRecording>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, deviceIds=deviceIdsNode.rstrip())
                
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <IsManualRecordingResponse>
                #   <IsManualRecordingResult>
                #     <ManualRecordingInfo>
                #       ...
                #     </ManualRecordingInfo>
                #     <ManualRecordingInfo>
                #       ...
                #     </ManualRecordingInfo>
                #   </IsManualRecordingResult>
                # </IsManualRecordingResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "IsManualRecordingResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWManualRecording))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "ManualRecordingInfo")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_ManualRecordingInfo(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWManualRecording Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def JPEGGetAt(self, deviceId:str, time:datetime, title:str=None) -> XPWJpegData:
        """
        Get image from a given device as JPEG, at a given time or the nearest 
        one (either before or after).

        Args:
            deviceId (str):
                Device ID to obtain the data from.
            time (datetime):
                Requested image time as UTC
            title (str):
                Title to assign to the image.  
                If null, then the deviceId argument value will be used.

        Returns:
            An XPWJpegData class that contains JPEG image data.

        Raises:
            XPWException:
                deviceId argument is null or an empty string.  
                time argument is null, or year is less than 1800, or greater than datetime.max.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        If no image is available, the response is a JPEGData structure with time set to 
        minimum dateTime and data set to nothing.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/JPEGGetAt.py
        ```
        </details>
        """
        serviceMethodName:str = "JPEGGetAt"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving JPEG image from device ID \"{0}\" at time \"{1}\"".format(deviceId, time))

                # validations.
                if (deviceId == None) or (len(deviceId) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceId"))
                if (time == None) or (not isinstance(time,datetime)) or (time.year < 1800) or (time > datetime.max):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR_DATETIME.format("time"))
                if (title == None) or (len(title) ==0):
                    title = deviceId

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServiceRegistration/JPEGGetAt",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <JPEGGetAt xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceId>{deviceId}</deviceId>
                              <time>{time}</time>
                            </JPEGGetAt>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, deviceId=deviceId, time=time.isoformat())

                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <JPEGGetAtResponse>
                #   <JPEGGetAtResult>
                #     <Time>2023-07-16T01:27:47.5040000Z</Time>
                #     <Data>/9j/4AAQSkZJRgABAg ... t1mY3P/Z</Data>
                #   </JPEGGetAtResult>
                # </JPEGGetAtResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "JPEGGetAtResult", rsltNamespaces, True)

                # parse response details and return to caller.
                return self._Parse_JPEGGetAt(oDict, serviceMethodName, title)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def JPEGGetAtOrAfter(self, deviceId:str, time:datetime, title:str=None) -> XPWJpegData:
        """
        Get image from a given device as JPEG, at a given time or the nearest 
        one after.

        Args:
            deviceId (str):
                Device ID to obtain the data from.
            time (datetime):
                Requested image time as UTC
            title (str):
                Title to assign to the image.  
                If null, then the deviceId argument value will be used.

        Returns:
            An XPWJpegData class that contains JPEG image data.

        Raises:
            XPWException:
                deviceId argument is null or an empty string.  
                time argument is null, or year is less than 1800, or greater than datetime.max.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        If no image is available, the response is a JPEGData structure with time set to 
        minimum dateTime and data set to nothing.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/JPEGGetAtOrAfter.py
        ```
        </details>
        """
        serviceMethodName:str = "JPEGGetAtOrAfter"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving JPEG image from device ID \"{0}\" at time \"{1}\"".format(deviceId, time))

                # validations.
                if (deviceId == None) or (len(deviceId) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceId"))
                if (time == None) or (not isinstance(time,datetime)) or (time.year < 1800) or (time > datetime.max):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR_DATETIME.format("time"))
                if (title == None) or (len(title) ==0):
                    title = deviceId

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServiceRegistration/JPEGGetAtOrAfter",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <JPEGGetAtOrAfter xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceId>{deviceId}</deviceId>
                              <time>{time}</time>
                            </JPEGGetAtOrAfter>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   deviceId=deviceId, 
                                   time=time.isoformat())
                    
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <JPEGGetAtOrAfterResponse>
                #   <JPEGGetAtOrAfterResult>
                #     <Time>2023-07-16T01:27:47.5040000Z</Time>
                #     <Data>/9j/4AAQSkZJRgABAg ... t1mY3P/Z</Data>
                #   </JPEGGetAtOrAfterResult>
                # </JPEGGetAtOrAfterResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "JPEGGetAtOrAfterResult", rsltNamespaces, True)

                # parse response details and return to caller.
                return self._Parse_JPEGGetAt(oDict, serviceMethodName, title)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def JPEGGetAtOrBefore(self, deviceId:str, time:datetime, title:str=None) -> XPWJpegData:
        """
        Get image from a given device as JPEG, at a given time or the nearest 
        one before.

        Args:
            deviceId (str):
                Device ID to obtain the data from.
            time (datetime):
                Requested image time as UTC
            title (str):
                Title to assign to the image.  
                If null, then the deviceId argument value will be used.

        Returns:
            An XPWJpegData class that contains JPEG image data.

        Raises:
            XPWException:
                deviceId argument is null or an empty string.  
                time argument is null, or year is less than 1800, or greater than datetime.max.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        If no image is available, the response is a JPEGData structure with time set to 
        minimum dateTime and data set to nothing.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/JPEGGetAtOrBefore.py
        ```
        </details>
        """
        serviceMethodName:str = "JPEGGetAtOrBefore"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving JPEG image from device ID \"{0}\" at time \"{1}\"".format(deviceId, time))

                # validations.
                if (deviceId == None) or (len(deviceId) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceId"))
                if (time == None) or (not isinstance(time,datetime)) or (time.year < 1800) or (time > datetime.max):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR_DATETIME.format("time"))
                if (title == None) or (len(title) ==0):
                    title = deviceId

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServiceRegistration/JPEGGetAtOrBefore",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <JPEGGetAtOrBefore xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceId>{deviceId}</deviceId>
                              <time>{time}</time>
                            </JPEGGetAtOrBefore>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   deviceId=deviceId, 
                                   time=time.isoformat())
                
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <JPEGGetAtOrBeforeResponse>
                #   <JPEGGetAtOrBeforeResult>
                #     <Time>2023-07-16T01:27:47.5040000Z</Time>
                #     <Data>/9j/4AAQSkZJRgABAg ... t1mY3P/Z</Data>
                #   </JPEGGetAtOrBeforeResult>
                # </JPEGGetAtOrBeforeResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "JPEGGetAtOrBeforeResult", rsltNamespaces, True)

                # parse response details and return to caller.
                return self._Parse_JPEGGetAt(oDict, serviceMethodName, title)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def JPEGGetLive(self, deviceId:str, maxWidth:int=100, maxHeight:int=100, title:str=None) -> XPWJpegData:
        """
        Gets a live image from a given device as JPEG (i.e. encoded from last keyframe). 

        Args:
            deviceId (str):
                Device ID to obtain the data from.
            maxWidth (int):
                Maximum width of the returned image.  
                Note that this will never be larger than the max resolution that the device supports.  
                Default is 100 pixels.
            maxHeight (int):
                Maximum height of the returned image.  
                Note that this will never be larger than the max resolution that the device supports.  
                Default is 100 pixels.
            title (str):
                Title to assign to the image.  
                If null, then the deviceId argument value will be used.

        Returns:
            An XPWJpegData class that contains JPEG image data.

        Raises:
            XPWException:
                deviceId argument is null or an empty string.  
                maxWidth argument is null or less than 100.  
                maxHeight argument is null or less than 100.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        If no image is available, the response is a JPEGData structure with time set to 
        minimum dateTime and data set to nothing.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/JPEGGetLive.py
        ```
        </details>
        """
        serviceMethodName:str = "JPEGGetLive"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Live JPEG image from device ID \"{0}\"".format(deviceId))

                # validations.
                if (deviceId == None) or (len(deviceId) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceId"))
                if (maxWidth == None) or (maxWidth < 100):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("maxWidth"))
                if (maxHeight == None) or (maxHeight < 100):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("maxHeight"))
                if (title == None) or (len(title) ==0):
                    title = deviceId

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServiceRegistration/JPEGGetLive",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <JPEGGetLive xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceId>{deviceId}</deviceId>
                              <maxWidth>{maxWidth}</maxWidth>
                              <maxHeight>{maxHeight}</maxHeight>
                            </JPEGGetLive>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   deviceId=deviceId, 
                                   maxWidth=maxWidth, 
                                   maxHeight=maxHeight)
                
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <JPEGGetLiveResponse>
                #   <JPEGGetLiveResult>
                #     <Time>2023-07-16T01:27:47.5040000Z</Time>
                #     <Data>/9j/4AAQSkZJRgABAg ... t1mY3P/Z</Data>
                #   </JPEGGetLiveResult>
                # </JPEGGetLiveResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "JPEGGetLiveResult", rsltNamespaces, True)

                # parse response details and return to caller.
                return self._Parse_JPEGGetAt(oDict, serviceMethodName, title)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def SequencesGet(self, deviceId:str, sequenceType:str, minTime:datetime, maxTime:datetime, maxCount:int) -> XPWCollection:
        """
        Get chronological list of sequences for a given sequence type with specified minimum time, 
        maximum time and maximum count. 

        Args:
            deviceId (str):
                Device ID to obtain the data from.
            sequenceType (str):
                The requested sequence type id.  
                This should be a value returned from a call to the SequencesGetTypes method.
            minTime (datetime):
                Minimum sequence date and time to search for, in UTC format.
            maxTime (datetime):
                Maximum sequence date and time to search for, in UTC format.
            maxCount (int):
                Maximum number of sequences to return.

        Returns:
            A collection of XPWRecorderSequenceEntry objects that contains sequence types
            for the specified device id.

        Raises:
            XPWException:
                deviceId argument is null or an empty string.  
                sequenceType argument is null or an empty string.  
                minTime argument is null, or year is less than 1800, or greater than datetime.max.  
                maxTime argument is null, or year is less than 1800, or greater than datetime.max.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        Sequences are processed onwards from minTime and are sorted by TimeBegin.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/SequencesGet.py
        ```
        </details>
        """
        serviceMethodName:str = "SequencesGet"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Sequences from device ID \"{0}\" for sequence type ID \"{1}\"".format(deviceId, sequenceType))

                # validations.
                if (deviceId == None) or (len(deviceId) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceId"))
                if (sequenceType == None) or (len(sequenceType) == 0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("sequenceType"))
                if (minTime == None) or (not isinstance(minTime,datetime)) or (minTime.year < 1800) or (minTime > datetime.max):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR_DATETIME.format("minTime"))
                if (maxTime == None) or (not isinstance(maxTime,datetime)) or (maxTime.year < 1800) or (maxTime > datetime.max):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR_DATETIME.format("maxTime"))
                if (maxCount == None) or (not isinstance(maxCount,int)) or (maxCount < 1):
                    maxCount = 1

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServiceRegistration/SequencesGet",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <SequencesGet xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceId>{deviceId}</deviceId>
                              <sequenceType>{sequenceType}</sequenceType>
                              <minTime>{minTime}</minTime>
                              <maxTime>{maxTime}</maxTime>
                              <maxCount>{maxCount}</maxCount>
                            </SequencesGet>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   deviceId=deviceId, 
                                   sequenceType=sequenceType, 
                                   minTime=minTime.isoformat(), 
                                   maxTime=maxTime.isoformat(), 
                                   maxCount=maxCount)

                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <SequencesGetResponse>
                #   <SequencesGetResult>
                #     <SequenceEntry>
                #       ...
                #     </SequenceEntry>
                #     <SequenceEntry>
                #       ...
                #     </SequenceEntry>
                #   </SequencesGetResult>
                # </SequencesGetResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "SequencesGetResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWRecorderSequenceEntry))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "SequenceEntry")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_SequenceEntry(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWRecorderSequenceEntry Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def SequencesGetAround(self, deviceId:str, sequenceType:str, centerTime:datetime, maxCountBefore:int, maxCountAfter:int) -> XPWCollection:
        """
        Get chronological list of sequences for a given sequence type with specified center time, 
        maximum count before center time and maximum count after center time. 

        Args:
            deviceId (str):
                Device ID to obtain the data from.
            sequenceType (str):
                The requested sequence type id.  
                This should be a value returned from a call to the SequencesGetAroundTypes method.
            centerTime (datetime):
                Minimum sequence date and time to search for, in UTC format.
            maxCountBefore (int):
                Maximum number of sequences before the centerTime to return.
            maxCountAfter (int):
                Maximum number of sequences after the centerTime to return.

        Returns:
            A collection of XPWRecorderSequenceEntry objects that contains sequence types
            for the specified device id.

        Raises:
            XPWException:
                deviceId argument is null or an empty string.  
                sequenceType argument is null or an empty string.  
                centerTime argument is null, or year is less than 1800, or greater than datetime.max.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        A sequence with TimeBegin equal to centertime will increase "after" count.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/SequencesGetAround.py
        ```
        </details>
        """
        serviceMethodName:str = "SequencesGetAround"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Sequences around center time from device ID \"{0}\" for sequence type ID \"{1}\"".format(deviceId, sequenceType))

                # validations.
                if (deviceId == None) or (len(deviceId) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceId"))
                if (sequenceType == None) or (len(sequenceType) == 0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("sequenceType"))
                if (centerTime == None) or (not isinstance(centerTime,datetime)) or (centerTime.year < 1800) or (centerTime > datetime.max):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR_DATETIME.format("centerTime"))
                if (maxCountBefore == None) or (not isinstance(maxCountBefore,int)) or (maxCountBefore < 1):
                    maxCountBefore = 1
                if (maxCountAfter == None) or (not isinstance(maxCountAfter,int)) or (maxCountAfter < 1):
                    maxCountAfter = 1

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServiceRegistration/SequencesGetAround",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <SequencesGetAround xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceId>{deviceId}</deviceId>
                              <sequenceType>{sequenceType}</sequenceType>
                              <centerTime>{centerTime}</centerTime>
                              <maxCountBefore>{maxCountBefore}</maxCountBefore>
                              <maxCountAfter>{maxCountAfter}</maxCountAfter>
                            </SequencesGetAround>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   deviceId=deviceId, 
                                   sequenceType=sequenceType, 
                                   centerTime=centerTime.isoformat(), 
                                   maxCountBefore=maxCountBefore, 
                                   maxCountAfter=maxCountAfter)

                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <SequencesGetAroundResponse>
                #   <SequencesGetAroundResult>
                #     <SequenceEntry>
                #       ...
                #     </SequenceEntry>
                #     <SequenceEntry>
                #       ...
                #     </SequenceEntry>
                #   </SequencesGetAroundResult>
                # </SequencesGetAroundResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "SequencesGetAroundResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWRecorderSequenceEntry))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "SequenceEntry")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_SequenceEntry(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWRecorderSequenceEntry Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def SequencesGetAroundWithSpan(self, deviceId:str, sequenceType:str, centerTime:datetime, maxTimeBefore:int, maxCountBefore:int, maxTimeAfter:int, maxCountAfter:int) -> XPWCollection:
        """
        Get chronological list of sequences for a given sequence type with specified center time, 
        maximum count before center time and maximum count after center time. Furthermore, search 
        is limited before and after centertime by maximum timespans.

        Args:
            deviceId (str):
                Device ID to obtain the data from.
            sequenceType (str):
                The requested sequence type id.  
                This should be a value returned from a call to the SequencesGetAroundWithSpanTypes method.
            centerTime (datetime):
                Minimum sequence date and time to search for, in UTC format.
            maxTimeBefore (int):
                Maximum amount of time (in milliseconds) before the centerTime to return sequences for.
            maxCountBefore (int):
                Maximum number of sequences before the centerTime to return.
            maxTimeAfter (int):
                Maximum amount of time (in milliseconds) after the centerTime to return sequences for.
            maxCountAfter (int):
                Maximum number of sequences after the centerTime to return.

        Returns:
            A collection of XPWRecorderSequenceEntry objects that contains sequence types
            for the specified device id.

        Raises:
            XPWException:
                deviceId argument is null or an empty string.  
                sequenceType argument is null or an empty string.  
                centerTime argument is null, or year is less than 1800, or greater than datetime.max.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/SequencesGetAroundWithSpan.py
        ```
        </details>
        """
        serviceMethodName:str = "SequencesGetAroundWithSpan"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Sequences around center time (with span) from device ID \"{0}\" for sequence type ID \"{1}\"".format(deviceId, sequenceType))

                # validations.
                if (deviceId == None) or (len(deviceId) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceId"))
                if (sequenceType == None) or (len(sequenceType) == 0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("sequenceType"))
                if (centerTime == None) or (not isinstance(centerTime,datetime)) or (centerTime.year < 1800) or (centerTime > datetime.max):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR_DATETIME.format("centerTime"))
                if (maxTimeBefore == None) or (not isinstance(maxTimeBefore,int)) or (maxTimeBefore < 1):
                    maxTimeBefore = 1
                if (maxCountBefore == None) or (not isinstance(maxCountBefore,int)) or (maxCountBefore < 1):
                    maxCountBefore = 1
                if (maxTimeAfter == None) or (not isinstance(maxTimeAfter,int)) or (maxTimeAfter < 1):
                    maxTimeAfter = 1
                if (maxCountAfter == None) or (not isinstance(maxCountAfter,int)) or (maxCountAfter < 1):
                    maxCountAfter = 1

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServiceRegistration/SequencesGetAroundWithSpan",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <SequencesGetAroundWithSpan xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceId>{deviceId}</deviceId>
                              <sequenceType>{sequenceType}</sequenceType>
                              <centerTime>{centerTime}</centerTime>
                              <maxTimeBefore>
                                <MicroSeconds>{maxTimeBefore}</MicroSeconds>
                              </maxTimeBefore>
                              <maxCountBefore>{maxCountBefore}</maxCountBefore>
                              <maxTimeAfter>
                                <MicroSeconds>{maxTimeAfter}</MicroSeconds>
                              </maxTimeAfter>
                              <maxCountAfter>{maxCountAfter}</maxCountAfter>
                            </SequencesGetAroundWithSpan>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   deviceId=deviceId, 
                                   sequenceType=sequenceType, 
                                   centerTime=centerTime.isoformat(), 
                                   maxTimeBefore=maxTimeBefore, 
                                   maxCountBefore=maxCountBefore, 
                                   maxTimeAfter=maxTimeAfter, 
                                   maxCountAfter=maxCountAfter)
                
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <SequencesGetAroundWithSpanResponse xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                #   <SequencesGetAroundWithSpanResult>
                #     <SequenceEntry>
                #       ...
                #     </SequenceEntry>
                #     <SequenceEntry>
                #       ...
                #     </SequenceEntry>
                #   </SequencesGetAroundWithSpanResult>
                # </SequencesGetAroundWithSpanResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "SequencesGetAroundWithSpanResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWRecorderSequenceEntry))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "SequenceEntry")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_SequenceEntry(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWRecorderSequenceEntry Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def SequencesGetTypes(self, deviceId:str) -> XPWCollection:
        """
        Gets a collection of available sequence types for a given device.

        Args:
            deviceId (str):
                The device id string to query for sequence types.

        Returns:
            A collection of XPWRecorderSequenceType objects that contains sequence types
            for the specified device id.

        Raises:
            XPWException:
                deviceId argument is null or an empty list.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        Common sequence types are:
        RecordingSequence = {F9C62604-D0C5-4050-AE25-72DE51639B14}  
        MotionSequence = {53CB5E33-2183-44bd-9491-8364D2457480}  
        RecordingWithTriggerSequence = {0601D294-B7E5-4d93-9614-9658561AD5E4}  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/SequencesGetTypes.py
        ```
        </details>
        """
        serviceMethodName:str = "SequencesGetTypes"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving recorder Sequence Types for device id \"{0}\"".format(str(deviceId)))

                # validations.
                if (deviceId == None) or (len(deviceId) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceId"))

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSRecorderCommand/SequencesGetTypes",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <SequencesGetTypes xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceId>{deviceId}</deviceId>
                            </SequencesGetTypes>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, deviceId=deviceId)
                
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <SequencesGetTypesResponse>
                #   <SequencesGetTypesResult>
                #     <SequenceType>
                #       ...
                #     </SequenceType>
                #     <SequenceType>
                #       ...
                #     </SequenceType>
                #   </SequencesGetTypesResult>
                # </SequencesGetTypesResponse>
    
                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "SequencesGetTypesResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWRecorderSequenceType))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "SequenceType")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_SequenceType(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWRecorderSequenceType Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def StartManualRecording(self, deviceIds:list[str]) -> XPWCollection:
        """
        Requests a start of manual recording on a device(s). 

        Args:
            deviceIds (list[str]):
                A list of device id strings to start manually recording on.

        Returns:
            A collection of XPWManualRecordingResult objects that contain manual recording
            statuses for the specified device id(s).

        Raises:
            XPWException:
                deviceIds argument is null, or an empty list, or is not of type list.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        The start manual recording request will start recording on the device if recording has not already 
        been started because of other rules.  A service channel event is sent when the evaluation of start 
        manual recording has been made. If manual recording is already active, the command is simply ignored, 
        but the request is still successful.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/StartManualRecording.py
        ```
        </details>
        """
        serviceMethodName:str = "StartManualRecording"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Starting Manual Recording for device id(s) \"{0}\"".format(str(deviceIds)))

                # validations.
                if (deviceIds == None) or (len(deviceIds) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceIds"), None, _logsi)
                if (not isinstance(deviceIds, list)):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR.format("deviceIds", "list[str]", type(deviceIds).__name__))

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate device ids nodes.
                    deviceIdsNode:str = ""
                    for device in deviceIds:
                        deviceIdsNode = deviceIdsNode + "<deviceId>{0}</deviceId>\n                                ".format(device)

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSRecorderCommand/StartManualRecording",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <StartManualRecording xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceIds>
                                {deviceIds}
                              </deviceIds>
                            </StartManualRecording>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, deviceIds=deviceIdsNode.rstrip())
                
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <StartManualRecordingResponse>
                #   <StartManualRecordingResult>
                #     <ManualRecordingResult>
                #       ...
                #     </ManualRecordingResult>
                #     <ManualRecordingResult>
                #       ...
                #     </ManualRecordingResult>
                #   </StartManualRecordingResult>
                # </StartManualRecordingResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "StartManualRecordingResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWManualRecordingResult))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "ManualRecordingResult")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_ManualRecordingResult(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWManualRecordingResult Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def StopManualRecording(self, deviceIds:list[str]) -> XPWCollection:
        """
        Requests a stop of manual recording on a device(s). 

        Args:
            deviceIds (list[str]):
                A list of device id strings to stop manually recording on.

        Returns:
            A collection of XPWManualRecordingResult objects that contain manual recording
            statuses for the specified device id(s).

        Raises:
            XPWException:
                deviceIds argument is null, or an empty list, or is not of type list.  
                Login.Authentication type "X" not implemented for this method.  
                The method failed for any other reason.  

        Note that stopping manual recording does not necessary mean that the device stops recording. 
        The device might still record because of other recording rules, just not because of manual recording. 
        A service channel event is sent when the evaluation of stop manual recording has been made. If 
        manual recording is already stopped, the command is simply ignored but the request is still successful.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWRecorderCommandService/StopManualRecording.py
        ```
        </details>
        """
        serviceMethodName:str = "StopManualRecording"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Stopping Manual Recording for device id(s) \"{0}\"".format(str(deviceIds)))

                # validations.
                if (deviceIds == None) or (len(deviceIds) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceIds"), None, _logsi)
                if (not isinstance(deviceIds, list)):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR.format("deviceIds", "list[str]", type(deviceIds).__name__))

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate device ids nodes.
                    deviceIdsNode:str = ""
                    for device in deviceIds:
                        deviceIdsNode = deviceIdsNode + "<deviceId>{0}</deviceId>\n                                ".format(device)

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/RecorderCommandService/RecorderCommandService.asmx".format(self.RecordingServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSRecorderCommand/StopManualRecording",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <StopManualRecording xmlns="http://videoos.net/2/XProtectCSRecorderCommand">
                              <token>{token}</token>
                              <deviceIds>
                                {deviceIds}
                              </deviceIds>
                            </StopManualRecording>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   deviceIds=deviceIdsNode.rstrip())
                
                else:
                    
                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody))

                # prepare the request.
                reqSess = Session()
                reqprep = reqSess.prepare_request(req)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST.format(serviceMethodName), reqprep)
                    _logsi.LogSource(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_BODY.format(serviceMethodName), reqprep.body, SISourceId.Xml)
                    _logsi.LogDictionary(SILevel.Verbose, MSG_TRACE_METHOD_REQUEST_HEADERS.format(serviceMethodName), reqprep.headers)

                # send the request.
                resp = reqSess.send(reqprep, verify=self.IsSslVerifyEnabled)

                # SOAP response example:
                # <StopManualRecordingResponse>
                #   <StopManualRecordingResult>
                #     <ManualRecordingResult>
                #       ...
                #     </ManualRecordingResult>
                #     <ManualRecordingResult>
                #       ...
                #     </ManualRecordingResult>
                #   </StopManualRecordingResult>
                # </StopManualRecordingResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "StopManualRecordingResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWManualRecordingResult))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "ManualRecordingResult")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_ManualRecordingResult(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWManualRecordingResult Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)
