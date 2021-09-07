# MY PASSWORD MANAGER APPLICATION

**APP VERSION : 0.1**

Handy & Usefully CLI application For My Password Manager & Other Functionality 

---

### ALL  APPLICATION  IN  THIS  APP

> **1 : PASSWORD MANAGER**
>
> **2 : KEY GENERATOR**
>
> **3 : TEXT CIPHER**
>
> **4 : TEXT CRYPTO**
>
> **5 : UPDATE DATABASE ACCOUNT**
>
> **6 : SETTING FOR PASSWORD MANAGER**

---

### FAST  START

After Run Application You Can Set The Created Setting For Life Easier

```bash
MY PASSWORD MANAGER APPLICATION [VERSION 0.1]

SET YOUR SETTING PATH
        IF NOT SETTING FILE PRESS [ENTER] FOR SKIP

SETTING PATH />
```

Set Setting Path if you Have Setting Other Wise Press **ENTER** for Skip.

If U Set Setting U must Set **Key** & **Method**. [The Method Is Always Needed But Key Is Optional]

```bash
SETTING PATH /> ./stting.json
SECURE DATA IN SETTING IF NOT SECURED PRESS [ENTER] FOR SKIP [SETTING KEY]
SETTING KEY /> ******
SETTING METHOD /> [default : mb64] lmb64
```

Next U see The Menu Chose **Number** For Run Application.

```bash
MY PASSWORD MANAGER APPLICATION [VERSION 0.1]

        1  : PASSWORD MANAGER.
        2  : KEY GENERATOR.
        3  : TEXT CIPHER.
        4  : TEXT CRYPTO.
        5  : UPDATE ACCOUNT DATABASE.
        6  : CREATE OR UPDATE SETTING PASSWORD MANAGER.
        0  : EXIT.
        -1 : CLear Display. U can Use 'cls' or 'clear'.

-- />
```

If Setting is Set And U Want Run **Password Manager** Question For **Name** Set The Data Base Name In Setting for Load Data From Setting And Send To Password Manager . The Other Wise U Must Set The Data Base Data After Running **Password Manager App**.

```bash
MY PASSWORD MANAGER APPLICATION [VERSION 0.1]

        1  : PASSWORD MANAGER.
        2  : KEY GENERATOR.
        3  : TEXT CIPHER.
        4  : TEXT CRYPTO.
        5  : UPDATE ACCOUNT DATABASE.
        6  : CREATE OR UPDATE SETTING PASSWORD MANAGER.
        0  : EXIT.
        -1 : CLear Display. U can Use 'cls' or 'clear'.

-- /> 1
... PASSWORD MANAGER ...
TYPE SETTING NAME IF DATABASE ADDED IN SETTING
SETTING NAME /> mydb
```

After This Run **Password Manager** & **Connected** To Chosen Data Base.

```bash
PASSWORD MANAGER APP [VERSION 0.1]

        < DATA BASE [my_data_base_0.mps] IS ACTIVE >
        ------------------------------------------------------

        1 : 'ADD' Password.
                add Password into The DataBase.
        2 : 'GET' Password.
                get Data From Data Base.
        3 : 'ALL NAME' Password.
                get All Name Existed into Data Base.
        4 : 'UPDATE' Password.
                update or replace Data.
        5 : 'EXISTS' Password.
                exists data into Data Base.
        6 : 'COUNT' Password.
                count Password into Data Base.
        7 : 'DELETE' Password.
                delete Password From data Base.
        8 : 'RESET' Data Base.
                reset DATA BASE *REMOVE ALL PASSWORD or *DELETE DATA BASE.
        0 : 'EXIT'
                Quit Application.
        -1 : 'CLEAR' Console Screen
                Clear Display U can Use 'cls' or 'clear'.
-- />
```

Now Run Again The **My Password Manager App** And **Skipped** Setting Path

```bash
MY PASSWORD MANAGER APPLICATION [VERSION 0.1]

        1  : PASSWORD MANAGER.
        2  : KEY GENERATOR.
        3  : TEXT CIPHER.
        4  : TEXT CRYPTO.
        5  : UPDATE ACCOUNT DATABASE.
        6  : CREATE OR UPDATE SETTING PASSWORD MANAGER.
        0  : EXIT.
        -1 : CLear Display. U can Use 'cls' or 'clear'.

-- />
```

Now for Run **Password Manager** Must Type **Number [1]**

```
PASSWORD MANAGER APP [VERSION 0.1]
... CONNECT TO DATABASE ...
PATH />
```

We Need **Connect** App To **Data Base** If Data Base Not Existed App is **Created** Data Base. Type **Data Base Path**

```bash
PASSWORD MANAGER APP [VERSION 0.1]
... CONNECT TO DATABASE ...
PATH /> ./my_database.mps
METHOD />
```

Now Chose Data Base **Cipher Method** Cipher Method use **nested_cipher** library and Based on URL SAFE BASE64

*All Support Method :* **b64 - ab64 - mb64 - eb64 - lb64 - rb64 - rab64 - rmb64 - reb64 - rlb64**

Next Must Type **User Name** and **Password**

```bash
PASSWORD MANAGER APP [VERSION 0.1]
... CONNECT TO DATABASE ...
PATH /> ./test/tdb/my_database.mps
METHOD /> mb64
USERNAME /> my_username
PASSWORD /> MyPassword
```

After This If Everything is Ok App Connected To Data Base 

```bash
PASSWORD MANAGER APP [VERSION 0.1]
        < DATA BASE [my_database.mps] IS ACTIVE >
        ------------------------------------------------------

        1 : 'ADD' Password.
                add Password into The DataBase.
        2 : 'GET' Password.
                get Data From Data Base.
        3 : 'ALL NAME' Password.
                get All Name Existed into Data Base.
        4 : 'UPDATE' Password.
                update or replace Data.
        5 : 'EXISTS' Password.
                exists data into Data Base.
        6 : 'COUNT' Password.
                count Password into Data Base.
        7 : 'DELETE' Password.
                delete Password From data Base.
        8 : 'RESET' Data Base.
                reset DATA BASE *REMOVE ALL PASSWORD or *DELETE DATA BASE.
        0 : 'EXIT'
                Quit Application.
        -1 : 'CLEAR' Console Screen
                Clear Display U can Use 'cls' or 'clear'.
-- />
```

Thank You Dear

---

### KEY GENERATOR

Simple Key Generator

```bash
KEY GENERATOR [VERSION 0.1]

        1  : GENERATE KEY
        2  : SET LENGTH [DEFAULT : 32]
        3  : SET CHARACTERS [DEFAULT : ASCII 32/126]
        4  : SET SKIP CHARACTERS
        5  : SET COUNT MAKE [DEFAULT : 1]
        6  : SET PATH FOR SAVE RESULTS
        0  : EXIT
        -1 : Clear Display. U can Use "cls" or "clear"

-- />
```

**Option Key Generator**

> **KEY LENGTH**   NUMBER   **[ 2 ]**
>
> > Default Length is **32**
>
> **VALID CHARACTER**  NUMBER  **[ 3 ]**
>
> > Default Character is **ASCII - 32 / 126** 
>
> **SKIP CHARACTER**  NUMBER  **[ 4 ]**
>
> **MAKING KEY COUNTER**  NUMBER **[ 5 ]**
>
> > Default Counter Making Key is  **1**
>
> **SET PATH FOR SAVING RESULT**  NUMBER **[ 6 ]**
>
> > Default File Result is **Result Show in Console**

After Setup Your Setting Use **[ 1 ]** For Generate Key Is Start

---

### TEXT CIPHER

Simple Cipher Text This App Supports Encrypt / Decrypt Method - Based on **nested_cipher**

```bash
CIPHER APP [VERSION 0.1]

        1  : SETUP CIPHER.
        2  : INPUT TEXT ENCODE / DECODE.
        3  : FILE TEXT ENCODE / DECODE.
        4  : INPUT TEXT ONLY NESTED CIPHER ENCODE / DECODE.
        5  : FILE TEXT ONLY NESTED CIPHER ENCODE / DECODE.
        6  : SET FILE FOR SAVE RESULT.
        7  : UPDATE CIPHER.
        8  : GENERATE KEY.
        0  : Exit.
        -1 : CLear Display. U can Use 'cls' or 'clear'.

-- />
```

First Must Setup Cipher For Active Cipher Use **[ 1 ]** for setup Cipher

```bash

-- /> 1
SETUP CIPHER
SETUP NEW CIPHER
KEY /> [default : 'NONE']
```

For Encrypt or Decrypt Use Key Other Wise Press **ENTER** for Skip & Continue

```bash

-- /> 1
SETUP CIPHER
SETUP NEW CIPHER
KEY /> [default : 'NONE']
METHOD /> [default : 'NONE']
```

Chose **nested_cipher** Method other wise Press **ENTER** for skip this & Set Method **rmb64**

> **All Method Supports**
>
> > **b64 - ab64 - mb64 - eb64 - lb64 - rb64 - rab64 - rmb64 - reb64 - rlb64**

```bas

-- /> 1
SETUP CIPHER
SETUP NEW CIPHER
KEY /> [default : 'NONE']
METHOD /> [default : 'NONE']
CIPHER KEY /> ['0' or '1']~[default : '0']
```

Set Cipher Key  **"0"** means **False** and **"1"** means **True**

if **1** means Your **Key** Cipher With Before Use and Other Wise **Key** is **Raw Key**

```bash

-- /> 1
SETUP CIPHER
SETUP NEW CIPHER
KEY /> [default : 'NONE']
METHOD /> [default : 'NONE']
CIPHER KEY /> ['0' or '1']~[default : '0']
NEW CIPHER IS ACTIVE
-- />
```

Now Cipher Setup Is Done And Cipher Active For Work Chose Order For **ENCODE / DECODE** Your Text or Text File

---

### TEXT CRYPTO

Simple Encrypt or Decrypt Text Encoding **UTF8**

```bash
CRYPTO APP [VERSION 0.1]

        1  : INPUT TEXT ENCRYPTING OR DECRYPTING.
        2  : FILE TEXT ENCRYPTING OR DECRYPTING.
        3  : SET KEY.
        4  : SET PATH FOR SAVE RESULT.
        0  : EXIT.
        -1 : CLear Display. U can Use 'cls' or 'clear'.

-- />
```

for Set Key Use **3** Other Wise Every Time U Want To Encrypt or Decrypt Must Type Key

---

### UPDATE ACCOUNT DATABASE

For Change User Name & Password & Method Set in Data Base Use This App

*Attention This App Can not Change Setting Data For Change Setting Data Must Update Setting Manually* 

```bash
UPDATE ACCOUNT DATA BASE APP [VERSION 0.1]

        1  : UPDATE ACCOUNT.
        2  : RESET.
        0  : EXIT.
        -1 : CLear Display. U can Use 'cls' or 'clear'.

-- />
```

Type **1** For Update Data Base Account

```bash

-- /> 1
UPDATE ACCOUNT
SET DATA BASE PATH AND ACCOUNT DATA
DATA BASE [PATH] />
```

Set Data Base File Path

```bash
-- /> 1
UPDATE ACCOUNT
SET DATA BASE PATH AND ACCOUNT DATA
DATA BASE [PATH] /> ./my_db.mps
DATA BASE [USER NAME] /> my_username
DATA BASE [PASSWORD] /> MyPassword
DATA BASE [CIPHER METHOD] /> mb64
```

Set User Name & Password & Method For Connect To Data Base

```bash
SETTED DATA BASE FILE AND ACCOUNT DATA
SET NEW ACCOUNT DATA
ONLY 'PASSWORD' MUST BE CHANGED 'USER NAME' AND 'METHOD' IS OPTIONAL FO CHANGE
NEW USER NAME /> [default 'my_username']
```

Now Must Set **New** Data Only **Password** Must Be Change Other **User Name & Method** Optional For Update

```bash
SETTED DATA BASE FILE AND ACCOUNT DATA
SET NEW ACCOUNT DATA
ONLY 'PASSWORD' MUST BE CHANGED 'USER NAME' AND 'METHOD' IS OPTIONAL FO CHANGE
NEW USER NAME /> [default 'my_username']
NEW PASSWORD /> NewPassword
NEW METHOD /> [default 'mb64']
```

After Set Your New Data Question If Ready Type **Y - y** for Update Account Is Start

```bash
DATA BASE NEW ACCOUNT IS SETTED
ARE U READY /> [default : 'N'] y
```

  Wait For Update Account Is Done

---

### CREATE OR UPDATE SETTING PASSWORD MANAGER

Frist Set Setting Path if File Not Exist App Created The File

```bash
SETTING APP [VERSION 0.1]
SETTING PATH />
```

Then If Want To Secure Data Type Key and Method

```bash
SETTING APP [VERSION 0.1]
SETTING PATH /> ./test/tdb/setting.sjson
SETTING KEY /> [default : No Secure] mykey
SETTING METHOD /> [default : mb64] 
```

Now Connect The Setting Add New Data For Created Setting And Put Data Into The Setting

```bash
SETTING APP [VERSION 0.1]

        1  : ADD OR UPDATE TO SETTING.
        2  : GET FROM SETTING.
        3  : CONNECT TO OTHER SETTING.
        4  : RESET SETTING. [CLEAR SETTING FILE]
        0  : EXIT.
        -1 : CLear Display. U can Use 'cls' or 'clear'.

-- />
```

Add or Update

```bash

-- /> 1
ADD DATA TO SETTING
NAME />
```

Type This Data Name

```bash

-- /> 1
ADD DATA TO SETTING
NAME /> db_data
DB FILE PATH /> ./my_database.mps
METHOD SECURE DB /> mb64
DB USER NAME /> my_username
DB PASSWORD /> MyPassword
```

After Type Name Type Other Data Base Data **Path - Cipher Method - User Name - Password**

```bash

-- /> 1
ADD DATA TO SETTING
NAME /> db_data
DB FILE PATH /> ./test/tdb/mdb.mps
METHOD SECURE DB /> mb64
DB USER NAME /> my_username
DB PASSWORD /> MyPassword
DATA [db_data] ADDED TO SETTING
```

 Data Added To Setting Now You Can Use This Setting For Life Easier Use My Password Application

---

Tank You 

---

author: **Tooraj Jahangiri** version: **0.1**