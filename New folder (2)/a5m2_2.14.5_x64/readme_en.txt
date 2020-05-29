-------------------------------------------------------------------
Software   : A5:SQL Mk-2 Version 2.14.4
Author     : masakazu matsubara
Target OS  : Windows XP
             Windows Vista
             Windows 7
             Windows 8
             Windows 8.1
             Windows 10
             Windows Server 2003
             Windows Server 2008
             Windows Server 2012 (GUI)

             ** x86 version can not connect to 64bit OLE DB, ODBC.
             ** x64 version does not work on 32 bit OS.
             ** x64 version can not be connected to 32 bit OLE DB, ODBC.

Website   : https://a5m2.mmatsubara.com/
File      : x86 edition : a5m2_2.14.4_x86.zip
            x64 edition : a5m2_2.14.4_x64.zip
            x86 edition(Read-only edition) : a5m2_2.14.4_x86_r.zip
            x64 edition(Read-only edition) : a5m2_2.14.4_x64_r.zip
            Microsoft Store x64 edition：A5M2.x64.appx 
-------------------------------------------------------------------

[OUTLINE]
  A5:SQL Mk-2 is a free SQL development environment & ER diagram development 
  tool developed to support database development that is complicated.

  It is developed with the goal of being highly functional and lightweight and 
  easy to understand its usage.

  In addition to executing SQL and editing tables, it has various functions 
  such as obtaining SQL execution plans and creating ER diagrams.


[FILE CONTENTS]
  The archive file contains the following files.
    A5M2.exe                          A5:SQL Mk-2 execution file.
    A5M2.ENU                          English (U.S.) Language resource.
    A5M2.ENG                          English (U.K.) Language resource.
    history.txt                       change history.
    license.txt                       License regulation.
    license_en.txt                    License regulation.
    readme.txt                        readme.
    readme_en.txt                     this file.
    sampledb\*                        Sample database(Microsoft Access, ER Diagram)
    sample\*                          Sample script.
    scripts\*                         Script file.
    VirusCheck.txt                    Check result file of each file in anti-virus software.


[REQUIED SOFTWARE]
  None.


[INSTALL]
  ** ZIP File edition **
  Installation work is not necessary.

  You can use it by expanding the archive file and starting A5M2.exe.

  To use it in portable mode (described later), create "Portable" folder in the 
  same folder as A5M2.exe before executing.

  ** Microsoft Store edition **
  Install from the Microsoft Store.

[UPGRADE]
  ** ZIP File edition **
  You can use it by unpacking the archive file and launching A5M2.exe like 
  installation.

  Please unpack the archive file to a folder different from the old version.

  ** Microsoft Store edition **
  Upgrade from the Microsoft Store.


[UNINSTALL]
  ** X86 version or x86 version (read only version) **
  Delete the folder where the archive file was expanded.

  Delete registry \\HKEY_CURRENT_USER\Software\mmatsubara\a5m2(x86) .

  Delete directory (%APPDATA% is an environment variable) represented by 
  %APPDATA%\a5m2(x86)
    (Deleting the directory registry is not mandatory)

  After that, delete the folder with A5M2.exe.

 ** X64 version or x64 version (read only version) **
  Delete the folder where the archive file was expanded.

  Delete registry \\HKEY_CURRENT_USER\Software\mmatsubara\a5m2(x64) .

  Delete directory (%APPDATA% is an environment variable) represented by 
  %APPDATA%\a5m2(x64)
    (Deleting the directory registry is not mandatory)

  After that, delete the folder with A5M2.exe.

 ** When using in portable mode **
  Delete the folder with A5M2.exe.

 ** If you are not in portable mode and have ever activated in normal mode at 
  least once, X86 version, x86 version (read only version) or x64 version, 
  x64 version (read only version) Please follow the uninstallation procedure.

  ** Microsoft Store edition **
    Right-click A5: SQL Mk-2 icon in Start menu and select "Uninstall".


[HOW TO USE]
  When registering for the first time, the database registration screen will 
  be displayed. Register the database to use from there.

  When that is done, you can connect to each database from the tree on the 
  left and access the table view synonym and the stored procedure.

  You can test SQL statements by choosing Create New from the SQL menu. 
  You can execute select statements and other DML statements (Insert, Update, 
  Delete) in this window. DDL statements can also be executed with the syntax 
  provided by the connection destination RDBMS.

  Rough function list
  · Connection to various databases
    (You can connect directly to Oracle, PostgreSQL, MySQL, SQLite)
  · SQL input completion function (also analyzes common table expressions and subqueries)
  · Create and edit SQL with GUI
  · Show SQL Execution plan 
  · Format SQL
  · Continuous execution of SQL delimited by ";" (semicolon) or "/" (slash) or "GO" at the beginning of the line
  · Multiple result sets are output to Excel collectively
  · Execute SQL twice to output differences to Excel (also possible to compare multiple result sets)
  · Execution of SQL with parameters
  · Filtering of tables and query result sets (narrowing down)
  · A pseudo-life specifying a column name, a result set title, etc. in a query comment
    Function to embed decree
  · Table editor that can be output to Excel
  · Display property of table (additional RDBMS information)
  · Show table source
  · Export/Import of table contents
  · Insert a large amount of test dummy data into the table
  · Create ER diagram
  · Create ER diagram from database
  · Create DDL of database from ER diagram
  · Script language


[PORTABLE MODE]
  By creating a "Portable" folder in the same folder as A5M2.exe in advance, it 
  is possible to operate in "portable mode" where all settings and temporary 
  files / SQL log files are placed in the "Portable" folder I can do it.

  With this, you can place A5:SQL Mk-2 on a USB memory etc, and you can share 
  settings on each PC.

  Portable mode has the following features.

  · Do not write to the registry
  · Do not create temporary files other than "Portable" folder
  · All settings, temporary files, and SQL log files are encrypted with AES (256 bit)
  · Start password can be set

  In the portable mode, as described above, all settings, temporary files, and 
  SQL log files are encrypted with AES (key length: 256 bits). Therefore, if 
  you set up the startup password, even if you lose the USB memory with 
  A5:SQL Mk-2 in the unlikely event, you can set the DB setting information, 
  temporarily saved SQL · ER diagram · script, It is possible to minimize the 
  possibility of logged log files being leaked.

  Of course, you can also use the portable mode for not writing to the registry 
  without entering into the USB memory etc.

  Microsoft Store Edition is not available in portable mode.

[About used program components]
  In A5:SQL Mk-2 we use the following program parts (component and library). 
  I am thankful to the authors from the bottom of my heart.

  ・ActiveQueryBuilder Ver 1.17
      Active Database Software
      Commercial License
  ・DCPcrypt 2016/10/26(r13)
      Copyright © 1999-2002 David Barton
      MIT License
        http://a5m2.mmatsubara.com/open_source_license/DCPcrypt/MIT_license.txt
        https://opensource.org/licenses/mit-license.php
  ・DMonkey Version: 0.3.9
      Project DMonkey
      Proprietary license
  ・GDI+ API, GDI+ Class, GDI+ Util
      http://www.progdigy.com
      Mozilla Public License Version 1.1
      Source header (description about License) : http://a5m2.mmatsubara.com/open_source_license/progdigy.com/source_header.txt
      source : http://a5m2.mmatsubara.com/open_source_license/progdigy.com/gdiplus.zip
  ・NkPrinter(0.53)
      T.Nakamura
  ・SecureBridge Ver 9.0.2
      Devart
      Commercial License
  ・Syntax Editor SDK v 2.6.0
      EControl
      Commercial License
  ・TCtrlGridコンポーネント  Ver 2.10
    (TCtrlGrid Components Ver 2.10)
      ＳＵＮ
  ・UniDAC Ver 7.3.9
      Devart
      Commercial License
  ・フォント名コンボボックス(＆リストボックス) Version 1.2.1
    (Fontname Combobox(&Listbox) Version 1.2.1)
      CQN11335 加藤太朗
