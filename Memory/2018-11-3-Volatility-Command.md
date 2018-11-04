---
layout: post
title: Volatility 명령어 정리 [업데이트 예정]
date: 2018-11-3
mathjax: true
tag: [VolatilityCommand]
categories: 0x01_MemoryForensic
---



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

