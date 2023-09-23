"""
Module: xpwservercommandservice.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  

</details>
"""


# external package imports.
import inspect
import json
from requests import Request, Session
from smartinspectpython.sisourceid import SISourceId 

# our package imports.
from .xpwalerttype import XPWAlertType
from .xpwalerttypegroup import XPWAlertTypeGroup
from .xpwapplicationsecurity import XPWApplicationSecurity
from .xpwappmessages import XPWAppMessages
from .xpwaudiomessage import XPWAudioMessage
from .xpwauthenticationtype import XPWAuthenticationType
from .xpwbookmarksettings import XPWBookmarkSettings
from .xpwcamera import XPWCamera
from .xpwcameragroup import XPWCameraGroup
from .xpwcamerasecurity import XPWCameraSecurity
from .xpwcapability import XPWCapability
from .xpwcollection import XPWCollection
from .xpwconfiguration import XPWConfiguration
from .xpwdevicedisabled import XPWDeviceDisabled
from .xpwdevice import XPWDevice
from .xpwdevicemapping import XPWDeviceMapping
from .xpweventtype import XPWEventType
from .xpweventtypegroup import XPWEventTypeGroup
from .xpwexception import XPWException
from .xpwgroup import XPWGroup
from .xpwhardware import XPWHardware
from .xpwhemisphere import XPWHemisphere
from .xpwimmervision import XPWImmerVision
from .xpwinput import XPWInput
from .xpwinputgroup import XPWInputGroup
from .xpwinputsecurity import XPWInputSecurity
from .xpwipix import XPWIpix
from .xpwlicense import XPWLicense
from .xpwlogininfo import XPWLoginInfo
from .xpwmatrixmonitor import XPWMatrixMonitor
from .xpwmetadatadevice import XPWMetadataDevice
from .xpwmetadatadevicesecurity import XPWMetadataDeviceSecurity
from .xpwmetadatatype import XPWMetadataType
from .xpwmicrophone import XPWMicrophone
from .xpwmicrophonegroup import XPWMicrophoneGroup
from .xpwmicrophonesecurity import XPWMicrophoneSecurity
from .xpwoutputgroup import XPWOutputGroup
from .xpwoutput import XPWOutput
from .xpwoutputsecurity import XPWOutputSecurity
from .xpwpanoramiclens import XPWPanoramicLens
from .xpwposition import XPWPosition
from .xpwproduct import XPWProduct
from .xpwptz import XPWPtz
from .xpwptzsecurity import XPWPtzSecurity
from .xpwpreset import XPWPreset
from .xpwrecorder import XPWRecorder
from .xpwretentionoption import XPWRetentionOption
from .xpwserveroption import XPWServerOption
from .xpwsmartclientsecurity import XPWSmartClientSecurity
from .xpwspeakergroup import XPWSpeakerGroup
from .xpwspeaker import XPWSpeaker
from .xpwspeakersecurity import XPWSpeakerSecurity
from .xpwstream import XPWStream
from .xpwsystemeventtype import XPWSystemEventType
from .xpwtrack import XPWTrack
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
class XPWServerCommandService(XPWWebServiceBase):
    """
    The Server Command Service SOAP web service provides access to XProtect
    Management Server functions in a given installation.
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

            # trace.
            _logsi.LogObject(SILevel.Verbose, "XPWServerCommandService Object Initialized", self)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def GetConfiguration(self) -> XPWConfiguration:
        """
        Returns configuration information for an XProtect Management Server.

        Returns:
            An XPWConfiguration class that contains server configuration details.

        Raises:
            XPWWebServiceException:
                The XProtect Web-Services Server returned a failed response.
            XPWException:
                The method fails for any other reason.  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWServerCommandService/GetConfiguration.py
        ```
        </details>
        """
        serviceMethodName:str = "GetConfiguration"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Server Configuration information")

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):
                    
                    # formulate xprotect svc service request parameters (url, headers, body).
                    requrl:str = "{0}/ManagementServer/ServerCommandService.svc".format(self.ManagementServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/GetConfiguration",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetConfiguration xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                            </GetConfiguration>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token)

                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/ServerAPI/ServerCommandService.asmx".format(self.ServerApiUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/GetConfiguration",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetConfiguration xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                            </GetConfiguration>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token)

                else:

                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(self.LoginInfo.UserName, self.LoginInfo.Password))

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
                # <GetConfigurationResponse xmlns="http://videoos.net/2/XProtectCSServerCommand">
                #   <GetConfigurationResult>
                #     <ServerId>fc9e48ce-a39b-4327-8b92-32b012688944</ServerId>
                #     <ServerName>WIN10VM</ServerName>
                #     <ServerDescription />
                #     <FailoverCheckInterval>0</FailoverCheckInterval>
                #      ...
                #   </GetConfigurationResult>
                # </GetConfigurationResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "GetConfigurationResult", rsltNamespaces, True)

                # parse response details and return to caller.
                return self._Parse_ConfigurationInfo(oDict, serviceMethodName)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def GetConfigurationHardware(self, deviceIds:list[str]) -> XPWCollection:
        """
        Returns configuration hardware information for an XProtect Management Server.

        Args:
            deviceIds (list[str]):
                A list of device id strings to query for configuration information.

        Returns:
            A collection of XPWHardware objects that contains hardware configuration 
            details for the specified device id(s).  The collection will be empty if
            the specified device id(s) could not be found.

        Raises:
            XPWWebServiceException:
                The XProtect Web-Services Server returned a failed response.
            XPWException:
                deviceIds argument was not supplied.  
                The method fails for any other reason.  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWServerCommandService/GetConfigurationHardware.py
        ```
        </details>
        """
        serviceMethodName:str = "GetConfigurationHardware"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Server Hardware Configuration information")

                # validations.
                if (deviceIds == None) or (len(deviceIds) ==0):
                    raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("deviceIds"), None, _logsi)
                if (not isinstance(deviceIds, list)):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR.format("deviceIds", "list[str]", type(deviceIds).__name__))

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):

                    # formulate device ids nodes.
                    deviceIdsNode:str = ""
                    for device in deviceIds:
                        deviceIdsNode = deviceIdsNode + "<a:guid>{0}</a:guid>\n                            ".format(device)

                    # formulate xprotect svc service request parameters (url, headers, body).
                    requrl:str = "{0}/ManagementServer/ServerCommandService.svc".format(self.ManagementServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/GetConfigurationHardware",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetConfigurationHardware xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                              <hardwareIds xmlns:a="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
                                {guids}
                              </hardwareIds>
                            </GetConfigurationHardware>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   guids=deviceIdsNode.rstrip())
                    
                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):

                    # formulate device ids nodes.
                    deviceIdsNode:str = ""
                    for device in deviceIds:
                        deviceIdsNode = deviceIdsNode + "<guid>{0}</guid>\n                            ".format(device)

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/ServerAPI/ServerCommandService.asmx".format(self.ServerApiUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/GetConfigurationHardware",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetConfigurationHardware xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                              <hardwareIds>
                                {guids}
                              </hardwareIds>
                            </GetConfigurationHardware>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   guids=deviceIdsNode.rstrip())

                else:

                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(self.LoginInfo.UserName, self.LoginInfo.Password))

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
                # <GetConfigurationHardwareResponse>
                #   <GetConfigurationHardwareResult>
                #     <HardwareInfo>
                #       ...
                #     </HardwareInfo>
                #   </GetConfigurationHardwareResult>
                # </GetConfigurationHardwareResponse>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "GetConfigurationHardwareResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWHardware))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "HardwareInfo")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_HardwareInfo(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWHardware Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def GetConfigurationRecorders(self, recorderIds:list[str]) -> XPWCollection:
        """
        Returns configuration information for one or more XProtect Recording Servers.

        Args:
            recorderIds (list[str]):
                A list of recorder id strings to query for configuration information.

        Returns:
            A collection of XPWRecorder objects that contain recorder configuration 
            details for the specified recorder id(s).  The collection will be empty if
            the specified recorder id(s) could not be found.

        Raises:
            XPWWebServiceException:
                The XProtect Web-Services Server returned a failed response.
            XPWException:
                recorderIds argument was not supplied.  
                The method fails for any other reason.  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWServerCommandService/GetConfigurationRecorders.py
        ```
        </details>
        """
        serviceMethodName:str = "GetConfigurationRecorders"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Recording Server Configuration information")

                # validations.
                if (recorderIds == None) or (len(recorderIds) ==0):
                    raise Exception(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("recorderIds"), None, _logsi)
                if (not isinstance(recorderIds, list)):
                    raise Exception(XPWAppMessages.ARGUMENT_TYPE_ERROR.format("recorderIds", "list[str]", type(recorderIds).__name__))

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):
                    
                    # formulate device id nodes.
                    recorderIdsNode:str = ""
                    for device in recorderIds:
                        recorderIdsNode = recorderIdsNode + "<guid>{0}</guid>\n                            ".format(device)

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/ServerAPI/ServerCommandService.asmx".format(self.ServerApiUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/GetConfigurationRecorders",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetConfigurationRecorders xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                              <recorderIds>
                                {guids}
                              </recorderIds>
                            </GetConfigurationRecorders>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   guids=recorderIdsNode.rstrip())
                
                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):
                    
                    # formulate device ids nodes.
                    recorderIdsNode:str = ""
                    for device in recorderIds:
                        recorderIdsNode = recorderIdsNode + "<a:guid>{0}</a:guid>\n                            ".format(device)

                    # formulate xprotect svc service request parameters (url, headers, body).
                    requrl:str = "{0}/ManagementServer/ServerCommandService.svc".format(self.ManagementServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/GetConfigurationRecorders",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetConfigurationRecorders xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                              <recorderIds xmlns:a="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
                                {guids}
                              </recorderIds>
                            </GetConfigurationRecorders>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   guids=recorderIdsNode.rstrip())
                
                else:

                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(self.LoginInfo.UserName, self.LoginInfo.Password))

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
                # <GetConfigurationRecordersResult>
                #   <RecorderInfo>
                #      ...
                #   </RecorderInfo>
                #   <RecorderInfo>
                #      ...
                #   </RecorderInfo>
                # </GetConfigurationRecordersResult>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "GetConfigurationRecordersResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWRecorder))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "RecorderInfo")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_RecorderInfo(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWRecorder Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def GetDevicesDisabled(self) -> XPWCollection:
        """
        Returns disabled device information for an XProtect Management Server.

        Returns:
            A collection of XPWDeviceDisabled objects that contain disabled device 
            configuration details.  The collection will be empty if there are
            currently no disabled devices found.

        Raises:
            XPWWebServiceException:
                The XProtect Web-Services Server returned a failed response.
            XPWException:
                The method fails for any other reason.  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWServerCommandService/GetDevicesDisabled.py
        ```
        </details>
        """
        serviceMethodName:str = "GetDevicesDisabled"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Retrieving Server Disabled Devices information")

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):

                    # formulate xprotect svc service request parameters (url, headers, body).
                    requrl:str = "{0}/ManagementServer/ServerCommandService.svc".format(self.ManagementServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/GetDevicesDisabled",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetDevicesDisabled xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                            </GetDevicesDisabled>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token)

                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/ServerAPI/ServerCommandService.asmx".format(self.ServerApiUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/GetDevicesDisabled",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetDevicesDisabled xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                            </GetDevicesDisabled>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token)
                
                else:

                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(self.LoginInfo.UserName, self.LoginInfo.Password))

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
                # <GetDevicesDisabledResult>
                #   <DeviceDisabledInfo>
                #     <DeviceId>0c60e7bf-9d57-4047-b623-e76d375a1fe6</DeviceId>
                #     <DeviceName>iPadCam01 Camera</DeviceName>
                #     <DeviceType>Camera</DeviceType>
                #     <HardwareId>08cf6a24-c7ab-4b50-80e0-5a56cf624c5f</HardwareId>
                #     <RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
                #   </DeviceDisabledInfo>
                #   <DeviceDisabledInfo>
                #     <DeviceId>8a381bcc-7752-45dd-91f2-3aa8345d37db</DeviceId>
                #     <DeviceName>iPadCam01 Microphone</DeviceName>
                #     <DeviceType>Microphone</DeviceType>
                #     <HardwareId>08cf6a24-c7ab-4b50-80e0-5a56cf624c5f</HardwareId>
                #     <RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
                #   </DeviceDisabledInfo>
                # </GetDevicesDisabledResult>

                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "GetDevicesDisabledResult", rsltNamespaces, False)

                # create results collection.
                oResult:XPWCollection = XPWCollection((XPWDeviceDisabled))

                # were any results returned?
                if (oDict != None):

                    # process xml result collection item node(s).
                    baseNodes:dict = self.GetDictItems(oDict, "DeviceDisabledInfo")
                    for itemNode in baseNodes:
                        oResult.append(self._Parse_DeviceDisabledInfo(itemNode, serviceMethodName))
  
                    # trace.
                    _logsi.LogText(SILevel.Verbose, "XPWDeviceDisabled Items Summary", str(oResult))

                # return object to caller.
                return oResult

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def GetProductInfo(self) -> XPWProduct:
        """
        Returns product information for an XProtect Management Server.

        Returns:
            An XPWProduct class that contains management server product details.

        Raises:
            XPWWebServiceException:
                The XProtect Web-Services Server returned a failed response.
            XPWException:
                The method fails for any other reason.  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWServerCommandService/GetProductInfo.py
        ```
        </details>
        """
        serviceMethodName:str = "GetProductInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Getting Product information")

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):

                    # formulate xprotect svc service request parameters (url, headers, body).
                    requrl:str = "{0}/ManagementServer/ServerCommandService.svc".format(self.ManagementServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/GetProductInfo",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetProductInfo xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                            </GetProductInfo>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token)

                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/ServerAPI/ServerCommandService.asmx".format(self.ServerApiUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/GetProductInfo",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <GetProductInfo xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                            </GetProductInfo>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token)

                else:

                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(self.LoginInfo.UserName, self.LoginInfo.Password))

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
                # <GetProductInfoResponse>
                #   <GetProductInfoResult>
                #   </GetProductInfoResult>
                # </GetProductInfoResponse>
    
                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "GetProductInfoResult", rsltNamespaces, True)

                # parse response details and return to caller.
                return self._Parse_ProductInfo(oDict, serviceMethodName)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def QueryRecorderInfo(self, recorderId:str) -> XPWRecorder:
        """
        Returns configuration information for an XProtect Recording Server.

        Args:
            recorderId (str):
                The recorder id string of the recording server to query.  

        Returns:
            An XPWRecorder class that contains recording server configuration details 
            for the specified device id.

        Raises:
            XPWWebServiceException:
                The XProtect Web-Services Server returned a failed response.
            XPWException:
                recorderId argument was not supplied.  
                The method fails for any other reason.  

        A XPWWebServiceException will be raised if the specified recorder id
        could not be found.  

        Note that the QueryRecorderInfo only returns the base properties of the recording server
        configuration.  It does not return collection properties (e.g. Cameras, Hardware, Inputs, 
        Outputs, Microphones, Speakers, etc); use the GetConfiguration method to return ALL properties 
        of a recording server.

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWServerCommandService/QueryRecorderInfo.py
        ```
        </details>
        """
        serviceMethodName:str = "QueryRecorderInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Querying Recording Server information")

                # validations.
                if (recorderId == None) or (len(recorderId) ==0):
                    raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("recorderId"), None, _logsi)

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):

                    # formulate xprotect svc service request parameters (url, headers, body).
                    requrl:str = "{0}/ManagementServer/ServerCommandService.svc".format(self.ManagementServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/QueryRecorderInfo",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <QueryRecorderInfo xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                              <recorderId>{recorderId}</recorderId>
                            </QueryRecorderInfo>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   recorderId=recorderId)
                
                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/ServerAPI/ServerCommandService.asmx".format(self.ServerApiUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/QueryRecorderInfo",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <QueryRecorderInfo xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                              <recorderId>{recorderId}</recorderId>
                            </QueryRecorderInfo>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   recorderId=recorderId)
               
                else:

                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(self.LoginInfo.UserName, self.LoginInfo.Password))

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

                # Note that the QueryRecorderInfo only returns the base properties of the recording server
                # configuration.  It does not return Cameras, Hardware, etc - use the GetConfiguration method
                # to return ALL properties of the recording server.

                # SOAP response example:
                # <QueryRecorderInfoResponse>
                #   <QueryRecorderInfoResult>
                #     <RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
                #     <ServiceId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</ServiceId>
                #     <Name>WIN10VM</Name>
                #     <Description>XProtect Recording Server WIN10VM.</Description>
                #     <HostName>WIN10VM</HostName>
                #     <WebServerUri>http://win10vm:7563/</WebServerUri>
                #     <TimeZoneName>Central Standard Time</TimeZoneName>
                #     <DefaultRecordingTimeSeconds>0</DefaultRecordingTimeSeconds>
                #     <XmlEncoding>utf-8</XmlEncoding>
                #     <LastModified>2023-09-12T22:34:38.03Z</LastModified>
                #   </QueryRecorderInfoResult>
                # </QueryRecorderInfoResponse>    

                # search xml response for the results node and create a dictionary from it.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "QueryRecorderInfoResult", rsltNamespaces, True)

                # parse response details and return to caller.
                return self._Parse_RecorderInfo(oDict, serviceMethodName)

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def RegisterIntegration(self, instanceId:str, integrationId:str, integrationVersion:str, integrationName:str, manufacturerName:str) -> None:
        """
    	Registers an integration for the sole purpose of getting an overview 
	    of integration usage.

        Args:
            instanceId (str):
                The globally unique identtifier identifying the calling instance.  
                Typically each ID should refer to a specific machine running an integration.
            integrationId (str):
                The globally unique identtifier representing the integration.   
                Should be hardcoded the integrating application.
            integrationVersion (str):
                Version of the calling application.
            integrationName (str):
                Name of the calling application.
            manufacturerName (str):
                Name of the manufacturer of the calling application.

        Raises:
            XPWWebServiceException:
                The XProtect Web-Services Server returned a failed response.
            XPWException:
                instanceId argument is null or an empty string.  
                integrationId argument is null or an empty string.  
                integrationVersion argument is null or an empty string.  
                integrationName argument is null or an empty string.  
                manufacturerName argument is null or an empty string.  
                The method fails for any other reason.  

        <details>
          <summary>Sample Code</summary><br/>
        ```python
        .. include:: ../docs/include/samplecode/XPWServerCommandService/RegisterIntegration.py
        ```
        </details>
        """
        serviceMethodName:str = "RegisterIntegration"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug) 

            with self._fLock:

                # trace.
                _logsi.LogMessage("Registering Integration information")

                # validations.
                if (instanceId == None) or (len(instanceId) ==0):
                    raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("instanceId"), None, _logsi)
                if (integrationId == None) or (len(integrationId) ==0):
                    raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("integrationId"), None, _logsi)
                if (integrationVersion == None) or (len(integrationVersion) ==0):
                    raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("integrationVersion"), None, _logsi)
                if (integrationName == None) or (len(integrationName) ==0):
                    raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("integrationName"), None, _logsi)
                if (manufacturerName == None) or (len(manufacturerName) ==0):
                    raise XPWException(XPWAppMessages.ARGUMENT_REQUIRED_ERROR.format("manufacturerName"), None, _logsi)

                # automatic token renewal check and logininfo validation.
                self._AutoTokenRenewalCheck(serviceMethodName)

                # call method based upon authentication type.
                if (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Basic):

                    # formulate xprotect svc service request parameters (url, headers, body).
                    requrl:str = "{0}/ManagementServer/ServerCommandService.svc".format(self.ManagementServerUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/IServerCommandService/RegisterIntegration",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <RegisterIntegration xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                              <instanceId>{instanceId}</instanceId>
                              <integrationId>{integrationId}</integrationId>
                              <integrationVersion>{integrationVersion}</integrationVersion>
                              <integrationName>{integrationName}</integrationName>
                              <manufacturerName>{manufacturerName}</manufacturerName>
                            </RegisterIntegration>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   instanceId=instanceId, 
                                   integrationId=integrationId, 
                                   integrationVersion=integrationVersion, 
                                   integrationName=integrationName, 
                                   manufacturerName=manufacturerName)

                elif (self._fLoginInfo.AuthenticationType == XPWAuthenticationType.Windows):

                    # formulate xprotect asmx service request parameters (url, headers, body).
                    requrl:str = "{0}/ServerAPI/ServerCommandService.asmx".format(self.ServerApiUrlPrefix)

                    reqheaders:list[str] = { 
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": "http://videoos.net/2/XProtectCSServerCommand/RegisterIntegration",
                        }

                    reqbody:str = \
                        """
                        <?xml version="1.0" encoding="utf-8"?>
                        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                          <s:Body>
                            <RegisterIntegration xmlns="http://videoos.net/2/XProtectCSServerCommand">
                              <token>{token}</token>
                              <instanceId>{instanceId}</instanceId>
                              <integrationId>{integrationId}</integrationId>
                              <integrationVersion>{integrationVersion}</integrationVersion>
                              <integrationName>{integrationName}</integrationName>
                              <manufacturerName>{manufacturerName}</manufacturerName>
                            </RegisterIntegration>
                          </s:Body>
                        </s:Envelope>
                        """.format(token=self._fLoginInfo.Token, 
                                   instanceId=instanceId, 
                                   integrationId=integrationId, 
                                   integrationVersion=integrationVersion, 
                                   integrationName=integrationName, 
                                   manufacturerName=manufacturerName)

                else:

                    # raise authentication type not implemented exception.
                    raise XPWException(XPWAppMessages.LOGININFO_AUTHTYPE_NOTIMPLEMENTED.format(str(self.LoginInfo.AuthenticationType), serviceMethodName), None, _logsi)

                # create request object.
                req:Request = Request('POST', requrl, headers=reqheaders, data=inspect.cleandoc(reqbody), auth=(self.LoginInfo.UserName, self.LoginInfo.Password))

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
                # <RegisterIntegrationResponse />
    
                # namespaces used in the response xml for this method.
                rsltNamespaces = { 'http://videoos.net/2/XProtectCSRecorderCommand':None,
                                   'http://schemas.microsoft.com/2003/10/Serialization/Arrays':None,
                                   'http://www.w3.org/2001/XMLSchema-instance':None
                                 }

                # check response code; raise an exception if it failed, or return a dictionary with results if it succeeded.
                oDict:dict = self.CheckResponseStatusCode(serviceMethodName, req, resp, "GetProductInfoResult", rsltNamespaces, True)

                # parse valid response.
                # nothing to parse - status 200 indicates success.
                return

        except XPWException: raise  # pass thru exceptions already handled
        except Exception as ex:

            # format unhandled exception.
            raise XPWException(XPWAppMessages.UNHANDLED_EXCEPTION.format(serviceMethodName, str(ex)), ex, _logsi)

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_AlertTypeGroupInfo(self, oDict:dict, serviceMethodName:str) -> XPWAlertTypeGroup:
        """
        Parses dictionary data for AlertTypeGroupInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWAlertTypeGroup class that represents the dictionary details.
        """
        oItem:XPWAlertTypeGroup = None
        methodKeyName:str = "AlertTypeGroupInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<AlertTypeGroupInfo>
            #  <GroupId>00000000-0000-0000-0000-000000000000</GroupId>
            #  <Name>All AlertTypes (Corporate)</Name>
            #  <AlertTypeGroups />
            #  <AlertTypes />
            #</AlertTypeGroupInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWAlertTypeGroup = XPWAlertTypeGroup()
                self._Parse_GroupInfo(oDict, serviceMethodName, oItem)
                self.ParseCollectionItemStrings(oItem.AlertTypes, oDict, "AlertTypes", "guid")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "AlertTypeGroups", "AlertTypeGroupInfo")
                for itemNode in collNodes:
                    oItem.AlertTypeGroups.append(self._Parse_AlertTypeGroupInfo(itemNode, serviceMethodName))

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


    def _Parse_AlertTypeInfo(self, oDict:dict, serviceMethodName:str) -> XPWAlertType:
        """
        Parses dictionary data for AlertTypeInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWAlertType class that represents the dictionary details.
        """
        oItem:XPWAlertType = None
        methodKeyName:str = "AlertTypeInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<AlertTypeInfo>
            #  <AlertTypeId>D3afFfd2-604A-F0eb-acbB-ba33d8D6Aba8</AlertTypeId>
            #  <Name>string</Name>
            #  <Description>string</Description>
            #</AlertTypeInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWAlertType = XPWAlertType()
                oItem.Description = self.GetDictKeyValueString(oDict, "Description")
                oItem.AlertTypeId = self.GetDictKeyValueString(oDict, "AlertTypeId")
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


    def _Parse_ApplicationSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWApplicationSecurity) -> None:
        """
        Parses dictionary data for ApplicationSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
        """
        methodKeyName:str = "ApplicationSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<ApplicationAccess>
            #  <SmartClientSecurity>
            #    <SmartClientBrowse>true</SmartClientBrowse>
            #    <SmartClientLive>true</SmartClientLive>
            #    <SmartClientReport>true</SmartClientReport>
            #    <SmartClientSetup>true</SmartClientSetup>
            #  </SmartClientSecurity>
            #</ApplicationAccess>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                # none.

                if (self.DictHasKey(oDict,"SmartClientSecurity")):
                    self._Parse_SmartClientSecurityInfo(oDict["SmartClientSecurity"], serviceMethodName, oItem.SmartClientSecurity)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_AudioMessageInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWAudioMessage) -> None:
        """
        Parses dictionary data for AudioMessageInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
        """
        methodKeyName:str = "AudioMessageInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<AudioMessages>
            #  <AudioMessageInfo>
            #    <Id>01f1Fe42-DBA7-F0B2-Ac65-B451Ce282427</Id>
            #    <Name>string</Name>
            #    <Description>string</Description>
            #  </AudioMessageInfo>
            #</AudioMessages>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.Description = self.GetDictKeyValueString(oDict, "Description")
                oItem.Id = self.GetDictKeyValueString(oDict, "Id")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_BookmarkSettingsInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWBookmarkSettings) -> None:
        """
        Parses dictionary data for BookmarkSettingsInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
        """
        methodKeyName:str = "BookmarkSettingsInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<BookmarkSettings>
            #  <DefaultPostTimeSec>30</DefaultPostTimeSec>
            #  <DefaultPreTimeSec>3</DefaultPreTimeSec>
            #</BookmarkSettings>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.DefaultPostTimeSec = self.GetDictKeyValueInt(oDict, "DefaultPostTimeSec")
                oItem.DefaultPreTimeSec = self.GetDictKeyValueInt(oDict, "DefaultPreTimeSec")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_CameraGroupInfo(self, oDict:dict, serviceMethodName:str) -> XPWCameraGroup:
        """
        Parses dictionary data for CameraGroupInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWCameraGroup class that represents the dictionary details.
        """
        oItem:XPWCameraGroup = None
        methodKeyName:str = "CameraGroupInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<CameraGroupInfo>
            #  <GroupId>df5f5964-a582-4fa7-a811-3031f1cc18fe</GroupId>
            #  <Name>720p Resolution Cameras</Name>
            #  <Description>All cameras with max resolution of 720p.</Description>
            #  <CameraGroups>
            #    <CameraGroupInfo>
            #      <GroupId>895f3cfe-104b-4a7d-a425-ce70b8491cad</GroupId>
            #      <Name>Office 720P Cameras</Name>
            #      <Description>All Office cameras with max resolution of 720p.</Description>
            #      <CameraGroups />
            #      <Cameras>
            #        <guid>71cab37e-8718-4383-8e86-146b38168e42</guid>
            #      </Cameras>
            #    </CameraGroupInfo>
            #  </CameraGroups>
            #  <Cameras />
            #</CameraGroupInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWCameraGroup = XPWCameraGroup()
                self._Parse_GroupInfo(oDict, serviceMethodName, oItem)
                self.ParseCollectionItemStrings(oItem.Cameras, oDict, "Cameras", "guid")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "CameraGroups", "CameraGroupInfo")
                for itemNode in collNodes:
                    oItem.CameraGroups.append(self._Parse_CameraGroupInfo(itemNode, serviceMethodName))

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


    def _Parse_CameraInfo(self, oDict:dict, serviceMethodName:str) -> XPWCamera:
        """
        Parses dictionary data for CameraInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWCamera class that represents the dictionary details.
        """
        oItem:XPWCamera = None
        methodKeyName:str = "CameraInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<CameraInfo>
            #  <CoverageDepth>0</CoverageDepth>
            #  <CoverageDirection>0</CoverageDirection>
            #  <CoverageFieldOfView>0</CoverageFieldOfView>
            #  <Description>IP = 192.168.1.156, port 8554</Description>
            #  <DeviceId>71cab37e-8718-4383-8e86-146b38168e42</DeviceId>
            #  <DeviceIndex>0</DeviceIndex>
            #  <GisPoint>POINT EMPTY</GisPoint>
            #  <HardwareId>84a1745c-b3bc-47c3-9568-e178441b226c</HardwareId>
            #  <Icon>0</Icon>
            #  <Name>iPadCam03 Office</Name>
            #  <RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
            #  <ShortName>iPadCam03 Office</ShortName>
            #  <Shortcut/>
            #  <BrowsableStream>false</BrowsableStream>
            #  <CameraSecurity />
            #  <EdgeStoragePlayback>false</EdgeStoragePlayback>
            #  <EdgeStorageSupported>false</EdgeStorageSupported>
            #  <IpixSettings />
            #  <MaxFPS>0</MaxFPS>
            #  <MulticastEnabled>false</MulticastEnabled>
            #  <PanoramicLensSettings />
            #  <PtzSettings />
            #  <StopManualRecordingSeconds>300</StopManualRecordingSeconds>
            #  <Streams i:nil="true"/>
            #  <Tracks />
            #</CameraInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWCamera = XPWCamera()
                self._Parse_DeviceInfo(oDict, serviceMethodName, oItem)
                oItem.CoverageDepth = self.GetDictKeyValueFloat(oDict, "CoverageDepth")
                oItem.CoverageDirection = self.GetDictKeyValueFloat(oDict, "CoverageDirection")
                oItem.CoverageFieldOfView = self.GetDictKeyValueFloat(oDict, "CoverageFieldOfView")
                oItem.BrowsableStream = self.GetDictKeyValueBool(oDict, "BrowsableStream")
                oItem.EdgeStoragePlayback = self.GetDictKeyValueBool(oDict, "EdgeStoragePlayback")
                oItem.EdgeStorageSupported = self.GetDictKeyValueBool(oDict, "EdgeStorageSupported")
                oItem.MaxFPS = self.GetDictKeyValueInt(oDict, "MaxFPS")
                oItem.MulticastEnabled = self.GetDictKeyValueBool(oDict, "MulticastEnabled")
                oItem.StopManualRecordingSeconds = self.GetDictKeyValueInt(oDict, "StopManualRecordingSeconds")

                if (self.DictHasKey(oDict,"CameraSecurity")):
                    self._Parse_CameraSecurityInfo(oDict["CameraSecurity"], serviceMethodName, oItem.CameraSecurity)

                if (self.DictHasKey(oDict,"IpixSettings")):
                    self._Parse_IpixInfo(oDict["IpixSettings"], serviceMethodName, oItem.IpixSettings)

                if (self.DictHasKey(oDict,"PanoramicLensSettings")):
                    self._Parse_PanoramicLensInfo(oDict["PanoramicLensSettings"], serviceMethodName, oItem.PanoramicLensSettings)

                if (self.DictHasKey(oDict,"PtzSettings")):
                    self._Parse_PtzInfo(oDict["PtzSettings"], serviceMethodName, oItem.PtzSettings)

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Streams", "StreamInfo")
                for itemNode in collNodes:
                    oItem.Streams.append(self._Parse_StreamInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Tracks", "TrackInfo")
                for itemNode in collNodes:
                    oItem.Tracks.append(self._Parse_TrackInfo(itemNode, serviceMethodName))

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


    def _Parse_CameraSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWCameraSecurity) -> None:
        """
        Parses dictionary data for CameraSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWCameraSecurity):
                An existing XPWCameraSecurity object whose settings will be loaded.
        """
        methodKeyName:str = "CameraSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<CameraSecurity>
            #  <BookmarkAdd>true</BookmarkAdd>
            #  <BookmarkDelete>true</BookmarkDelete>
            #  <BookmarkEdit>true</BookmarkEdit>
            #  <BookmarkView>true</BookmarkView>
            #  <Browse>true</Browse>
            #  <ExportAvi>true</ExportAvi>
            #  <ExportDatabase>true</ExportDatabase>
            #  <ExportJpeg>true</ExportJpeg>
            #  <GetSequences>true</GetSequences>
            #  <Live>true</Live>
            #  <ManagePatrollingProfiles>true</ManagePatrollingProfiles>
            #  <ManagePresetLocks>true</ManagePresetLocks>
            #  <ManagePresets>true</ManagePresets>
            #  <PtzSecurity />
            #  <RestrictedMediaCreate>true</RestrictedMediaCreate>
            #  <RestrictedMediaRemove>true</RestrictedMediaRemove>
            #  <RestrictedMediaView>true</RestrictedMediaView>
            #  <RetentionCreate>true</RetentionCreate>
            #  <RetentionRemove>true</RetentionRemove>
            #  <RetentionView>true</RetentionView>
            #  <RetrieveEdgeRecordings>false</RetrieveEdgeRecordings>
            #  <SmartSearch>true</SmartSearch>
            #  <StartRecording>true</StartRecording>
            #  <StopRecording>true</StopRecording>
            #</CameraSecurity>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.BookmarkAdd = self.GetDictKeyValueBool(oDict, "BookmarkAdd")
                oItem.BookmarkDelete = self.GetDictKeyValueBool(oDict, "BookmarkDelete")
                oItem.BookmarkEdit = self.GetDictKeyValueBool(oDict, "BookmarkEdit")
                oItem.BookmarkView = self.GetDictKeyValueBool(oDict, "BookmarkView")
                oItem.Browse = self.GetDictKeyValueBool(oDict, "Browse")
                oItem.ExportAvi = self.GetDictKeyValueBool(oDict, "ExportAvi")
                oItem.ExportDatabase = self.GetDictKeyValueBool(oDict, "ExportDatabase")
                oItem.ExportJpeg = self.GetDictKeyValueBool(oDict, "ExportJpeg")
                oItem.GetSequences = self.GetDictKeyValueBool(oDict, "GetSequences")
                oItem.Live = self.GetDictKeyValueBool(oDict, "Live")
                oItem.ManagePatrollingProfiles = self.GetDictKeyValueBool(oDict, "ManagePatrollingProfiles")
                oItem.ManagePresetLocks = self.GetDictKeyValueBool(oDict, "ManagePresetLocks")
                oItem.ManagePresets = self.GetDictKeyValueBool(oDict, "ManagePresets")
                oItem.RestrictedMediaCreate = self.GetDictKeyValueBool(oDict, "RestrictedMediaCreate")
                oItem.RestrictedMediaRemove = self.GetDictKeyValueBool(oDict, "RestrictedMediaRemove")
                oItem.RestrictedMediaView = self.GetDictKeyValueBool(oDict, "RestrictedMediaView")
                oItem.RetentionCreate = self.GetDictKeyValueBool(oDict, "RetentionCreate")
                oItem.RetentionRemove = self.GetDictKeyValueBool(oDict, "RetentionRemove")
                oItem.RetentionView = self.GetDictKeyValueBool(oDict, "RetentionView")
                oItem.RetrieveEdgeRecordings = self.GetDictKeyValueBool(oDict, "RetrieveEdgeRecordings")
                oItem.SmartSearch = self.GetDictKeyValueBool(oDict, "SmartSearch")
                oItem.StartRecording = self.GetDictKeyValueBool(oDict, "StartRecording")
                oItem.StopRecording = self.GetDictKeyValueBool(oDict, "StopRecording")

                # process xml result <PtzSecurity> node.
                if (self.DictHasKey(oDict,"PtzSecurity")):
                    self._Parse_PtzSecurityInfo(oDict["PtzSecurity"], serviceMethodName, oItem.PtzSecurity)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_CapabilityInfo(self, oDict:dict, serviceMethodName:str) -> XPWCapability:
        """
        Parses dictionary data for CapabilityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWCapability class that represents the dictionary details.
        """
        oItem:XPWCapability = None
        methodKeyName:str = "CapabilityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<Capabilities>
            #  <CapabilityInfo>
            #    <CapabilityId>FFAee9E5-458f-DCDF-AfcB-39ce0Abc6B38</CapabilityId>
            #    <Name>string</Name>
            #    <Absolute>true</Absolute>
            #    <Relative>true</Relative>
            #    <Start>true</Start>
            #    <Stop>true</Stop>
            #    <Speed>true</Speed>
            #    <Automatic>true</Automatic>
            #  </CapabilityInfo>
            #</Capabilities>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWCapability = XPWCapability()
                oItem.Absolute = self.GetDictKeyValueBool(oDict, "Absolute")
                oItem.Automatic = self.GetDictKeyValueBool(oDict, "Automatic")
                oItem.CapabilityId = self.GetDictKeyValueString(oDict, "CapabilityId")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")
                oItem.Relative = self.GetDictKeyValueBool(oDict, "Relative")
                oItem.Speed = self.GetDictKeyValueBool(oDict, "Speed")
                oItem.Start = self.GetDictKeyValueBool(oDict, "Start")
                oItem.Stop = self.GetDictKeyValueBool(oDict, "Stop")

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


    def _Parse_ConfigurationInfo(self, oDict:dict, serviceMethodName:str) -> XPWConfiguration:
        """
        Parses dictionary data for ConfigurationInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWConfiguration class that represents the dictionary details.
        """
        oItem:XPWConfiguration = None
        methodKeyName:str = "ConfigurationInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<ApplicationAccess />
            #<AudioMessages />
            #<AlertTypes />
            #<AlertTypeGroups />
            #<Cameras i:nil="true"/>
            #<CameraGroups i:nil="true"/>
            #<DefaultRecordingTimeSeconds>0</DefaultRecordingTimeSeconds>
            #<Description>XProtect Recording Server WIN10VM.</Description>
            #<DeviceMappings i:nil="true"/>
            #<EventTypeGroups/>
            #<EventTypes />
            #<Hardware i:nil="true"/>
            #<HostName>WIN10VM</HostName>
            #<Inputs i:nil="true"/>
            #<LastModified>2023-07-28T00:22:21.82Z</LastModified>
            #<MetadataDevices i:nil="true"/>
            #<MatrixMonitors />
            #<Microphones i:nil="true"/>
            #<Name>WIN10VM</Name>
            #<Outputs i:nil="true"/>
            #<RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
            #<ServiceId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</ServiceId>
            #<Speakers i:nil="true"/>
            #<TimeZoneName>Central Standard Time</TimeZoneName>
            #<WebServerUri>http://win10vm:7563/</WebServerUri>
            #<XmlEncoding>utf-8</XmlEncoding>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # load base properties.
                oItem = XPWConfiguration()
                oItem.FailoverCheckInterval = self.GetDictKeyValueInt(oDict, "FailoverCheckInterval")
                oItem.ServerDescription = self.GetDictKeyValueString(oDict, "ServerDescription")
                oItem.ServerId = self.GetDictKeyValueString(oDict, "ServerId")
                oItem.ServerName = self.GetDictKeyValueString(oDict, "ServerName")

                if (self.DictHasKey(oDict,"ApplicationAccess")):
                    self._Parse_ApplicationSecurityInfo(oDict["ApplicationAccess"], serviceMethodName, oItem.ApplicationAccess)

                if (self.DictHasKey(oDict,"BookmarkSettings")):
                    self._Parse_BookmarkSettingsInfo(oDict["BookmarkSettings"], serviceMethodName, oItem.BookmarkSettings)

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "AlertTypeGroups", "AlertTypeGroupInfo")
                for itemNode in collNodes:
                    oItem.AlertTypeGroups.append(self._Parse_AlertTypeGroupInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "AlertTypes", "AlertTypeInfo")
                for itemNode in collNodes:
                    oItem.AlertTypes.append(self._Parse_AlertTypeInfo(itemNode, serviceMethodName))
  
                # does results dictionary contain "<AudioMessages>" key?
                if (self.DictHasKey(oDict,"AudioMessages")):
  
                    # map the settings block.
                    oDict_Child:dict = oDict["AudioMessages"]

                    # note - per the milestone docs, the "AudioMessages" property is just a single "AudioMessageInfo" 
                    # object (e.g. NOT a collection of "AudioMessageInfo" objects).
                    if (self.DictHasKey(oDict_Child,"AudioMessageInfo")):
                        self._Parse_AudioMessageInfo(oDict_Child["AudioMessageInfo"], serviceMethodName, oItem.AudioMessages)

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "CameraGroups", "CameraGroupInfo")
                for itemNode in collNodes:
                    oItem.CameraGroups.append(self._Parse_CameraGroupInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "EventTypeGroups", "EventTypeGroupInfo")
                for itemNode in collNodes:
                    oItem.EventTypeGroups.append(self._Parse_EventTypeGroupInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "EventTypes", "EventTypeInfo")
                for itemNode in collNodes:
                    oItem.EventTypes.append(self._Parse_EventTypeInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "DeviceMappings", "DeviceMappingInfo")
                for itemNode in collNodes:
                    oItem.DeviceMappings.append(self._Parse_DeviceMappingInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "InputGroups", "InputGroupInfo")
                for itemNode in collNodes:
                    oItem.InputGroups.append(self._Parse_InputGroupInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Licenses", "LicenseInfo")
                for itemNode in collNodes:
                    oItem.Licenses.append(self._Parse_LicenseInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "MatrixMonitors", "MatrixMonitorInfo")
                for itemNode in collNodes:
                    oItem.MatrixMonitors.append(self._Parse_MatrixMonitorInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "MicrophoneGroups", "MicrophoneGroupInfo")
                for itemNode in collNodes:
                    oItem.MicrophoneGroups.append(self._Parse_MicrophoneGroupInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "OutputGroups", "OutputGroupInfo")
                for itemNode in collNodes:
                    oItem.OutputGroups.append(self._Parse_OutputGroupInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Recorders", "RecorderInfo")
                for itemNode in collNodes:
                    oItem.Recorders.append(self._Parse_RecorderInfo(itemNode, serviceMethodName))
  
                # does results dictionary contain "<RetentionSettings>" key?
                if (self.DictHasKey(oDict,"RetentionSettings")):
  
                    # map the settings block.
                    oDict_Child:dict = oDict["RetentionSettings"]

                    # process xml result collection item node(s).
                    collNodes:dict = self.GetDictCollectionItems(oDict_Child, "RetentionOptions", "RetentionOption")
                    for itemNode in collNodes:
                        oItem.RetentionOptions.append(self._Parse_RetentionOption(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "ServerOptions", "ServerOption")
                for itemNode in collNodes:
                    oItem.ServerOptions.append(self._Parse_ServerOption(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "SpeakerGroups", "SpeakerGroupInfo")
                for itemNode in collNodes:
                    oItem.SpeakerGroups.append(self._Parse_SpeakerGroupInfo(itemNode, serviceMethodName))
  
                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "SystemEventTypes", "SystemEventTypeInfo")
                for itemNode in collNodes:
                    oItem.SystemEventTypes.append(self._Parse_SystemEventTypeInfo(itemNode, serviceMethodName))

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


    def _Parse_DeviceDisabledInfo(self, oDict:dict, serviceMethodName:str) -> XPWDeviceDisabled:
        """
        Parses dictionary data for DeviceDisabledInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWDeviceDisabled class that represents the dictionary details.
        """
        oItem:XPWDeviceDisabled = None
        methodKeyName:str = "DeviceDisabledInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<DeviceDisabledInfo>
            #  <DeviceId>0c60e7bf-9d57-4047-b623-e76d375a1fe6</DeviceId>
            #  <DeviceName>iPadCam01 Camera</DeviceName>
            #  <DeviceType>Camera</DeviceType>
            #  <HardwareId>08cf6a24-c7ab-4b50-80e0-5a56cf624c5f</HardwareId>
            #  <RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
            #</DeviceDisabledInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWDeviceDisabled = XPWDeviceDisabled()
                oItem.DeviceId = self.GetDictKeyValueString(oDict, "DeviceId")
                oItem.DeviceName = self.GetDictKeyValueString(oDict, "DeviceName")
                oItem.DeviceType = self.GetDictKeyValueString(oDict, "DeviceType")
                oItem.HardwareId = self.GetDictKeyValueString(oDict, "HardwareId")
                oItem.RecorderId = self.GetDictKeyValueString(oDict, "RecorderId")

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


    def _Parse_DeviceInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWDevice) -> None:
        """
        Parses dictionary data for DeviceInfo base class details.  

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWDevice):
                Object that inherits from XPWDevice base class.

        This can be used for any methods that parse properties for classes that inherit 
        from the XPWDevice base class (e.g. XPWCamera, XPWInput, XPWOutput,
        XPWMicrophone, XPWMetadataDevice, XPWSpeaker).
        """
        methodKeyName:str = "DeviceInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<DeviceInfo>
            #  <RecorderId>EEC28fa5-bDae-a0fD-f033-7D95FadD8CFf</RecorderId>
            #  <HardwareId>fe1CD5B7-F748-CF80-DFF2-7f2D4Bf0e8F7</HardwareId>
            #  <DeviceId>24bBea6e-08e4-Fd1a-9aB6-0373fcA3e3fd</DeviceId>
            #  <Name>string</Name>
            #  <Description>string</Description>
            #  <Shortcut>string</Shortcut>
            #  <DeviceIndex>100</DeviceIndex>
            #  <GisPoint>string</GisPoint>
            #  <ShortName>string</ShortName>
            #  <Icon>100</Icon>
            #</DeviceInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.Description = self.GetDictKeyValueString(oDict, "Description")
                oItem.DeviceId = self.GetDictKeyValueString(oDict, "DeviceId")
                oItem.DeviceIndex = self.GetDictKeyValueInt(oDict, "DeviceIndex")
                oItem.GisPoint = self.GetDictKeyValueString(oDict, "GisPoint")
                oItem.HardwareId = self.GetDictKeyValueString(oDict, "HardwareId")
                oItem.Icon = self.GetDictKeyValueInt(oDict, "Icon")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")
                oItem.RecorderId = self.GetDictKeyValueString(oDict, "RecorderId")
                oItem.ShortName = self.GetDictKeyValueString(oDict, "ShortName")

                # trace.
                # if (_logsi.IsOn(SILevel.Verbose)):
                #     _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_DeviceMappingInfo(self, oDict:dict, serviceMethodName:str) -> XPWDeviceMapping:
        """
        Parses dictionary data for DeviceMappingInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWDeviceMapping class that represents the dictionary details.
        """
        oItem:XPWDeviceMapping = None
        methodKeyName:str = "DeviceMappingInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<DeviceMappingInfo>
            #  <DeviceA>0c60e7bf-9d57-4047-b623-e76d375a1fe6</DeviceA>
            #  <DeviceB>8a381bcc-7752-45dd-91f2-3aa8345d37db</DeviceB>
            #</DeviceMappingInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWDeviceMapping = XPWDeviceMapping()
                oItem.DeviceA = self.GetDictKeyValueString(oDict, "DeviceA")
                oItem.DeviceB = self.GetDictKeyValueString(oDict, "DeviceB")

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


    def _Parse_EventTypeGroupInfo(self, oDict:dict, serviceMethodName:str) -> XPWEventTypeGroup:
        """
        Parses dictionary data for EventTypeGroupInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWEventTypeGroup class that represents the dictionary details.
        """
        oItem:XPWEventTypeGroup = None
        methodKeyName:str = "EventTypeGroupInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<EventTypeGroupInfo>
            #  <GroupId>0aca1fc0-7c58-4b39-8629-fbe2a4a760e6</GroupId>
            #  <Name>iPad EventTypes</Name>
            #  <Description />
            #  <EventTypeGroups />
            #  <EventTypes>
            #    <guid>3be8e5c6-939a-4a31-bb89-2205e5d54d15</guid>
            #    <guid>7cdddfdd-ace8-491d-b38c-0b00f0cd9a3b</guid>
            #    <guid>8a381bcc-7752-45dd-91f2-3aa8345d37db</guid>
            #  </EventTypes>
            #</EventTypeGroupInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWEventTypeGroup = XPWEventTypeGroup()
                self._Parse_GroupInfo(oDict, serviceMethodName, oItem)
                self.ParseCollectionItemStrings(oItem.EventTypes, oDict, "EventTypes", "guid")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "EventTypeGroups", "EventTypeGroupInfo")
                for itemNode in collNodes:
                    oItem.EventTypeGroups.append(self._Parse_EventTypeGroupInfo(itemNode, serviceMethodName))

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


    def _Parse_EventTypeInfo(self, oDict:dict, serviceMethodName:str) -> XPWEventType:
        """
        Parses dictionary data for EventTypeInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWEventType class that represents the dictionary details.
        """
        oItem:XPWEventType = None
        methodKeyName:str = "EventTypeInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<EventTypeInfo>
            #  <EventTypeId>D3afFfd2-604A-F0eb-acbB-ba33d8D6Aba8</EventTypeId>
            #  <Name>string</Name>
            #  <Description>string</Description>
            #</EventTypeInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWEventType = XPWEventType()
                oItem.Description = self.GetDictKeyValueString(oDict, "Description")
                oItem.EventTypeId = self.GetDictKeyValueString(oDict, "EventTypeId")
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


    def _Parse_GroupInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWGroup) -> None:
        """
        Parses dictionary data for GroupInfo base class details.  

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWGroup):
                Object that inherits from XPWGroup base class.

        This can be used for any methods that parse properties for classes that inherit 
        from the XPWGroup base class (e.g. XPWCameraGroup, XPWMicrophoneGroup, etc).
        """
        methodKeyName:str = "GroupInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<GroupInfo>
            #  <Description>Group Description.</Description>
            #  <GroupId>EEC28fa5-bDae-a0fD-f033-7D95FadD8CFf</GroupId>
            #  <Name>Group Name</Name>
            #</GroupInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.Description = self.GetDictKeyValueString(oDict, "Description")
                oItem.GroupId = self.GetDictKeyValueString(oDict, "GroupId")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_HardwareInfo(self, oDict:dict, serviceMethodName:str) -> XPWHardware:
        """
        Parses dictionary data for HardwareInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWHardware class that represents the dictionary details.
        """
        oItem:XPWHardware = None
        methodKeyName:str = "HardwareInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<HardwareInfo>
            #  <HardwareId>08cf6a24-c7ab-4b50-80e0-5a56cf624c5f</HardwareId>
            #  <DeviceIds>
            #    <guid>0c60e7bf-9d57-4047-b623-e76d375a1fe6</guid>
            #    <guid>8a381bcc-7752-45dd-91f2-3aa8345d37db</guid>
            #  </DeviceIds>
            #  <RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
            #  <Name>iPadCam01</Name>
            #  <Description>iPad Camera and Microphone via LiveReporter RTSP Streaming.
            #  <Uri>http://192.168.1.154:8554/</Uri>
            #  <Interconnected>false</Interconnected>
            #  <LastModified>2023-06-26T23:49:14.05Z</LastModified>
            #</HardwareInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWHardware = XPWHardware()
                oItem.HardwareId = self.GetDictKeyValueString(oDict, "HardwareId")
                oItem.RecorderId = self.GetDictKeyValueString(oDict, "RecorderId")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")
                oItem.Description = self.GetDictKeyValueString(oDict, "Description")
                oItem.Uri = self.GetDictKeyValueString(oDict, "Uri")
                oItem.Interconnected = self.GetDictKeyValueBool(oDict, "Interconnected")
                oItem.LastModified = self.GetDictKeyValueDateTime(oDict, "LastModified")
                self.ParseCollectionItemStrings(oItem.DeviceIds, oDict, "DeviceIds", "guid")

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


    def _Parse_HemisphereInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWHemisphere) -> None:
        """
        Parses dictionary data for HemisphereInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWHemisphere):
                An existing XPWHemisphere object whose settings will be loaded.
        """
        methodKeyName:str = "HemisphereInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<Hemisphere>
            #  <CenterX>0</CenterX>
            #  <CenterY>0</CenterY>
            #  <RadiusX>0</RadiusX>
            #  <RadiusY>0</RadiusY>
            #</Hemisphere>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.CenterX = self.GetDictKeyValueString(oDict, "CenterX")
                oItem.CenterY = self.GetDictKeyValueString(oDict, "CenterY")
                oItem.RadiusX = self.GetDictKeyValueString(oDict, "RadiusX")
                oItem.RadiusY = self.GetDictKeyValueString(oDict, "RadiusY")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_ImmerVisionInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWImmerVision) -> None:
        """
        Parses dictionary data for ImmerVisionInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWImmerVision):
                An existing XPWImmerVision object whose settings will be loaded.
        """
        methodKeyName:str = "ImmerVisionInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<ImmerVision>
            #    <LensProfileData>Value</LensProfileData>
            #    <LensProfileName>Value</LensProfileName>
            #    <LensProfileRpl>Value</LensProfileRpl>
            #</ImmerVision>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.LensProfileData = self.GetDictKeyValueString(oDict, "LensProfileData")
                oItem.LensProfileName = self.GetDictKeyValueString(oDict, "LensProfileName")
                oItem.LensProfileRpl = self.GetDictKeyValueString(oDict, "LensProfileRpl")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_InputGroupInfo(self, oDict:dict, serviceMethodName:str) -> XPWInputGroup:
        """
        Parses dictionary data for InputGroupInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWInputGroup class that represents the dictionary details.
        """
        oItem:XPWInputGroup = None
        methodKeyName:str = "InputGroupInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<InputGroupInfo>
            #  <GroupId>0aca1fc0-7c58-4b39-8629-fbe2a4a760e6</GroupId>
            #  <Name>iPad Inputs</Name>
            #  <Description />
            #  <InputGroups />
            #  <Inputs>
            #    <guid>3be8e5c6-939a-4a31-bb89-2205e5d54d15</guid>
            #    <guid>7cdddfdd-ace8-491d-b38c-0b00f0cd9a3b</guid>
            #    <guid>8a381bcc-7752-45dd-91f2-3aa8345d37db</guid>
            #  </Inputs>
            #</InputGroupInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWInputGroup = XPWInputGroup()
                self._Parse_GroupInfo(oDict, serviceMethodName, oItem)
                self.ParseCollectionItemStrings(oItem.Inputs, oDict, "Inputs", "guid")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "InputGroups", "InputGroupInfo")
                for itemNode in collNodes:
                    oItem.InputGroups.append(self._Parse_InputGroupInfo(itemNode, serviceMethodName))

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


    def _Parse_InputInfo(self, oDict:dict, serviceMethodName:str) -> XPWInput:
        """
        Parses dictionary data for InputInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWInput class that represents the dictionary details.
        """
        oItem:XPWInput = None
        methodKeyName:str = "InputInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<InputInfo>
            #  <RecorderId>2292124c-19CE-128b-Da0A-B2Ce5ecA19Ce</RecorderId>
            #  <HardwareId>59BCff2c-DB83-8A9f-72aF-d26928040e7D</HardwareId>
            #  <DeviceId>6fedc4a2-A21e-F3cE-7EB0-1E71464Ec241</DeviceId>
            #  <Name>string</Name>
            #  <Description>string</Description>
            #  <Shortcut>string</Shortcut>
            #  <DeviceIndex>100</DeviceIndex>
            #  <GisPoint>string</GisPoint>
            #  <ShortName>string</ShortName>
            #  <Icon>100</Icon>
            #  <CoverageDirection>17</CoverageDirection>
            #  <CoverageDepth>39</CoverageDepth>
            #  <CoverageFieldOfView>35</CoverageFieldOfView>
            #  <InputSecurity />
            #</InputInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWInput = XPWInput()
                self._Parse_DeviceInfo(oDict, serviceMethodName, oItem)
                oItem.CoverageDepth = self.GetDictKeyValueFloat(oDict, "CoverageDepth")
                oItem.CoverageDirection = self.GetDictKeyValueFloat(oDict, "CoverageDirection")
                oItem.CoverageFieldOfView = self.GetDictKeyValueFloat(oDict, "CoverageFieldOfView")

                if (self.DictHasKey(oDict,"InputSecurity")):
                    self._Parse_InputSecurityInfo(oDict["InputSecurity"], serviceMethodName, oItem.InputSecurity)

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


    def _Parse_InputSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWInputSecurity) -> None:
        """
        Parses dictionary data for InputSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWInputSecurity):
                An existing XPWInputSecurity object whose settings will be loaded.
        """
        methodKeyName:str = "InputSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<InputSecurity>
            #  <ReadInput>true</ReadInput>
            #</InputSecurity>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.ReadInput = self.GetDictKeyValueBool(oDict, "ReadInput")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_IpixInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWIpix) -> None:
        """
        Parses dictionary data for IpixInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWIpix):
                An existing XPWIpix object whose settings will be loaded.
        """
        methodKeyName:str = "IpixInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<IpixSettings>
            #    <CeilingMounted>false</CeilingMounted>
            #    <Hemisphere i:nil="true"/>
            #    <Homeposition i:nil="true"/>
            #    <IpixEnabled>false</IpixEnabled>
            #</IpixSettings>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.CeilingMounted = self.GetDictKeyValueBool(oDict, "CeilingMounted")
                oItem.IpixEnabled = self.GetDictKeyValueBool(oDict, "IpixEnabled")

                # process xml result <Hemisphere> node.
                if (self.DictHasKey(oDict,"Hemisphere")):
                    self._Parse_HemisphereInfo(oDict["Hemisphere"], serviceMethodName, oItem.Hemisphere)

                # process xml result <Hemisphere> node.
                if (self.DictHasKey(oDict,"Homeposition")):
                    self._Parse_PositionInfo(oDict["Homeposition"], serviceMethodName, oItem.Homeposition)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_LicenseInfo(self, oDict:dict, serviceMethodName:str) -> XPWLicense:
        """
        Parses dictionary data for LicenseInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWLicense class that represents the dictionary details.
        """
        oItem:XPWLicense = None
        methodKeyName:str = "LicenseInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<Licenses>
            #  <LicenseInfo>
            #    <LicenseId>0109dd80-139a-48b3-93d1-9dcb4f9eaa20</LicenseId>
            #    <Data>&lt;pluginconfiguration id="0109DD80-139A-48b3-93D1-9DCB4F9EAA20" plugin="VideoOS.RemoteClient.Application\Actions\PtzMoveContinuousUpAction" /&gt;</Data>
            #  </LicenseInfo>
            #</Licenses>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWLicense = XPWLicense()
                oItem.Data = self.GetDictKeyValueString(oDict, "Data")
                oItem.LicenseId = self.GetDictKeyValueString(oDict, "LicenseId")

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


    def _Parse_MatrixMonitorInfo(self, oDict:dict, serviceMethodName:str) -> XPWMatrixMonitor:
        """
        Parses dictionary data for MatrixMonitorInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWMatrixMonitor class that represents the dictionary details.
        """
        oItem:XPWMatrixMonitor = None
        methodKeyName:str = "MatrixMonitorInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<MatrixMonitorInfo>
            #  <MatrixMonitorId>D3afFfd2-604A-F0eb-acbB-ba33d8D6Aba8</MatrixMonitorId>
            #  <DisplayName>string</DisplayName>
            #</MatrixMonitorInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWMatrixMonitor = XPWMatrixMonitor()
                oItem.DisplayName = self.GetDictKeyValueString(oDict, "DisplayName")
                oItem.MatrixMonitorId = self.GetDictKeyValueString(oDict, "MatrixMonitorId")

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


    def _Parse_MetadataDeviceInfo(self, oDict:dict, serviceMethodName:str) -> XPWMetadataDevice:
        """
        Parses dictionary data for MetadataDeviceInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWMetadataDevice class that represents the dictionary details.
        """
        oItem:XPWMetadataDevice = None
        methodKeyName:str = "MetadataDeviceInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<MetadataDeviceInfo>
            #  <CoverageDirection>33</CoverageDirection>
            #  <CoverageDepth>62</CoverageDepth>
            #  <CoverageFieldOfView>86</CoverageFieldOfView>
            #  <Tracks/>
            #  <MetadataDeviceSecurity />
            #  <MulticastEnabled>true</MulticastEnabled>
            #  <EdgeStorageSupported>true</EdgeStorageSupported>
            #  <EdgeStoragePlayback>true</EdgeStoragePlayback>
            #  <MetadataTypes />
            #  <StopManualRecordingSeconds>100</StopManualRecordingSeconds>
            #</MetadataDeviceInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWMetadataDevice = XPWMetadataDevice()
                self._Parse_DeviceInfo(oDict, serviceMethodName, oItem)
                oItem.CoverageDepth = self.GetDictKeyValueFloat(oDict, "CoverageDepth")
                oItem.CoverageDirection = self.GetDictKeyValueFloat(oDict, "CoverageDirection")
                oItem.CoverageFieldOfView = self.GetDictKeyValueFloat(oDict, "CoverageFieldOfView")
                oItem.EdgeStoragePlayback = self.GetDictKeyValueBool(oDict, "EdgeStoragePlayback")
                oItem.EdgeStorageSupported = self.GetDictKeyValueBool(oDict, "EdgeStorageSupported")
                oItem.MulticastEnabled = self.GetDictKeyValueBool(oDict, "MulticastEnabled")
                oItem.StopManualRecordingSeconds = self.GetDictKeyValueInt(oDict, "StopManualRecordingSeconds")

                if (self.DictHasKey(oDict,"MetadataDeviceSecurity")):
                    self._Parse_MetadataDeviceSecurityInfo(oDict["MetadataDeviceSecurity"], serviceMethodName, oItem.MetadataDeviceSecurity)

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Tracks", "TrackInfo")
                for itemNode in collNodes:
                    oItem.Tracks.append(self._Parse_TrackInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "MetadataTypes", "MetadataTypeInfo")
                for itemNode in collNodes:
                    oItem.MetadataTypes.append(self._Parse_MetadataTypeInfo(itemNode, serviceMethodName))

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


    def _Parse_MetadataDeviceSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWMetadataDeviceSecurity) -> None:
        """
        Parses dictionary data for MetadataDeviceSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWMetadataDeviceSecurity):
                An existing XPWMetadataDeviceSecurity object whose settings will be loaded.
        """
        methodKeyName:str = "MetadataDeviceSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<MetadataDeviceSecurity>
            #  <Live>true</Live>
            #  <Browse>true</Browse>
            #  <GetSequences>true</GetSequences>
            #  <ExportDatabase>true</ExportDatabase>
            #  <RetrieveEdgeRecordings>true</RetrieveEdgeRecordings>
            #  <StartRecording>true</StartRecording>
            #  <StopRecording>true</StopRecording>
            #  <RetentionView>true</RetentionView>
            #  <RetentionCreate>true</RetentionCreate>
            #  <RetentionRemove>true</RetentionRemove>
            #  <RestrictedMediaView>true</RestrictedMediaView>
            #  <RestrictedMediaCreate>true</RestrictedMediaCreate>
            #  <RestrictedMediaRemove>true</RestrictedMediaRemove>
            #</MetadataDeviceSecurity>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.Browse = self.GetDictKeyValueBool(oDict, "Browse")
                oItem.ExportDatabase = self.GetDictKeyValueBool(oDict, "ExportDatabase")
                oItem.GetSequences = self.GetDictKeyValueBool(oDict, "GetSequences")
                oItem.Live = self.GetDictKeyValueBool(oDict, "Live")
                oItem.RestrictedMediaCreate = self.GetDictKeyValueBool(oDict, "RestrictedMediaCreate")
                oItem.RestrictedMediaRemove = self.GetDictKeyValueBool(oDict, "RestrictedMediaRemove")
                oItem.RestrictedMediaView = self.GetDictKeyValueBool(oDict, "RestrictedMediaView")
                oItem.RetentionCreate = self.GetDictKeyValueBool(oDict, "RetentionCreate")
                oItem.RetentionRemove = self.GetDictKeyValueBool(oDict, "RetentionRemove")
                oItem.RetentionView = self.GetDictKeyValueBool(oDict, "RetentionView")
                oItem.RetrieveEdgeRecordings = self.GetDictKeyValueBool(oDict, "RetrieveEdgeRecordings")
                oItem.StartRecording = self.GetDictKeyValueBool(oDict, "StartRecording")
                oItem.StopRecording = self.GetDictKeyValueBool(oDict, "StopRecording")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_MetadataTypeInfo(self, oDict:dict, serviceMethodName:str) -> XPWMetadataType:
        """
        Parses dictionary data for MetadataTypeInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWMetadataType class that represents the dictionary details.
        """
        oItem:XPWMetadataType = None
        methodKeyName:str = "MetadataTypeInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<MetadataTypes>
            #  <MetadataTypeInfo>
            #    <Id>19B76e0b-61f1-f314-EDD8-7bC2a90Ec2ce</Id>
            #    <Name>string</Name>
            #    <DisplayId>6A8d7904-ddf2-226A-8326-8796ABFe0D97</DisplayId>
            #    <DisplayName>string</DisplayName>
            #    <ValidTime>100</ValidTime>
            #  </MetadataTypeInfo>
            #</MetadataTypes>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWMetadataType = XPWMetadataType()
                oItem.DisplayId = self.GetDictKeyValueString(oDict, "DisplayId")
                oItem.DisplayName = self.GetDictKeyValueString(oDict, "DisplayName")
                oItem.Id = self.GetDictKeyValueString(oDict, "Id")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")
                oItem.ValidTime = self.GetDictKeyValueString(oDict, "ValidTime")

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


    def _Parse_MicrophoneGroupInfo(self, oDict:dict, serviceMethodName:str) -> XPWMicrophoneGroup:
        """
        Parses dictionary data for MicrophoneGroupInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWMicrophoneGroup class that represents the dictionary details.
        """
        oItem:XPWMicrophoneGroup = None
        methodKeyName:str = "MicrophoneGroupInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<MicrophoneGroupInfo>
            #  <GroupId>0aca1fc0-7c58-4b39-8629-fbe2a4a760e6</GroupId>
            #  <Name>iPad Microphones</Name>
            #  <Description />
            #  <MicrophoneGroups />
            #  <Microphones>
            #    <guid>3be8e5c6-939a-4a31-bb89-2205e5d54d15</guid>
            #    <guid>7cdddfdd-ace8-491d-b38c-0b00f0cd9a3b</guid>
            #    <guid>8a381bcc-7752-45dd-91f2-3aa8345d37db</guid>
            #  </Microphones>
            #</MicrophoneGroupInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWMicrophoneGroup = XPWMicrophoneGroup()
                self._Parse_GroupInfo(oDict, serviceMethodName, oItem)
                self.ParseCollectionItemStrings(oItem.Microphones, oDict, "Microphones", "guid")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "MicrophoneGroups", "MicrophoneGroupInfo")
                for itemNode in collNodes:
                    oItem.MicrophoneGroups.append(self._Parse_MicrophoneGroupInfo(itemNode, serviceMethodName))

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


    def _Parse_MicrophoneInfo(self, oDict:dict, serviceMethodName:str) -> XPWMicrophone:
        """
        Parses dictionary data for MicrophoneInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWMicrophone class that represents the dictionary details.
        """
        oItem:XPWMicrophone = None
        methodKeyName:str = "MicrophoneInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<MicrophoneInfo>
            #  <RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
            #  <HardwareId>a9c997f4-c5db-49e7-9f7e-8d4474f5a13f</HardwareId>
            #  <DeviceId>3be8e5c6-939a-4a31-bb89-2205e5d54d15</DeviceId>
            #  <Name>iPadCam02 Microphone</Name>
            #  <Description />
            #  <Shortcut />
            #  <DeviceIndex>0</DeviceIndex>
            #  <GisPoint>POINT EMPTY</GisPoint>
            #  <ShortName />
            #  <Icon>0</Icon>
            #  <CoverageDirection>0</CoverageDirection>
            #  <CoverageDepth>0</CoverageDepth>
            #  <CoverageFieldOfView>0</CoverageFieldOfView>
            #  <Tracks />
            #  <MicrophoneSecurity />
            #  <MulticastEnabled>false</MulticastEnabled>
            #  <EdgeStorageSupported>false</EdgeStorageSupported>
            #  <EdgeStoragePlayback>false</EdgeStoragePlayback>
            #  <StopManualRecordingSeconds>300</StopManualRecordingSeconds>
            #</MicrophoneInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWMicrophone = XPWMicrophone()
                self._Parse_DeviceInfo(oDict, serviceMethodName, oItem)
                oItem.CoverageDepth = self.GetDictKeyValueFloat(oDict, "CoverageDepth")
                oItem.CoverageDirection = self.GetDictKeyValueFloat(oDict, "CoverageDirection")
                oItem.CoverageFieldOfView = self.GetDictKeyValueFloat(oDict, "CoverageFieldOfView")
                oItem.EdgeStoragePlayback = self.GetDictKeyValueBool(oDict, "EdgeStoragePlayback")
                oItem.EdgeStorageSupported = self.GetDictKeyValueBool(oDict, "EdgeStorageSupported")
                oItem.MulticastEnabled = self.GetDictKeyValueBool(oDict, "MulticastEnabled")
                oItem.StopManualRecordingSeconds = self.GetDictKeyValueInt(oDict, "StopManualRecordingSeconds")

                if (self.DictHasKey(oDict,"MicrophoneSecurity")):
                    self._Parse_MicrophoneSecurityInfo(oDict["MicrophoneSecurity"], serviceMethodName, oItem.MicrophoneSecurity)

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Tracks", "TrackInfo")
                for itemNode in collNodes:
                    oItem.Tracks.append(self._Parse_TrackInfo(itemNode, serviceMethodName))

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


    def _Parse_MicrophoneSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWMicrophoneSecurity) -> None:
        """
        Parses dictionary data for MicrophoneSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWMicrophoneSecurity):
                An existing XPWMicrophoneSecurity object whose settings will be loaded.
        """
        methodKeyName:str = "MicrophoneSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<MicrophoneSecurity>
            #  <Live>true</Live>
            #  <Browse>true</Browse>
            #  <GetSequences>true</GetSequences>
            #  <ExportDatabase>true</ExportDatabase>
            #  <BookmarkView>true</BookmarkView>
            #  <BookmarkAdd>true</BookmarkAdd>
            #  <BookmarkEdit>true</BookmarkEdit>
            #  <BookmarkDelete>true</BookmarkDelete>
            #  <RetentionView>true</RetentionView>
            #  <RetentionCreate>true</RetentionCreate>
            #  <RetentionRemove>true</RetentionRemove>
            #  <RetrieveEdgeRecordings>false</RetrieveEdgeRecordings>
            #  <StartRecording>true</StartRecording>
            #  <StopRecording>true</StopRecording>
            #  <RestrictedMediaView>true</RestrictedMediaView>
            #  <RestrictedMediaCreate>true</RestrictedMediaCreate>
            #  <RestrictedMediaRemove>true</RestrictedMediaRemove>
            #</MicrophoneSecurity>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.BookmarkAdd = self.GetDictKeyValueBool(oDict, "BookmarkAdd")
                oItem.BookmarkDelete = self.GetDictKeyValueBool(oDict, "BookmarkDelete")
                oItem.BookmarkEdit = self.GetDictKeyValueBool(oDict, "BookmarkEdit")
                oItem.BookmarkView = self.GetDictKeyValueBool(oDict, "BookmarkView")
                oItem.Browse = self.GetDictKeyValueBool(oDict, "Browse")
                oItem.ExportDatabase = self.GetDictKeyValueBool(oDict, "ExportDatabase")
                oItem.GetSequences = self.GetDictKeyValueBool(oDict, "GetSequences")
                oItem.Live = self.GetDictKeyValueBool(oDict, "Live")
                oItem.RestrictedMediaCreate = self.GetDictKeyValueBool(oDict, "RestrictedMediaCreate")
                oItem.RestrictedMediaRemove = self.GetDictKeyValueBool(oDict, "RestrictedMediaRemove")
                oItem.RestrictedMediaView = self.GetDictKeyValueBool(oDict, "RestrictedMediaView")
                oItem.RetentionCreate = self.GetDictKeyValueBool(oDict, "RetentionCreate")
                oItem.RetentionRemove = self.GetDictKeyValueBool(oDict, "RetentionRemove")
                oItem.RetentionView = self.GetDictKeyValueBool(oDict, "RetentionView")
                oItem.RetrieveEdgeRecordings = self.GetDictKeyValueBool(oDict, "RetrieveEdgeRecordings")
                oItem.StartRecording = self.GetDictKeyValueBool(oDict, "StartRecording")
                oItem.StopRecording = self.GetDictKeyValueBool(oDict, "StopRecording")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_OutputGroupInfo(self, oDict:dict, serviceMethodName:str) -> XPWOutputGroup:
        """
        Parses dictionary data for OutputGroupInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWOutputGroup class that represents the dictionary details.
        """
        oItem:XPWOutputGroup = None
        methodKeyName:str = "OutputGroupInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<OutputGroupInfo>
            #  <GroupId>0aca1fc0-7c58-4b39-8629-fbe2a4a760e6</GroupId>
            #  <Name>iPad Outputs</Name>
            #  <Description />
            #  <OutputGroups />
            #  <Outputs>
            #    <guid>3be8e5c6-939a-4a31-bb89-2205e5d54d15</guid>
            #    <guid>7cdddfdd-ace8-491d-b38c-0b00f0cd9a3b</guid>
            #    <guid>8a381bcc-7752-45dd-91f2-3aa8345d37db</guid>
            #  </Outputs>
            #</OutputGroupInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWOutputGroup = XPWOutputGroup()
                self._Parse_GroupInfo(oDict, serviceMethodName, oItem)
                self.ParseCollectionItemStrings(oItem.Outputs, oDict, "Outputs", "guid")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "OutputGroups", "OutputGroupInfo")
                for itemNode in collNodes:
                    oItem.OutputGroups.append(self._Parse_OutputGroupInfo(itemNode, serviceMethodName))

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


    def _Parse_OutputInfo(self, oDict:dict, serviceMethodName:str) -> XPWOutput:
        """
        Parses dictionary data for OutputInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWOutput class that represents the dictionary details.
        """
        oItem:XPWOutput = None
        methodKeyName:str = "OutputInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<OutputInfo>
            #  <RecorderId>EEC28fa5-bDae-a0fD-f033-7D95FadD8CFf</RecorderId>
            #  <HardwareId>fe1CD5B7-F748-CF80-DFF2-7f2D4Bf0e8F7</HardwareId>
            #  <DeviceId>24bBea6e-08e4-Fd1a-9aB6-0373fcA3e3fd</DeviceId>
            #  <Name>string</Name>
            #  <Description>string</Description>
            #  <Shortcut>string</Shortcut>
            #  <DeviceIndex>100</DeviceIndex>
            #  <GisPoint>string</GisPoint>
            #  <ShortName>string</ShortName>
            #  <Icon>100</Icon>
            #  <CoverageDirection>93</CoverageDirection>
            #  <CoverageDepth>23</CoverageDepth>
            #  <CoverageFieldOfView>21</CoverageFieldOfView>
            #  <OutputSecurity />
            #</OutputInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWOutput = XPWOutput()
                self._Parse_DeviceInfo(oDict, serviceMethodName, oItem)
                oItem.CoverageDepth = self.GetDictKeyValueFloat(oDict, "CoverageDepth")
                oItem.CoverageDirection = self.GetDictKeyValueFloat(oDict, "CoverageDirection")
                oItem.CoverageFieldOfView = self.GetDictKeyValueFloat(oDict, "CoverageFieldOfView")

                if (self.DictHasKey(oDict,"OutputSecurity")):
                    self._Parse_OutputSecurityInfo(oDict["OutputSecurity"], serviceMethodName, oItem.OutputSecurity)

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


    def _Parse_OutputSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWOutputSecurity) -> None:
        """
        Parses dictionary data for OutputSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWOutputSecurity):
                An existing XPWOutputSecurity object whose settings will be loaded.
        """
        methodKeyName:str = "OutputSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<OutputSecurity>
            #  <Activate>true</Activate>
            #</OutputSecurity>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.Activate = self.GetDictKeyValueBool(oDict, "Activate")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_PanoramicLensInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWPanoramicLens) -> None:
        """
        Parses dictionary data for PanoramicLensInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWPanoramicLens):
                An existing XPWPanoramicLens object whose settings will be loaded.
        """
        methodKeyName:str = "PanoramicLensInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<PanoramicLensSettings>
            #  <CameraMount i:nil="true"/>
            #  <ImmerVision i:nil="true"/>
            #  <PanoramicLensType i:nil="true"/>
            #</PanoramicLensSettings>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.CameraMount = self.GetDictKeyValueString(oDict, "CameraMount")
                oItem.PanoramicLensEnabled = self.GetDictKeyValueBool(oDict, "PanoramicLensEnabled")
                oItem.PanoramicLensType = self.GetDictKeyValueString(oDict, "PanoramicLensType")

                # process xml result <ImmerVision> node.
                if (self.DictHasKey(oDict,"ImmerVision")):
                    self._Parse_ImmerVisionInfo(oDict["ImmerVision"], serviceMethodName, oItem.ImmerVision)

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_PositionInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWPosition) -> None:
        """
        Parses dictionary data for PositionInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWPosition):
                An existing XPWPosition object whose settings will be loaded.
        """
        methodKeyName:str = "PositionInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<Homeposition>
            #  <Pan>0</Pan>
            #  <Tilt>0</Tilt>
            #  <Zoom>0</Zoom>
            #</Homeposition>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.Pan = self.GetDictKeyValueString(oDict, "Pan")
                oItem.Tilt = self.GetDictKeyValueString(oDict, "Tilt")
                oItem.Zoom = self.GetDictKeyValueString(oDict, "Zoom")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_PresetInfo(self, oDict:dict, serviceMethodName:str) -> XPWPreset:
        """
        Parses dictionary data for PresetInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWPreset class that represents the dictionary details.
        """
        oItem:XPWPreset = None
        methodKeyName:str = "PresetInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<Presets>
            #  <PresetInfo>
            #    <Name>string</Name>
            #    <Position>
            #      <Pan>14</Pan>
            #      <Tilt>8</Tilt>
            #      <Zoom>26</Zoom>
            #    </Position>
            #    <Shortcut>string</Shortcut>
            #    <Id>CFdd6C2f-8D76-c0B6-617D-1D27cF9FBB25</Id>
            #    <Locked>true</Locked>
            #  </PresetInfo>
            #</Presets>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWPreset = XPWPreset()
                oItem.Id = self.GetDictKeyValueString(oDict, "Id")
                oItem.Locked = self.GetDictKeyValueBool(oDict, "Locked")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")
                oItem.Shortcut = self.GetDictKeyValueString(oDict, "Shortcut")

                # process xml result <Position> node.
                if (self.DictHasKey(oDict,"Position")):
                    self._Parse_PositionInfo(oDict["Position"], serviceMethodName, oItem.Position)

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


    def _Parse_ProductInfo(self, oDict:dict, serviceMethodName:str) -> XPWProduct:
        """
        Parses dictionary data for ProductInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "QueryProductInfo", "GetConfiguration", etc.

        Returns:
            An XPWProduct class that represents the dictionary details.
        """
        oItem:XPWProduct = None
        methodKeyName:str = "ProductInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<GetProductInfoResult>
            #  <ProductLine>83a8680e-30b1-46d7-8fd2-cb3d0bf7db9e</ProductLine>
            #  <VendorId>84594050-3c80-465c-a3ab-7c337ce4fd23</VendorId>
            #  <SubProduct>00000000-0000-0000-0000-000000000000</SubProduct>
            #  <MajorVersion>23</MajorVersion>
            #  <MinorVersion>2</MinorVersion>
            #  <ServiceVersion>a</ServiceVersion>
            #  <BuildConfiguration>Release</BuildConfiguration>
            #  <BuildNumber>32</BuildNumber>
            #  <BuildDate>2023-06-02T16:55:24</BuildDate>
            #  <ProductCode>440</ProductCode>
            #  <SLC>M01-C07-232-01-6C4B9A</SLC>
            #</GetProductInfoResult>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWProduct = XPWProduct()
                oItem.BuildConfiguration = self.GetDictKeyValueString(oDict, "BuildConfiguration")
                oItem.BuildDate = self.GetDictKeyValueDateTime(oDict, "BuildDate")
                oItem.BuildNumber = self.GetDictKeyValueString(oDict, "BuildNumber")
                oItem.MajorVersion = self.GetDictKeyValueString(oDict, "MajorVersion")
                oItem.MinorVersion = self.GetDictKeyValueString(oDict, "MinorVersion")
                oItem.ProductLine = self.GetDictKeyValueString(oDict, "ProductLine")
                oItem.ProductCode = self.GetDictKeyValueString(oDict, "ProductCode")
                oItem.ProductName = self.GetDictKeyValueString(oDict, "ProductName")
                oItem.ServiceVersion = self.GetDictKeyValueString(oDict, "ServiceVersion")
                oItem.SoftwareLicenseCode = self.GetDictKeyValueString(oDict, "SLC")
                oItem.SubProduct = self.GetDictKeyValueString(oDict, "SubProduct")
                oItem.VendorId = self.GetDictKeyValueString(oDict, "VendorId")

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


    def _Parse_PtzInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWPtz) -> None:
        """
        Parses dictionary data for PtzInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWPtz):
                An existing XPWPtz object whose settings will be loaded.
        """
        methodKeyName:str = "PtzInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<PtzSettings>
            #  <Capabilities/>
            #  <EditPreset>false</EditPreset>
            #  <IsCenterOnPositionInViewSupported>false</IsCenterOnPositionInViewSupported>
            #  <IsPtzCenterAndZoomToRectangleSupported>false</IsPtzCenterAndZoomToRectangleSupported>
            #  <IsPtzDiagonalSupported>false</IsPtzDiagonalSupported>
            #  <IsPtzHomeSupported>false</IsPtzHomeSupported>
            #  <Presets i:nil="true"/>
            #  <PtzEnabled>false</PtzEnabled>
            #</PtzSettings>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.EditPreset = self.GetDictKeyValueBool(oDict, "EditPreset")
                oItem.IsCenterOnPositionInViewSupported = self.GetDictKeyValueBool(oDict, "IsCenterOnPositionInViewSupported")
                oItem.IsPtzCenterAndZoomToRectangleSupported = self.GetDictKeyValueBool(oDict, "IsPtzCenterAndZoomToRectangleSupported")
                oItem.IsPtzDiagonalSupported = self.GetDictKeyValueBool(oDict, "IsPtzDiagonalSupported")
                oItem.IsPtzHomeSupported = self.GetDictKeyValueBool(oDict, "IsPtzHomeSupported")
                oItem.PtzEnabled = self.GetDictKeyValueBool(oDict, "PtzEnabled")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Capabilities", "CapabilityInfo")
                for itemNode in collNodes:
                    oItem.Capabilities.append(self._Parse_CapabilityInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Presets", "PresetInfo")
                for itemNode in collNodes:
                    oItem.Presets.append(self._Parse_PresetInfo(itemNode, serviceMethodName))

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_PtzSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWPtzSecurity) -> None:
        """
        Parses dictionary data for PtzSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWPtzSecurity):
                An existing XPWPtzSecurity object whose settings will be loaded.
        """
        methodKeyName:str = "PtzSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<PtzSecurity>
            #  <ManualControl>true</ManualControl>
            #  <PresetControl>true</PresetControl>
            #  <ReserveControl>true</ReserveControl>
            #</PtzSecurity>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.ManualControl = self.GetDictKeyValueBool(oDict, "ManualControl")
                oItem.PresetControl = self.GetDictKeyValueBool(oDict, "PresetControl")
                oItem.ReserveControl = self.GetDictKeyValueBool(oDict, "ReserveControl")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_RecorderInfo(self, oDict:dict, serviceMethodName:str) -> XPWRecorder:
        """
        Parses dictionary data for RecorderInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "QueryRecorderInfo", "GetConfiguration", etc.

        Returns:
            An XPWRecorder class that represents the dictionary details.
        """
        oItem:XPWRecorder = None
        methodKeyName:str = "RecorderInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # Note that some XProtect web-service methods only return the base properties of the recording 
            # info object (e.g. Name, Description, etc), and do not return detailed collection information
            # (Cameras, Hardware, Inputs, Outputs, Microphones, etc).

            # SOAP response example:
            #<Cameras i:nil="true"/>
            #<DefaultRecordingTimeSeconds>0</DefaultRecordingTimeSeconds>
            #<Description>XProtect Recording Server WIN10VM.</Description>
            #<Hardware i:nil="true"/>
            #<HostName>WIN10VM</HostName>
            #<Inputs i:nil="true"/>
            #<LastModified>2023-07-28T00:22:21.82Z</LastModified>
            #<MetadataDevices i:nil="true"/>
            #<Microphones i:nil="true"/>
            #<Name>WIN10VM</Name>
            #<Outputs i:nil="true"/>
            #<RecorderId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</RecorderId>
            #<ServiceId>19f94d50-b5ad-4e90-8b3f-9928bb60f9f2</ServiceId>
            #<Speakers i:nil="true"/>
            #<TimeZoneName>Central Standard Time</TimeZoneName>
            #<WebServerUri>http://win10vm:7563/</WebServerUri>
            #<XmlEncoding>utf-8</XmlEncoding>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWRecorder = XPWRecorder()
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")
                oItem.Description = self.GetDictKeyValueString(oDict, "Description")
                oItem.HostName = self.GetDictKeyValueString(oDict, "HostName")
                oItem.LastModified = self.GetDictKeyValueDateTime(oDict, "LastModified")
                oItem.TimeZoneName = self.GetDictKeyValueString(oDict, "TimeZoneName")
                oItem.WebServerUri = self.GetDictKeyValueString(oDict, "WebServerUri")
                oItem.RecorderId = self.GetDictKeyValueString(oDict, "RecorderId")
                oItem.ServiceId = self.GetDictKeyValueString(oDict, "ServiceId")
                oItem.XmlEncoding = self.GetDictKeyValueString(oDict, "XmlEncoding")
                oItem.DefaultRecordingTimeSeconds = self.GetDictKeyValueInt(oDict, "DefaultRecordingTimeSeconds")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Cameras", "CameraInfo")
                for itemNode in collNodes:
                    oItem.Cameras.append(self._Parse_CameraInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Hardware", "HardwareInfo")
                for itemNode in collNodes:
                    oItem.Hardware.append(self._Parse_HardwareInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Inputs", "InputInfo")
                for itemNode in collNodes:
                    oItem.Inputs.append(self._Parse_InputInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "MetadataDevices", "MetadataDeviceInfo")
                for itemNode in collNodes:
                    oItem.MetadataDevices.append(self._Parse_MetadataDeviceInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Microphones", "MicrophoneInfo")
                for itemNode in collNodes:
                    oItem.Microphones.append(self._Parse_MicrophoneInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Outputs", "OutputInfo")
                for itemNode in collNodes:
                    oItem.Outputs.append(self._Parse_OutputInfo(itemNode, serviceMethodName))

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Speakers", "SpeakerInfo")
                for itemNode in collNodes:
                    oItem.Speakers.append(self._Parse_SpeakerInfo(itemNode, serviceMethodName))

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


    def _Parse_RetentionOption(self, oDict:dict, serviceMethodName:str) -> XPWRetentionOption:
        """
        Parses dictionary data for RetentionOption details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWRetentionOption class that represents the dictionary details.
        """
        oItem:XPWRetentionOption = None
        methodKeyName:str = "RetentionOption"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<RetentionOptions>
            #  <RetentionOption>
            #    <RetentionUnits>1</RetentionUnits>
            #    <RetentionOptionType>Days</RetentionOptionType>
            #  </RetentionOption>
            #</RetentionOptions>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWRetentionOption = XPWRetentionOption()
                oItem.RetentionOptionType = self.GetDictKeyValueString(oDict, "RetentionOptionType")
                oItem.RetentionUnits = self.GetDictKeyValueString(oDict, "RetentionUnits")

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


    def _Parse_ServerOption(self, oDict:dict, serviceMethodName:str) -> XPWServerOption:
        """
        Parses dictionary data for ServerOption details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWServerOption class that represents the dictionary details.
        """
        oItem:XPWServerOption = None
        methodKeyName:str = "ServerOption"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<ServerOptions>
            #  <ServerOption>
            #    <Key>Bookmark</Key>
            #    <Value>False</Value>
            #  </ServerOption>
            #</ServerOptions>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWServerOption = XPWServerOption()
                oItem.Key = self.GetDictKeyValueString(oDict, "Key")
                oItem.Value = self.GetDictKeyValueString(oDict, "Value")

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


    def _Parse_SmartClientSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWSmartClientSecurity) -> None:
        """
        Parses dictionary data for SmartClientSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWSmartClientSecurity):
                An existing XPWSmartClientSecurity object whose settings will be loaded.
        """
        methodKeyName:str = "SmartClientSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<SmartClientSecurity>
            #  <SmartClientBrowse>true</SmartClientBrowse>
            #  <SmartClientLive>true</SmartClientLive>
            #  <SmartClientReport>true</SmartClientReport>
            #  <SmartClientSetup>true</SmartClientSetup>
            #</SmartClientSecurity>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.SmartClientBrowse = self.GetDictKeyValueBool(oDict, "SmartClientBrowse")
                oItem.SmartClientLive = self.GetDictKeyValueBool(oDict, "SmartClientLive")
                oItem.SmartClientReport = self.GetDictKeyValueBool(oDict, "SmartClientReport")
                oItem.SmartClientSetup = self.GetDictKeyValueBool(oDict, "SmartClientSetup")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_SpeakerGroupInfo(self, oDict:dict, serviceMethodName:str) -> XPWSpeakerGroup:
        """
        Parses dictionary data for SpeakerGroupInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWSpeakerGroup class that represents the dictionary details.
        """
        oItem:XPWSpeakerGroup = None
        methodKeyName:str = "SpeakerGroupInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<SpeakerGroupInfo>
            #  <GroupId>0aca1fc0-7c58-4b39-8629-fbe2a4a760e6</GroupId>
            #  <Name>iPad Speakers</Name>
            #  <Description />
            #  <SpeakerGroups />
            #  <Speakers>
            #    <guid>3be8e5c6-939a-4a31-bb89-2205e5d54d15</guid>
            #    <guid>7cdddfdd-ace8-491d-b38c-0b00f0cd9a3b</guid>
            #    <guid>8a381bcc-7752-45dd-91f2-3aa8345d37db</guid>
            #  </Speakers>
            #</SpeakerGroupInfo>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWSpeakerGroup = XPWSpeakerGroup()
                self._Parse_GroupInfo(oDict, serviceMethodName, oItem)
                self.ParseCollectionItemStrings(oItem.Speakers, oDict, "Speakers", "guid")

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "SpeakerGroups", "SpeakerGroupInfo")
                for itemNode in collNodes:
                    oItem.SpeakerGroups.append(self._Parse_SpeakerGroupInfo(itemNode, serviceMethodName))

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


    def _Parse_SpeakerInfo(self, oDict:dict, serviceMethodName:str) -> XPWSpeaker:
        """
        Parses dictionary data for SpeakerInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWSpeaker class that represents the dictionary details.
        """
        oItem:XPWSpeaker = None
        methodKeyName:str = "SpeakerInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<Speakers>
            #  <SpeakerInfo>
            #    <RecorderId>CE72ca6B-d198-cCD9-6aDC-1e2fd1Be8519</RecorderId>
            #    <HardwareId>37970B41-adDF-a5bd-9cEA-3e83A4Ac3E5B</HardwareId>
            #    <DeviceId>e0ec4185-0b83-5374-6702-314eC435dc9a</DeviceId>
            #    <Name>string</Name>
            #    <Description>string</Description>
            #    <Shortcut>string</Shortcut>
            #    <DeviceIndex>100</DeviceIndex>
            #    <GisPoint>string</GisPoint>
            #    <ShortName>string</ShortName>
            #    <Icon>100</Icon>
            #    <CoverageDirection>46</CoverageDirection>
            #    <CoverageDepth>6</CoverageDepth>
            #    <CoverageFieldOfView>24</CoverageFieldOfView>
            #    <Tracks/>
            #    <SpeakerSecurity />
            #    <MulticastEnabled>true</MulticastEnabled>
            #    <EdgeStorageSupported>true</EdgeStorageSupported>
            #    <EdgeStoragePlayback>true</EdgeStoragePlayback>
            #    <StopManualRecordingSeconds>100</StopManualRecordingSeconds>
            #  </SpeakerInfo>
            #</Speakers>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWSpeaker = XPWSpeaker()
                self._Parse_DeviceInfo(oDict, serviceMethodName, oItem)
                oItem.CoverageDepth = self.GetDictKeyValueFloat(oDict, "CoverageDepth")
                oItem.CoverageDirection = self.GetDictKeyValueFloat(oDict, "CoverageDirection")
                oItem.CoverageFieldOfView = self.GetDictKeyValueFloat(oDict, "CoverageFieldOfView")
                oItem.EdgeStoragePlayback = self.GetDictKeyValueBool(oDict, "EdgeStoragePlayback")
                oItem.EdgeStorageSupported = self.GetDictKeyValueBool(oDict, "EdgeStorageSupported")
                oItem.MulticastEnabled = self.GetDictKeyValueBool(oDict, "MulticastEnabled")
                oItem.StopManualRecordingSeconds = self.GetDictKeyValueInt(oDict, "StopManualRecordingSeconds")

                if (self.DictHasKey(oDict,"SpeakerSecurity")):
                    self._Parse_SpeakerSecurityInfo(oDict["SpeakerSecurity"], serviceMethodName, oItem.SpeakerSecurity)

                # process xml result collection item node(s).
                collNodes:dict = self.GetDictCollectionItems(oDict, "Tracks", "TrackInfo")
                for itemNode in collNodes:
                    oItem.Tracks.append(self._Parse_TrackInfo(itemNode, serviceMethodName))

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


    def _Parse_SpeakerSecurityInfo(self, oDict:dict, serviceMethodName:str, oItem:XPWSpeakerSecurity) -> None:
        """
        Parses dictionary data for SpeakerSecurityInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.
            oItem (XPWSpeakerSecurity):
                An existing XPWSpeakerSecurity object whose settings will be loaded.
        """
        methodKeyName:str = "SpeakerSecurityInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<SpeakerSecurity>
            #  <Live>true</Live>
            #  <Browse>true</Browse>
            #  <Speak>true</Speak>
            #  <GetSequences>true</GetSequences>
            #  <ExportDatabase>true</ExportDatabase>
            #  <BookmarkView>true</BookmarkView>
            #  <BookmarkAdd>true</BookmarkAdd>
            #  <BookmarkEdit>true</BookmarkEdit>
            #  <BookmarkDelete>true</BookmarkDelete>
            #  <RestrictedMediaView>true</RestrictedMediaView>
            #  <RestrictedMediaCreate>true</RestrictedMediaCreate>
            #  <RestrictedMediaRemove>true</RestrictedMediaRemove>
            #  <RetentionView>true</RetentionView>
            #  <RetentionCreate>true</RetentionCreate>
            #  <RetentionRemove>true</RetentionRemove>
            #  <RetrieveEdgeRecordings>true</RetrieveEdgeRecordings>
            #  <StartRecording>true</StartRecording>
            #  <StopRecording>true</StopRecording>
            #</SpeakerSecurity>


            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem.BookmarkAdd = self.GetDictKeyValueBool(oDict, "BookmarkAdd")
                oItem.BookmarkDelete = self.GetDictKeyValueBool(oDict, "BookmarkDelete")
                oItem.BookmarkEdit = self.GetDictKeyValueBool(oDict, "BookmarkEdit")
                oItem.BookmarkView = self.GetDictKeyValueBool(oDict, "BookmarkView")
                oItem.Browse = self.GetDictKeyValueBool(oDict, "Browse")
                oItem.ExportDatabase = self.GetDictKeyValueBool(oDict, "ExportDatabase")
                oItem.GetSequences = self.GetDictKeyValueBool(oDict, "GetSequences")
                oItem.Live = self.GetDictKeyValueBool(oDict, "Live")
                oItem.RestrictedMediaCreate = self.GetDictKeyValueBool(oDict, "RestrictedMediaCreate")
                oItem.RestrictedMediaRemove = self.GetDictKeyValueBool(oDict, "RestrictedMediaRemove")
                oItem.RestrictedMediaView = self.GetDictKeyValueBool(oDict, "RestrictedMediaView")
                oItem.RetentionCreate = self.GetDictKeyValueBool(oDict, "RetentionCreate")
                oItem.RetentionRemove = self.GetDictKeyValueBool(oDict, "RetentionRemove")
                oItem.RetentionView = self.GetDictKeyValueBool(oDict, "RetentionView")
                oItem.RetrieveEdgeRecordings = self.GetDictKeyValueBool(oDict, "RetrieveEdgeRecordings")
                oItem.Speak = self.GetDictKeyValueBool(oDict, "Speak")
                oItem.StartRecording = self.GetDictKeyValueBool(oDict, "StartRecording")
                oItem.StopRecording = self.GetDictKeyValueBool(oDict, "StopRecording")

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogObject(SILevel.Verbose, MSG_TRACE_RESULT_OBJECT.format(methodKeyName, str(oItem)), oItem, excludeNonPublic=True)

        except Exception as ex:

            # format unhandled exception.
            raise Exception(XPWAppMessages.EXCEPTION_SERVICE_PARSE_RESULTS.format(methodKeyName, str(ex)))

        finally:

            # trace.
            _logsi.LeaveMethod(SILevel.Debug)


    def _Parse_StreamInfo(self, oDict:dict, serviceMethodName:str) -> XPWStream:
        """
        Parses dictionary data for StreamInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWStream class that represents the dictionary details.
        """
        oItem:XPWStream = None
        methodKeyName:str = "StreamInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<Streams>
            #  <StreamInfo>
            #    <StreamId>11171A8D-bC2a-9CDA-76Ef-2d3fB5c5F236</StreamId>
            #    <Name>string</Name>
            #    <Default>true</Default>
            #  </StreamInfo>
            #</Streams>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWStream = XPWStream()
                oItem.Default = self.GetDictKeyValueBool(oDict, "Default")
                oItem.Name = self.GetDictKeyValueString(oDict, "Name")
                oItem.StreamId = self.GetDictKeyValueString(oDict, "StreamId")

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


    def _Parse_SystemEventTypeInfo(self, oDict:dict, serviceMethodName:str) -> XPWSystemEventType:
        """
        Parses dictionary data for SystemEventTypeInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWSystemEventType class that represents the dictionary details.
        """
        oItem:XPWSystemEventType = None
        methodKeyName:str = "SystemEventTypeInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<SystemEventTypes>
            #  <SystemEventTypeInfo>
            #    <EventTypeId>00579724-4652-4eb1-8b61-b38e65d9672a</EventTypeId>
            #    <Name>SmokeAndFireEnd</Name>
            #    <Description />
            #    <EventSource>Device</EventSource>
            #  </SystemEventTypeInfo>
            #</SystemEventTypes>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWSystemEventType = XPWSystemEventType()
                oItem.Description = self.GetDictKeyValueString(oDict, "Description")
                oItem.EventSource = self.GetDictKeyValueString(oDict, "EventSource")
                oItem.EventTypeId = self.GetDictKeyValueString(oDict, "EventTypeId")
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


    def _Parse_TrackInfo(self, oDict:dict, serviceMethodName:str) -> XPWTrack:
        """
        Parses dictionary data for TrackInfo details.

        Args:
            oDict (dict):
                Dictionary that was constructed by calling xmltodict with a XProtect 
                web-service xml response.
            serviceMethodName (str):
                Name of the XProtect web-service method that was called.  
                Example: "GetConfiguration", etc.

        Returns:
            An XPWTrack class that represents the dictionary details.
        """
        oItem:XPWTrack = None
        methodKeyName:str = "TrackInfo"

        try:

            # trace.
            _logsi.EnterMethod(SILevel.Debug)

            # SOAP response example:
            #<Tracks>
            #  <TrackInfo>
            #    <Edge>true</Edge>
            #    <TrackId>447476b1-97f7-4a9d-8c77-33808e7eadf3</TrackId>
            #  </TrackInfo>
            #  <TrackInfo>
            #    <Edge>false</Edge>
            #    <TrackId>71cab37e-8718-4383-8e86-146b38168e42</TrackId>
            #  </TrackInfo>
            #</Tracks>

            # were any results returned?
            if (oDict != None):

                # trace.
                if (_logsi.IsOn(SILevel.Verbose)):
                    _logsi.LogText(SILevel.Verbose, MSG_TRACE_PROCESSING_DICTIONARY.format(methodKeyName), json.dumps(oDict, indent=2))

                # parse base properties.
                oItem:XPWTrack = XPWTrack()
                oItem.Edge = self.GetDictKeyValueBool(oDict, "Edge")
                oItem.TrackId = self.GetDictKeyValueString(oDict, "TrackId")

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
