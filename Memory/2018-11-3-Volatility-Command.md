---
layout: post
title: Volatility 명령어 정리 [업데이트 예정]
date: 2018-11-3
mathjax: true
tag: [VolatilityCommand]
categories: 0x01_MemoryForensic
---

# Plugins



Image Identification : 덤프 파일의 하드웨어 정보

  \- imageinfo, kdbgscan, kprcscan



Processes and DLLs : 프로세스 분석 및 DLL 분석

  \- pslist, pstree, psscan, dlllist, dlldump, handles, getsids, verinfo, enumfunc



Process Memory : 프로세스 메모리 분석

  \- memmap, memdump, procmemdump, procexedump, vadwalk, vadtree, vadinfo, vaddump



Kernel Memory and Objects : 커널 분석

  \- modules, modscan, moddump, ssdt, driverscan, filescan, mutantscan, symlinkscan, thrdscan



Networking : 네트워크 분석

  \- connections, connscan, Sockets, sockscan, netscan



Registry : 레지스트리 분석

  \- hivescan, hivelist, printkey, hivedump, hashdump, lsadump, userassist



Crash Dumps, Hibernation, and Conversion : 덤프 분석

  \- crashinfo, , hibinfo, imagecopy



Malware and Rootkits : 악성코드 및 루트킷 분석

  \- malfind, , svcscan, ldrmodules, impscan, apihooks, idt, gdt, threads, callbacks, driverirp, devicetree, psxview, ssdt_ex, timers



Miscellaneous : 스트링 분석

  \- strings, volshell, bioskbd, yarascan



## Volatility 명령어

vol.py -f [덤프뜰 파일] --profile=[프로파일] (플러그인)



1) pstree 



2) psscan



3) netscan



4) iehistory

인터넷 히스토리



5) dumpfiles

메모리상에 있는 파일 복구

vol.py -f [덤프뜰 파일] --profile=[프로파일] dumpfiles -Q [메모리주소] -D [디렉토리] 



6) memdump

특정 프로세스 PID값을 넣어 그 프로세스 추출 가능

vol.py -f [덤프뜰 파일] --profile=[프로파일] memdump -p [PID] -D [디렉토리]



7) mftparser

메모리에 로드된 디코딩 자료들 분석



8) filescan

메모리상에 로드된 모든 파일을 볼 수있다.



9) cmdscan



10) malfind

시그니처 패턴 정보



11) pslist



12) psxview



13) connections

네트워크 접속 관련 정보



14

참고 : https://code.google.com/archive/p/volatility/wikis/CommandReference23.wiki

