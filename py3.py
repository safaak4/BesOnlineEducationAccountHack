from webbot import Browser
import time

web = Browser()

linklerlist = ["https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=MEHMET+B***&password=ogrencix123&checksum=681af1b2899e57845466b9319cc67e58c1ef2653",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=ZEYNEP+S***&password=ogrencix123&checksum=33147e62800d123bbb8b468dfaaaa7aeb99c5dea",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=SENANUR+T***&password=ogrencix123&checksum=a7ad9c1145583010fe199f87bb70f10445f8b6e8",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=ENDER+EMRE+H***&password=ogrencix123&checksum=8c0a9821dd7ed9eb64926daabe7f3398daba8660",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=BERKE+RAFET+U***&password=ogrencix123&checksum=dea507d9cb1ebb972e15573e7ff71cc78ec853fa",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=ZEYNEP+%C3%96***&password=ogrencix123&checksum=72764020b6ea3001824121cad5a189e842529b69",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=CUMA+%C5%9EAFAK+K***&password=ogrencix123&checksum=6f22be034730b33239dc33a3beee11646b017d8c",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=ALEYNA+YA%C4%9EMUR+***C3%87&password=ogrencix123&checksum=c3384e99ce2d8bae24ddfbdb799b7e8df8e55c44",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=SARP+***A&password=ogrencix123&checksum=8161360028112f75875f995e87aa8c1c81f81188",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=HASAN+TOLGA+A***&password=ogrencix123&checksum=62b0eb8d1c1f8dc2f99ab9d4d4622056c2981a37",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=%C3%9CM%C4%B0T+ARDA+TA***&password=ogrencix123&checksum=9b93f7815718b3679f868408f06b5f8073a1b4b1",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=%C***REM+TU%C4%9E%C3%87E+U***&password=ogrencix123&checksum=e05eefdec8135b36f94cde14e571e4d7d4e716c7",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=SA***R+Y***&password=ogrencix123&checksum=babbc4059778048f2d276a937c89a471a3d2152a",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName***%B0S+NUR+T%C***&password=ogrencix123&checksum=2952574472528bfd0cb589c9520afb011f478f4e",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=H%***Y%C4%B0N+EMRE+%C3%***R&password=ogrencix123&checksum=104d75f0c060cbcd7e20bd2ca3f54b8465b8ef43",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=EM***4%B0N***0LER&password=ogrencix123&checksum=9b9db0244cda4b46d702d7aedaad4f6ef4569ef8",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=A***C4%B***&password=ogrencix123&checksum=f9e1f1141f5a5aeb9236d457780eeb86eedeb9a8",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=TU%C4%9E%C3%****E&password=ogrencix123&checksum=e07d182bc14a1d4f2878a6407e145433063fc57a",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=RO***B0N+%***0K&password=ogrencix123&checksum=6387b2b05edfbeb522db0286701409e37426b559",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=AHM*****cix123&checksum=848237c2050d98c64cf785feae1910c6e1e99d56",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=L%C3%9CTF%C3***0R+ALAKOCA&password=ogrencix123&checksum=0b3c1a5deb8a3767842be8e9abab4f2372a1f057",
"https://server148.neteorservers.com/bigbluebutton/api/join?meetingID=44662&fullName=%C3%***M***sword=ogrencix123&checksum=60ddac06f56878b6dc79c437e294fd1503f71268"]

sayaclink = 0
while sayaclink <=21:
    web.new_tab(linklerlist[sayaclink])
    time.sleep(12)
    sayaclink += 1
