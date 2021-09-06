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



author: **Tooraj Jahangiri** version: **0.1**