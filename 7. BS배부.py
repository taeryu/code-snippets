import win32com.client
from SAPvariables import *

#BS배부 테스트완료
def SAP_BS():

    excelPath = r'#'
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    if not type(SapGuiAuto) == win32com.client.CDispatch:
        return

    application = SapGuiAuto.GetScriptingEngine
    if not type(application) == win32com.client.CDispatch:
        SapGuiAuto = None
        return

    connection = application.Children(0)
    if not type(connection) == win32com.client.CDispatch:
        application = None
        SapGuiAuto = None
        return

    session = connection.Children(0)
    if not type(session) == win32com.client.CDispatch:
        connection = None
        application = None
        SapGuiAuto = None
        return

    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/tbar[0]/okcd").text = "/NFAGLGA15"
    session.findById("wnd[0]").sendVKey (0)
    session.findById("wnd[0]/usr/chkRKGA2U-TEST").selected = False
    session.findById("wnd[0]/usr/ctxtRKGA2-RLDNR").text = "0L"
    session.findById("wnd[0]/usr/txtRKGA2U-FROM").text = thisMonth
    session.findById("wnd[0]/usr/txtRKGA2U-TO").text = thisMonth
    session.findById("wnd[0]/usr/txtRKGA2U-GJAHR").text = thisYear
    session.findById("wnd[0]/usr/ctxtRKGA2U-DOCTY").text = "sx"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[0,0]").text = "903AAA"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[1,0]").text = "903AA2"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[2,0]").text = "903AA3"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[3,0]").text = "903AA4"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[4,0]").text = "903AA6"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[5,0]").text = "903AA7"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[6,0]").text = "903BB1"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[7,0]").text = "903BB2"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[8,0]").text = "903BB3"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[9,0]").text = "903BB4"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[10,0]").text = "903BB5"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[11,0]").text = "903BB6"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[12,0]").text = "903BB7"
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[12,0]").setFocus()
    session.findById("wnd[0]/usr/sub:SAPMKGA2:0102/ctxtRKGA2-GLCYC[12,0]").caretPosition = "6"
    session.findById("wnd[0]").sendVKey (0)
    session.findById("wnd[0]/tbar[1]/btn[8]").press()

SAP_BS()