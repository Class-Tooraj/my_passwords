# MY PASSWORDS

#### Simple Password Manager Use Sqlite3 Data Base .

My Passwords is Password Manager Powered By Python 3 and Sqlite3

Data is Encrypted and Secured With Nested Cipher Based on Base64 URL Safe

---

### Arguments

> **Positional Input :**
>
> > **Username**
> >
> > **Password**    minimum length **6** 
> >
> > **Command**
> >
> > > **add**  add new password [new row add to database] - bool
> > >
> > > **get**  get password from database - string
> > >
> > > **up**   update existed password data - bool
> > >
> > > **del**  delete password from database - bool
> > >
> > > **exists** this password existed into database - bool
> > >
> > > **count**  how many password saved in database - integer
> > >
> > > **reset**  clear all password and password table is empty - bool
> > >
> > > **removeall** clear database and delete database file
>
> **Options :**
>
> > **(--name, -n)**  password name - Required is True
> >
> > **(--password, -p)** password - If *add* command Required is True
> >
> > **(--url, -u)**  password url or account or other - Required is False
> >
> > **(--more, -m)**  more information - Required is False
> >
> > **(--return, -r)** return for *get* command - *default* 'password'
> >
> > > (all, id, name, password, url, more, settime, lastupdate)
> > >
> > > **customize return example** *name,password,lastupdate* 
> >
> > **(--database, -db)**  database file - *default* './data/db.mp'
> >
> > **(--cipher_method, -cm)**  nested cipher method available - *default* 'rmb64'
> >
> > > (b64,ab64,mb64,eb64,lb64,rb64,rab64,rmb64,reb64,rlb64) 
> > >
> > > [more info]: https://pypi.org/project/nested-cipher/#description	"nested_cipher"

---

author: **Tooraj Jahangiri** version: **0.1**
