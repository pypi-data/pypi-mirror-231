"""
Module: xpwconst.py

<details>
  <summary>Revision History</summary>

| Date       | Version     | Description
| ---------- | ----------- | ----------------------
| 2023/07/11 | 1.0.0.0     | Initial Version.  
| 2023/08/15 | 1.0.1.0     | Miscellaneous documentation and sample code updates.
| 2023/09/22 | 1.0.2.0     | Test case scenario updates.

</details>
"""

# our package imports.
# none.

# constants are placed in this file if they are used across multiple files.
# the only exception to this is for the VERSION constant, which is placed here for convenience.

VERSION:str = "1.0.2"
""" 
Current version of the Milestone XProtect WS Python3 Library. 
"""

PACKAGENAME:str = "milestonexprotectwspython"
"""
Name of our package (used by PDoc Documentation build).
"""

# properties used in PDOC documentation build.

PDOC_BRAND_ICON_URL:str = "https://www.milestonesys.com/video-technology/platform/xprotect/"
"""
PDoc Documentation brand icon link url that is displayed in the help document TOC.
Value = "https://www.milestonesys.com/video-technology/platform/xprotect/"
"""

PDOC_BRAND_ICON_URL_SRC:str = "milestonexprotect.ico"
"""
PDoc Documentation brand icon link url that is displayed in the help document TOC.
Value = "milestonexprotect.ico"
"""

PDOC_BRAND_ICON_URL_TITLE:str = "A XProtect Client"
"""
PDoc Documentation brand icon link title that is displayed in the help document TOC.
Value = "A XProtect Client"
"""

# Miscellaneous constants:

UNKNOWN_VALUE:str = "<unknown>"
"""
Indicates if an event argument value is unknown for event argument objects that are displayed as a string.

Value: 
    `"<unknown>"`
"""

# Application trace messages.

MSG_TRACE_METHOD_REQUEST:str = "{0} Web-Service request"
"""
{0} Web-Service request
"""

MSG_TRACE_METHOD_REQUEST_HEADERS:str = "{0} Web-Service request headers"
"""
{0} Web-Service request headers
"""

MSG_TRACE_METHOD_REQUEST_BODY:str = "{0} Web-Service request body"
"""
{0} Web-Service request body 
"""

MSG_TRACE_METHOD_RESPONSE:str = "{0} Web-Service response"
"""
{0} Web-Service response
"""

MSG_TRACE_METHOD_RESPONSE_BODY:str = "{0} Web-Service response body"
"""
{0} Web-Service response body
"""

MSG_TRACE_METHOD_RESPONSE_DICTIONARY:str = "{0} Web-Service response dictionary for \"{1}\" node"
"""
{0} Web-Service response dictionary for \"{1}\" node
"""

MSG_TRACE_PROCESSING_DICTIONARY:str = "Processing \"{0}\" node dictionary"
"""
Processing \"{0}\" node dictionary
"""

MSG_TRACE_RESULT_OBJECT:str = "{0} object created: {1}"
"""
{0} object created: {1}
"""
