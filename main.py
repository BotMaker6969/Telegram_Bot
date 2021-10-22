import telebot


bot = telebot.TeleBot("2042205018:AAF7MN1zNTCmqpdMXY9t2tEpYNXHt0JoD3I")


@bot.message_handler(commands=['kickme'])
def greet(message):
    bot.reply_to(
        message, '''Leave manually u Retarded attention seeker''')

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(
        message, '''
Hello, I am a bot made by @heckerMassiah.
For help do /help...
  ''')

@bot.message_handler(commands=['splash'])
def greet(message):
    bot.reply_to(
message, '''
Custom Splashes For Pine--
hsx | prjkt° #1 ->  t.me/hsxbuilds/599
hsx | prjkt° #2 ->  t.me/boottheming_sdm439/345
android 12 inspired t.me/boottheming_sdm439/369
Nusantara inspired  t.me/boottheming_sdm439/365
CherishOS inspired  t.me/boottheming_sdm439/361
')

@bot.message_handler(commands=['lineage'])
def greet(message):
    bot.reply_to(
        message, ''' CAFExBABE Lineage 18.1
        
        t.me/c/1501031540/4
        
        ''')
    
    
@bot.message_handler(commands=['gsi'])
def greet(message):
    bot.reply_to(
        message, '''
GSI--
-- /nusantara_gsi
-- /corvusgsi
-- /a12_gsi
-- /dotos
-- /descendant
-- /aosp_gsi
-- /octavi_gsi
-- /ancient_gsi
-- /havoc_gsi
  ''')


@bot.message_handler(commands=['a12'])
def help(message):
    bot.reply_to(message, '''
 t.me/hsxbuilds/659
    
    ''')


@bot.message_handler(commands=['nusantara_gsi'])
def greet(message):
    bot.reply_to(
        message, '''
GSI for R7A - Nusantara--
    link -- bit.ly/3k0nNjO
    
if don't know how to flash /gsi_tutorial
  ''')


@bot.message_handler(commands=['gsi_tutorial'])
def greet(message):
    bot.reply_to(
        message, '''
First download GSI ( /gsi_roms ) | BASE( /base ) | PERMISSIVER( /permissiver ) | GAPPS( /gapps )

-- Then place them in an SDCard or PenDrive cuz we need it and 'Extract' the gsi you downloaded.
-- After That Go to your recovery and wipe (Dalvik, Cache, System and Data)
-- Then go to install and flash the base then the GSI.img and Permissiver
-- Then go to 'wipe' section and select 'system' and click repair < Resize and swipe.
-- Then flash the Gapps ( /gapps )

Reboot and Fire!
  ''')


@bot.message_handler(commands=['permissiver'])
def greet(message):
    bot.reply_to(message, '''
Link -- bit.ly/3BVXT6M
  ''')


@bot.message_handler(commands=['corvusgsi'])
def greet(message):
    bot.reply_to(
        message, '''
DO /gsi_tutorial FOR GUIDE
Corvus GSI-->
Its an unofficial gsi with 0 bugs.
-- Link for BASE 2.1 -> /base
-- Don't FORGET permissiver /permissiver
-- Link for brightness fix-> t.me/PineOfficial/98989
-- Link for GSI -> https://bit.ly/3E05e74
TESTED  ✅
  :D
DON'T FLASH KERNEL 
  ''')


@bot.message_handler(commands=['brightness'])
def greet(message):
    bot.reply_to(message, '''
  BRIGHTNESS FIX-> t.me/PineOfficial/98989
  ''')


@bot.message_handler(commands=['base'])
def greet(message):
    bot.reply_to(
        message, '''
Base 1.2 -> t.me/PineOfficial/107862
Base 1.9 -> t.me/PineOfficial/137127
Base 2.1 -> t.me/redmi7acommunity/149079
Base 3.1 -> t.me/redmi7acommunity/149081
Base 3.2 -> t.me/redmi7acommunity/149082
  ''')


@bot.message_handler(commands=['help'])
def greet(message):
    bot.reply_to(message, '''
COMMANDS:- 
-> /r7a (Redmi7A)
''')


@bot.message_handler(commands=['sayhi'])
def greet(message):
    bot.reply_to(
        message, '''
Hello I am Guider Bomt. Rose is trash so they added me! lul 😏
  ''')


@bot.message_handler(commands=['guide'])
def greet(message):
    bot.reply_to(
        message, '''
-> do /guiderom if installing rom...
      
-> do /gsi_tutorial if having trouble installing gsi...
  
 put slash/ at start. 
''')


@bot.message_handler(commands=['lyl'])
def greet(message):
    bot.reply_to(
        message, '''
  Love Your Life, the people who hate you are afraid of your success....  :)'''
    )


@bot.message_handler(commands=['oos'])
def greet(message):
    bot.reply_to(
        message, '''
    t.me/xr7ap/67
  
Currently the best gaming rom.
Bug:- While in a call or meeting u cannot play videos.
  ''')


@bot.message_handler(commands=['notes'])
def greet(message):
    bot.reply_to(
        message, '''
Notes:---
- Want gapps -------------------/gapps
- Want all roms for r7a ------- /allroms
- Want kernel for your device --/kernel
- Want to improve gaming -------/gaming
- Don't know how to flash ------/guiderom
- Want GSI's -------------------/gsi
- Guide to flash gsi? ----------/gsi_tutorial     
  ''')


@bot.message_handler(commands=['r7a'])
def greet(message):
    bot.reply_to(
        message, '''
COMMANDS:- 
-> /dotos
-> /nusantara
-> /dotfe
-> /gapps
-> /kernel
-> /gaming
-> /allroms
-> /gsi_guide
-> /guiderom
-> /recoverypine
-> /gsi_tutorial
-> /a13-preview
''')

 
@bot.message_handler(commands=['a13-preview'])
def greet(message):
    bot.reply_to(
        message, ''' bit.ly/3C5uesj
      Link Of preview
      Its still not official....''')

@bot.message_handler(commands=['dotos'])
def greet(message):
    bot.reply_to(
        message, '''
1:   /dotosguide 
2:   /dotosvanilla
3:   /dotosgapps 
4:   /gapps11
  ''')


@bot.message_handler(commands=['dotfe'])
def greet(message):
    bot.reply_to(
        message, '''
•DotFE (Dot OS Fan Edition) is another official rom for Redmi7A by Pro_xIx.
      
•Do /dotfelink for rom and /gapps11 for gapps.''')


@bot.message_handler(commands=['kernel'])
def greet(message):
    bot.reply_to(
        message, '''
1: /cherrykernel 
2: /chuck_kernel 
3: /chaeyoungkernel
4: /ralegacykernel
5: /silontkernel
''')

@bot.message_handler(commands=['chaeyoungkernel'])
def greet(message):
    bot.reply_to(
        message, '''
   t.me/Redmi7AUpdates/229  
        
        
''')
    
    
@bot.message_handler(commands=['ralegacy'])
def greet(message):
    bot.reply_to(
        message, '''
    t.me/Redmi7AUpdates/163    
        
        
''')
    
    
@bot.message_handler(commands=['partition'])
def greet(message):
    bot.reply_to(
        message, '''
-->  VBmeta ->      /vbmeta
-->  Cust   ->      /cust
-->  Splash ->      /splash
-->  Vendor ->      /base
-->  System ->      /gsi

        
        
''')
   

@bot.message_handler(commands=['cust'])
def greet(message):
    bot.reply_to(
        message, '''
  t.me/c/1501031540/3    
        
        
''')



    
@bot.message_handler(commands=['vbmeta'])
def greet(message):
    bot.reply_to(
        message, '''

  t.me/c/1501031540/2      
        
''')
    
    
    
    
@bot.message_handler(commands=['silontkernel'])
def chat(message):
    bot.reply_to(
        message, '''
Maintainers: ChuckDXD
Device: 
- Redmi 8 (olive)
- Redmi 8A (olivelite)
- Redmi 8A Pro/Dual (olivewood)
- Redmi 7A (pine)
Build date: 05/09/2021

    Download: www.pling.com/p/1589765/

Changelog:
• Initial Release
• Rebased over Joel A11/lineageos source
• BLOCKED ANY POSSIBLE CANCER TWEAK FROM BEING BOOT
• Compiled with Ngentod GCC + LTO + -O3 optimization
• Switch to SLMK driver
• Use performance on LITTLE cluster
• Default maple I/O scheduler, lz4 ZRAM, and bbr TCP
• Disable CAF CPU boost
• Enable devfreq boost & CPU input boost
• Use power efficient workqueue
• Full Changelog
Credits and Thanks:
• Thanks to #GengKapak and many more for their support 
    
    ''')


  
@bot.message_handler(commands=['chuck_kernel'])
def greet(message):
    bot.reply_to(
        message, '''
Chuck.Kernel - 1.4
Device: Xiaomi SDM439 (Mi439)
Date - 03/08/2021
By - ChuckDXD
▪️Download Link: https://sourceforge.net/projects/gengkapak/files/Kernel/Chuck.Kernel/Mi439/Chuck.Kernel-Mi439-1.4-2021-08-03.zip/download
▪️Changelog:
• Rebased to Kud base
• Compiled with Choki GCC 9.4.1
• Upstreamed to 4.9.277
• Merge tag LA.UM.9.6.2.r1-04800-89xx.0
• Added wireguard
• Disable more debug
• Switched to PRLMK driver
• Added adreno boost
• Sched improvement
• Performance improvements
DOWNLOAD --- https://sourceforge.net/projects/gengkapak/files/Kernel/Chuck.Kernel/Mi439/Chuck.Kernel-Mi439-1.4-2021-08-03.zip/DOWNLOAD'''
    )


@bot.message_handler(commands=['guiderom'])
def greet(message):
    bot.reply_to(
        message, '''
-> Go to TWRP
-> Go to wipe section
-> Go to Advanced wipe
-> Select Dalvik, Cache, System, Data
-> Swipe To wipe
-> Then Go to Install and Flash Rom And gapps /gapps
-> Then  format Data And You're gud to go!''')


@bot.message_handler(commands=['dotosvanilla'])
def greet(message):
    bot.reply_to(
        message,
        "https://t.me/hsxdiscussion/3887"
    )


@bot.message_handler(commands=['dotosgapps'])
def greet(message):
    bot.reply_to(
        message,
        "https://t.me/hsxdiscussion/3888"
    )


@bot.message_handler(commands=['gapps11'])
def greet(message):
    bot.reply_to(message, "-> bit.ly/3mEiSGS")


@bot.message_handler(commands=['peplus'])
def greet(message):
    bot.reply_to(message, "https://download.pixelexperience.org/pine")


@bot.message_handler(commands=['recoverypine'])
def greet(message):
    bot.reply_to(
        message, '''
      64bit TWRP:---
androidfilehost.com/?fid=14943124697586357172
      
      64bit PBRP:---
pitchblackrecovery.com/pine  
  ''')


    
    
@bot.message_handler(commands=['nusantara'])
def greet(message):
    bot.reply_to(
        message, '''
t.me/Redmi7AUpdates/186 --> V2.8
t.me/Redmi7AUpdates/188 --> V2.9
t.me/Redmi7AUpdates/198 --> V3.0 (Vanilla) 
t.me/Redmi7AUpdates/199 --> V3.0 (Gapps)
t.me/Redmi7AUpdates/165 --> LTS 1.1 (Vanilla)
{ /gapps for gapps}
  
{For Guide to how to install use /guiderom}
      
And /gapps11 for Gapps A11
  ''')


@bot.message_handler(commands=['nusantaraguide'])
def greet(message):
    bot.reply_to(
        message, '''
-> Go to TWRP
-> Go to wipe section
-> Go to Advanced wipe
-> Select Dalvik, Cache, System, Data
-> Swipe To wipe
-> Then Go to Install and Flash Rom And gapps /gapps
-> Then  format Data And You're gud to go!
  
''')


@bot.message_handler(commands=['cherrykernel'])
def greet(message):
    bot.reply_to(
        message, '''
https://t.me/CherryKernel_SDM439/59
  
🍒 Stable V2.3 release!
Changelog:
- Upstreamed to 4.9.280
- Initial Android 12 support.
- Improved deep sleep.
- Updated unification drivers, switched to new legacy_omx param.
- Fixed headset volume buttons.
- Replaced Xiaomi's pstore_reserve_mem ramoops implementation with proper drop-in standard-compliant replacement.
- Reverted TCP ECN to defaults (enabled only when requested by incoming connections, fixes network performance regressions on some ISPs)
- Fixed scheduler regressions.
- Removed BCL. Fixed CPU throttling at low battery levels.
Bug:- Deep Sleep bug in Android12. 
      Charging Speed is not fast.
- Removed Prima's debug and tracing bloat.
- Added srandom.
DOWNLOAD :--- https://t.me/CherryKernel_SDM439/59
Credits:--- AkiraNoSushi and Flopster101  
#release  
  ''')


@bot.message_handler(commands=['gapps'])
def greet(message):
    bot.reply_to(message, '''
-> /gapps11
-> /gapps10
  ''')


@bot.message_handler(commands=['gapps10'])
def greet(message):
    bot.reply_to(message, '''
-> bit.ly/3kH4N98
  ''')


#All Roms Start Here


@bot.message_handler(commands=['gaming'])
def greet(message):
    bot.reply_to(
        message, '''
Gaming-->
-- /havocos --
-- /corvusos --
-- /nusantara --
-- /oos -- (OxygenOS)
-- /70hz --
  ''')


@bot.message_handler(commands=['70hz'])
def greet(message):
    bot.reply_to(
        message, '''
70hz kernel--> 
-- t.me/CherryKernel_SDM439/59
#Backup your boot before flashing.''')


@bot.message_handler(commands=['allroms'])
def greet(message):
    bot.reply_to(
        message, '''
All Roms For R7A->
-- dotos --
-- dotfe --
-- nusantara --
-- havocos --
-- corvusos --
-- evox --
-- oos --
-- sparkos --
-- zeusos --
-- psakura --
-- crdroid --
-- fluid --
Put slash/ at start of command.....
:)
  ''')


@bot.message_handler(commands=['sparkos'])
def greet(message):
    bot.reply_to(
        message, '''
VANILLA---
https://t.me/Redmi7AUpdates/203
GAPPS--- /gapps
https://t.me/Redmi7AUpdates/202
''')


@bot.message_handler(commands=['evox'])
def greet(message):
    bot.reply_to(
        message, '''
EvolutionX--->
  
bit.ly/38qPDPk
  
NOT THE BEST ROM BUT WORTH A TRY!!
  ''')


@bot.message_handler(commands=['zeusos'])
def greet(message):
    bot.reply_to(message, '''
t.me/Redmi7AUpdates/222 --> ZeusOS
  
/gapps
:)
  ''')


@bot.message_handler(commands=['havocos'])
def greet(message):
    bot.reply_to(
        message, '''
HavocOS V4.9 by @atharv2951

https://t.me/projectxtrmupdates/604
  ''')


@bot.message_handler(commands=['crdroid'])
def greet(message):
    bot.reply_to(
        message, '''
CrDroid-->
  
bit.ly/3zx1jw6
  
/guiderom if having any problem
  :D
  ''')


@bot.message_handler(commands=['bing'])
def greet(message):
    bot.reply_to(message, '''
Bonk!!! ''')


@bot.message_handler(commands=['ping'])
def greet(message):
    bot.reply_to(message, '''
Pong!
  ''')


@bot.message_handler(commands=['fuk'])
def greet(message):
    bot.reply_to(message, '''
  same to you cat🐱''')


@bot.message_handler(commands=['hi'])
def greet(message):
    bot.reply_to(message, '''
 watcha dog doin!!
  
 ''')


@bot.message_handler(commands=['corvusos'])
def greet(message):
    bot.reply_to(
        message, '''
CorvusOS-->
CORVUS 10 | Vanilla
Updated: 03/04/21
By pro_xix
Rom Download :- https://sourceforge.net/projects/mybuildx/files/corvusq/Corvus_Android-10-pine-03042021-Unofficial-0832.zip/download (698mb)
https://t.me/pineoficiales/204912
Need Base :- v3.2 (Thanks for @SimplyJoel)
Changelog :- Initial build with BT audio
Installation guide :-
• Wipe all - Dalvik/data/cache/system/vendor
• Flash Base
• Flash the ROM zip
• Format Data
• Reboot & Fire
Bugs :-
• LED light only in notification Use 'bit.ly/3kzYF2n'
• DT2W Use 'bit.ly/3sXu0zz'
• Brightness Use 'bit.ly/3mNq1Vg'(flash via magisk)
• BT audio Use 'bit.ly/3mLkmz4'(mount vendor & flash zip from recovery)
Credit/Thanks :-
• @Exodev_698 for trees
• @BayoBT for BT Patch fix
• @zubairk22 for help 
• @SexyDeadPooI for test...
  ''')




@bot.message_handler(commands=['hello69'])
def greet(message):
    bot.reply_to(
        message, '''Hello Buddy, How u doin. I am a bot🎶, and Iam so hot🎶
Go fuk yourself now!!''')


@bot.message_handler(commands=['fuckyou'])
def greet(message):
    bot.reply_to(message, "no, fuck youuu, you lil cat")


@bot.message_handler(commands=['night'])
def greet(message):
    bot.reply_to(message, "bots dont sleep")


@bot.message_handler(commands=['morning'])
def greet(message):
    bot.reply_to(message, "Gud morning!!!!")


@bot.message_handler(commands=['fun'])
def greet(message):
    bot.reply_to(
        message, '''
:-- /hello
:-- /morning
:-- /night
:-- /bing
:-- /ping
  ''')

@bot.message_handler(commands=['bruh'])
def greet(message):
    bot.reply_to(
        message, ''' hehe  ''')


bot.polling()
