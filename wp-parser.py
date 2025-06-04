import os #line:1
import re #line:2
import threading #line:3
import platform #line:4
from colorama import init ,Fore #line:5
init (autoreset =True )#line:7
def parse_credentials (OO0OO000O00O00000 ,OOOO000OO000O00O0 ,O0OO0O00O0OO0O0O0 ,O000O0O00O0OOO0O0 ):#line:9
    O0O0000O0OO0000OO =[r'(https?://[^\s]*wp-login\.php):([^\s:]+):([^\s:]+)',r'(https?://[^\s]*wp-login\.php)\|([^\s|]+)\|([^\s|]+)',r'(https?://[^\s]*wp-login\.php)#([^\s@]+)@([^\s@]+)',r'(https?://[^\s]*wp-login\.php)#([^\s@]+)@([^\s@]+)@([^\s@]+)',r'(https?://[^\s]*wp-login\.php)\s*:\s*([^\s:]+)\s*:\s*([^\s:]+)']#line:16
    try :#line:18
        with open (OO0OO000O00O00000 ,'r',encoding ='utf-8',errors ='ignore')as O0000OO000O0O0OO0 :#line:19
            for OO0000000000OOOOO in O0000OO000O0O0OO0 :#line:20
                for OOOO000OO000OOO00 in O0O0000O0OO0000OO :#line:21
                    try :#line:22
                        OOOOO00O0O00000OO =re .findall (OOOO000OO000OOO00 ,OO0000000000OOOOO ,re .IGNORECASE )#line:23
                        for OOOOO0OOO0O0OO00O in OOOOO00O0O00000OO :#line:24
                            OO0O0O0OO0OO0O0OO =OOOOO0OOO0O0OO00O [0 ]#line:25
                            with O0OO0O00O0OO0O0O0 :#line:26
                                if len (OOOOO0OOO0O0OO00O )==3 :#line:27
                                    O0O0OOO000OO00000 =f"{OO0O0O0OO0OO0O0OO}|{OOOOO0OOO0O0OO00O[1]}|{OOOOO0OOO0O0OO00O[2]}"#line:28
                                elif len (OOOOO0OOO0O0OO00O )==4 :#line:29
                                    O0O0OOO000OO00000 =f"{OO0O0O0OO0OO0O0OO}|{OOOOO0OOO0O0OO00O[1]}|{OOOOO0OOO0O0OO00O[2]}@{OOOOO0OOO0O0OO00O[3]}"#line:30
                                if O0O0OOO000OO00000 not in OOOO000OO000O00O0 :#line:31
                                    OOOO000OO000O00O0 .add (O0O0OOO000OO00000 )#line:32
                                    print (f"{Fore.YELLOW}[ {Fore.RESET}Found {Fore.YELLOW}]{Fore.RESET} {O0O0OOO000OO00000} {Fore.RESET}| {Fore.GREEN}[ FOUND ]{Fore.RESET}")#line:33
                                    with open (O000O0O00O0OOO0O0 ,'a',encoding ='utf-8')as O000OO0OOO0OOO0OO :#line:34
                                        O000OO0OOO0OOO0OO .write (O0O0OOO000OO00000 +'\n')#line:35
                    except re .error as OOOO00OOOOO000OO0 :#line:36
                        print (f"{Fore.RED}[!] Regex error in {OO0OO000O00O00000} for pattern {OOOO000OO000OOO00}: {OOOO00OOOOO000OO0}{Fore.RESET}")#line:37
    except Exception as O0O0O00OO0000O0OO :#line:38
        print (f"{Fore.RED}[!] Error reading {OO0OO000O00O00000}: {O0O0O00OO0000O0OO}{Fore.RESET}")#line:39
def extract_credentials_from_folder (O00OO000OO0OO0OO0 ,OOOO0OO000OO0O0OO ,OOOO0OOO0OOO000O0 ):#line:41
    open (OOOO0OO000OO0O0OO ,'w',encoding ='utf-8').close ()#line:42
    OOO00OO0OOOO00000 =set ()#line:43
    O00OO0O00000OOOO0 =threading .Lock ()#line:44
    OOO00O00000O00O0O =[]#line:45
    OOOO0O00O00O0O0OO =[O0OO000OO00O0OOOO for O0OO000OO00O0OOOO in os .listdir (O00OO000OO0OO0OO0 )if O0OO000OO00O0OOOO .endswith ('.txt')]#line:46
    if not OOOO0O00O00O0O0OO :#line:48
        print (f"{Fore.RED}[!] Tidak ada file .txt di {O00OO000OO0OO0OO0}.{Fore.RESET}")#line:49
        return #line:50
    def OOO00OO0O0O00OO00 ():#line:52
        while OOOO0O00O00O0O0OO :#line:53
            O0OOOOOOOO0O0000O =OOOO0O00O00O0O0OO .pop ()#line:54
            OOO00OO0O000OO0OO =os .path .join (O00OO000OO0OO0OO0 ,O0OOOOOOOO0O0000O )#line:55
            print (f"{Fore.CYAN}[*] Memproses {OOO00OO0O000OO0OO}...{Fore.RESET}")#line:56
            parse_credentials (OOO00OO0O000OO0OO ,OOO00OO0OOOO00000 ,O00OO0O00000OOOO0 ,OOOO0OO000OO0O0OO )#line:57
    for _O00O0OO0O0OOO0O0O in range (min (OOOO0OOO0OOO000O0 ,len (OOOO0O00O00O0O0OO ))):#line:59
        O0OO000OO0OO0O000 =threading .Thread (target =OOO00OO0O0O00OO00 )#line:60
        OOO00O00000O00O0O .append (O0OO000OO0OO0O000 )#line:61
        O0OO000OO0OO0O000 .start ()#line:62
    for O0OO000OO0OO0O000 in OOO00O00000O00O0O :#line:64
        O0OO000OO0OO0O000 .join ()#line:65
    print (f"{Fore.GREEN}Extraction complete. {len(OOO00OO0OOOO00000)} credentials saved to {OOOO0OO000OO0O0OO}{Fore.RESET}")#line:67
def main ():#line:69
    if platform .system ()=="Windows":#line:70
        os .system ('cls')#line:71
    else :#line:72
        os .system ('clear')#line:73
    print (f"""
{Fore.YELLOW}
 ██████╗ ██╗  ██╗███████╗ █████╗ ██╗     ███████╗██╗  ██╗██╗████████╗██╗  ██╗███████╗███╗   ███╗ █████╗ 
██╔═══██╗╚██╗██╔╝╚════██║██╔══██╗██║     ██╔════╝╚██╗██╔╝██║╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔══██╗
██║   ██║ ╚███╔╝    ██╔╝ ███████║██║     █████╗   ╚███╔╝ ██║   ██║   ███████║█████╗  ██╔████╔██║███████║
██║   ██║ ██╔██╗   ██╔╝  ██╔══██║██║     ██╔══╝   ██╔██╗ ██║   ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══██║
╚██████╔╝██╔╝ ██╗  ██║   ██║  ██║███████╗███████╗██╔╝ ██╗██║   ██║   ██║  ██║███████╗██║ ╚═╝ ██║██║  ██║
 ╚═════╝ ╚═╝  ╚═╝  ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝
{Fore.RESET}
    """)#line:84
    O0000O00O00OOOOO0 =input ("Masukkan directory yang berisi .txt: ")#line:86
    O0OO00O000000O000 =input ("Masukkan nama result (example: result.txt): ")#line:87
    OO0000OO0O0O0O0OO =int (input ("Masukkan jumlah threads: "))#line:88
    OOOOOO0OOO00O0O00 =input ("Mamulakan scan! Adakah kamu mau melanjutkan? (y/n): ").strip ().lower ()#line:89
    if OOOOOO0OOO00O0O00 !='y':#line:91
        print (f"{Fore.RED}Scan dibatalkan.{Fore.RESET}")#line:92
        return #line:93
    if not os .path .isdir (O0000O00O00OOOOO0 ):#line:95
        print (f"{Fore.RED}[!] Directory {O0000O00O00OOOOO0} tidak valid.{Fore.RESET}")#line:96
        return #line:97
    extract_credentials_from_folder (O0000O00O00OOOOO0 ,O0OO00O000000O000 ,OO0000OO0O0O0O0OO )#line:99
if __name__ =="__main__":#line:101
    main ()
