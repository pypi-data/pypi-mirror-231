__update__ = '2023.08.16'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

'''
NOTES:
TASK:
WARNINGS:
'''

''' SYSTEM LIBRARIES '''
import os, datetime, platform, time
import hashlib
import urllib.request # INTERNET CONNECTION
import pyperclip as clipboard # Portapapeles
from inspect import getmembers, isfunction, isclass # OBJECTS CHECK
# from importlib import import_module


''' FUNCTIONS
--------------------------------------------------------
'''

## OPERATING SYSTEM

def GET_FIRM() -> str:
    '''
    Returns string with OS Login Id and Date in format ' yyyy-mm-dd / hh:mm '
    '''
    FIRM = "{} [{}]".format(os.getlogin(), datetime.datetime.now().strftime("%Y-%m-%d / %H:%M"))
    return FIRM

def OS_GET_SYSTEM() -> str:
    '''
    Returns the system OS name 
    '''
    os = platform.system()
    return os

def OS_GET_LOGIN() -> str:
    '''
    Get User SO Log-In Id in str format
    '''
    value = os.getlogin()
    return value

def COPY2CLIPBOARD(TEXT) -> None:
    '''
    Add selected data to clipboard
    '''
    clipboard.copy(TEXT)

def INTERNET_CONNECTION_CHECK(URL=r'https://cloud.seatable.cn/') -> bool:
    '''
    Returns bool value if run the selected URL connection
    Info: Some generics URL not run as well
    '''
    # https://cloud.seatable.cn/
    # https://www.rohde-schwarz.com/

    try:
        urllib.request.urlopen(
            URL,
            timeout=5
            )
        return True
    except:
        return False



## PATH FUNCTIONS

def PATH_OPEN(PATH) -> None:
    ''' 
    Run from OS selected PATH
    '''
    os.startfile(PATH)

def PATH_FOLDER_NEW(PATH=str, FOLDER_NAME=str) -> None:
    '''
    Create a new folder in selected path
    '''
    NEW_FOLDER = os.path.join(PATH,FOLDER_NAME)
    os.mkdir(NEW_FOLDER)

def PATH_GET_DESKTOP() -> str:
    '''
    Returns Desktop Path in str format
    
    INCOMPLETE: 
    - Hay que añadir mas sistemas operativos
    '''
    SO = OS_GET_SYSTEM()
    if SO == 'Windows': 
        PATH = "C:/Users/" + os.getlogin() + "/Desktop/"
    return PATH

def PATH_EXIST_CHECK(PATH=str) -> bool:
    '''
    Check if selected path or file exist 
    '''
    check = os.path.exists(PATH)
    return check



## DATE FUNCTIONS

def DATE_GET_TODAY():
    '''
    Returns Date in str format like ' yyyy-mm-dd '
    '''
    DATE = datetime.datetime.now().strftime('%Y-%m-%d')
    return DATE

def DATE_GET_NOW(format=r'%Y-%m-%d / %H:%M'):
    '''
    Returns Date Time in str (default) format like 'yyyy-mm-dd / hh:mm'
    '''
    DATE = str(datetime.datetime.now().strftime(format))
    return DATE

def DATE_ISO(DATE) -> str:
    '''
    Convert date to ISO Format 'yyyy-mm-dd'
    '''
    iso_date = "{}-{}-{:02d}".format(DATE.year(), DATE.month(), DATE.day())
    return iso_date



## LICENSE FUNCTIONS

def ENCODE_STR(STR: str) -> str:
    code = hashlib.sha256(str(STR).encode('utf-8')).hexdigest()
    return code

def LICENSE_TXT(file, appName: str, loginId: str, limitOpens: int, limitDate: int):
    '''
    Make a LICENSE FILE with the next atributes:
    - file (str) / Address and name of the file
    - appName (str) / Name of the Application
    - loginId (str) / Id of the OS User
    - limitOpens (int) / Maximun Opens
    - limitDate (int) / Maximun Date example: 20230601
    
    INCOMPLETE:
        - Hay que añadir la fecha de creación
    '''
    ## INIT FILE
    with open(file, 'w') as f:
        f.write('')
    ## ENCODE
    app = f"@{appName}"
    app = hashlib.sha256(app.encode('utf-8')).hexdigest()
    login = f"@{loginId}"
    login = hashlib.sha256(login.encode('utf-8')).hexdigest()
    opens = f"@{limitOpens}"
    opens = hashlib.sha256(opens.encode('utf-8')).hexdigest()
    date = f"@{limitDate}"
    date = hashlib.sha256(date.encode('utf-8')).hexdigest()
    ## CREATION TIME FILE
    createTime = os.path.getctime(file)
    createTime = time.ctime(createTime)
    createTime = f"@{createTime}"
    createTime = hashlib.sha256(createTime.encode('utf-8')).hexdigest()
    ## MODIFICATION TIME FILE
    modTime = os.path.getmtime(file)
    modTime = time.ctime(modTime)
    modTime = f"@{modTime}"
    modTime = hashlib.sha256(modTime.encode('utf-8')).hexdigest()
    ## EDIT FILE
    txtList = [app, login, opens, date, createTime, modTime]
    with open(file, 'w') as f:
        f.write('\n'.join(txtList))

def LICENSE_TXT_DATA(file) -> dict:
    '''
    Get data in the file

    INCOMPLETE:
    - Esta funcion se usa una vez dentro de la APP poder obtener los valores de la licencia
    - Hay que integrar esta funcion dentro de LICENSE_TXT_CHECK
    '''
    data = {
        'login': "FAIL",
        'opens': 0,
        'date': 0,
        }
    
    ## OPEN FILE
    if os.path.exists(file):
        with open(file, 'r') as f:
            txt = f.readlines()
    else:
        return data
    ## LOGIN
    login = f"@{OS_GET_LOGIN()}"
    login = hashlib.sha256(login.encode('utf-8')).hexdigest()
    if login == txt[1].replace(chr(10), ""): 
        data['login'] = "PASS"
    ## OPENS
    opens = 0
    for i in range(0, 2000):
        hash = f"@{i}"
        hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
        if hash == txt[2].replace(chr(10), ""):
            opens = i
            # print("limitOpens: PASS", opens)
            data['opens'] = opens
            break
        if i == 1999:
            # print("ERROR / limitOpens")
            data['opens'] = 0
            # return False
    ## DATE
    date = 0
    for i in range(20230101, 20250101):
        hash = f"@{i}"
        hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
        if hash == txt[3].replace(chr(10), ""):
            date = i
            # print("limitDate: PASS", date)
            data['date'] = date
            break
    return data

def LICENSE_TXT_CHECK(file, appName: str) -> bool:
    '''
    appName, loginId, limitOpens, limitDate, modTime

    INCOMPLETE:
        - Si no encuentra el fichero devuelve False
    '''

    ## OPEN FILE
    if os.path.exists(file) == False:
        return False
    
    with open(file, 'r') as f:
        txt = f.readlines()

    ## CHECK
    if len(txt) == 6:
        # 
        app = f"@{appName}"
        app = hashlib.sha256(app.encode('utf-8')).hexdigest()
        if app == txt[0].replace(chr(10), ""): print("appName: PASS")
        else:
            # print("ERROR / appName")
            return False
        # 
        login = f"@{os.getlogin()}"
        login = hashlib.sha256(login.encode('utf-8')).hexdigest()
        if login == txt[1].replace(chr(10), ""): print("loginId: PASS")
        else:
            # print("ERROR / loginId")
            return False
        # 
        opens = None
        for i in range(0, 2000):
            hash = f"@{i}"
            hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
            if hash == txt[2].replace(chr(10), ""):
                opens = i
                print("limitOpens: PASS", opens)
                break
            if i == 1999:
                # print("ERROR / limitOpens")
                return False
        # 
        for i in range(20230101, 20250101):
            hash = f"@{i}"
            hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
            if hash == txt[3].replace(chr(10), ""):
                date = i
                # print("limitDate: PASS", date)
                break
            if i == 20250100:
                # print("ERROR / limitDate")
                return False
        # 
        createTime = os.path.getctime(file)
        createTime = time.ctime(createTime)
        createTime = f"@{createTime}"
        createTime = hashlib.sha256(createTime.encode('utf-8')).hexdigest()
        if createTime == txt[4].replace(chr(10), ""): print("createTime: PASS")
        else:
            # print("ERROR / createTime")
            return False
        # 
        modTime = os.path.getmtime(file)
        modTime = time.ctime(modTime)
        modTime = f"@{modTime}"
        modTime = hashlib.sha256(modTime.encode('utf-8')).hexdigest()
        if modTime == txt[5].replace(chr(10), ""): print("modTime: PASS")
        else:
            # print("ERROR / modTime")
            return False
        
        ## EDIT FILE
        opens -= 1
        opens = f"@{opens}"
        opens = hashlib.sha256(opens.encode('utf-8')).hexdigest()
        # 
        with open(file, 'w') as f:
            f.write('')
        now = os.path.getmtime(file)
        now = time.ctime(now)
        now = f"@{now}"
        now = hashlib.sha256(now.encode('utf-8')).hexdigest()
        with open(file, 'w') as f:
            f.write('\n'.join(
                [txt[0].replace(chr(10), ""), 
                txt[1].replace(chr(10), ""), 
                opens, 
                txt[3].replace(chr(10), ""), 
                createTime, 
                now
                ]))
        # 
        return True
    # 
    else: 
        return False



## IMAGES FUNCTIONS

def IMG_PIXEL2CM(PIXELS=float) -> float:
    '''
    Convert from pixels value to centimeters value
    '''
    value = PIXELS * 0.0264583333
    return value

def IMG_CM2PIXEL(CM=float) -> float:
    '''
    Convert from centimeters value to pixels value 
    '''
    value = CM * 37.795275591
    return value



## MISCELLANEOUS FUNCTIONS

def OBJECT_CHECK(OBJECT, objectType: str = 'function', onlyNames: bool = False) -> list:
    '''
    - OBJECT: Library from importlib
    - objectType: 'function' (for function objects) / 'class' (for class objects)
    - onlyNames:
        - True (Return a List with al the selected objects in the library)
        - False (Return a List with a tuple with object name and the object)
    
    INCOMPLETE:
    - Cuando el objeto es creado desde importlib no se pasa path
    - No he comprobado si puedes pasar un path, directamente un import, etc.
    '''
    if objectType != 'function' and objectType != 'class':
        print("OBJECT_CHECK ERROR / objectType not supported")
        return []
    if objectType == 'function':
        LIST = getmembers(OBJECT, isfunction)
    if objectType == 'class':
        LIST = getmembers(OBJECT, isclass)
    if onlyNames:
        LIST = [func[0] for func in LIST]
    return LIST

def INT_TWODIGITS(INT=int) -> str:
    '''
    Convert Integer to tow digit string
    1 --> 01
    '''
    ORDR = '{:02d}'.format(INT)
    return ORDR



''' TEST
--------------------------------------------------------
'''

def OPEN_DIRECTORY(PATH=str) -> None:
    '''
    INCOMPLETE:
    - Se usa la funcion 'system' para lanzar un comando en consola
    - Para lo que se pensó esta funcióin es mejor usar PATH_OPEN()
    '''
    path = os.path.realpath(PATH)
    os.system(f'start {path}')

