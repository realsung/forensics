---
layout: post
title: Memory Forensic Volatility
date: 2018-09-18
mathjax: true
tag: [메모리포렌식, MemoryForensic, Volatility, 메모리분석]
categories: 0x01_MemoryForensic
---



![volatility_banner](https://user-images.githubusercontent.com/32904385/45824595-df9ae780-bcdf-11e8-853a-a8746a526050.png)

#### Info

* Python 기반으로 반든 Memory Forensic Tool
* Windows, Linux, Mac OS에서 실행 가능하다.
* 오픈소스 형태이며, Plugin으로 여러 기능을 사용할 수 있다
* 직접 Plugin을 만들어서 사용할 수 있다.

#### Available

* 침대사고대응 관련
* 포렌식 관련 CTF

#### Extension

`메모리 덤프 파일(.img, .raw, .dmp)`

`하이버네이션 파일(.hiber)`

`가상 머신 메모리(.vmem)`

#### information available

* 트리 형태 프로세스 리스트
* 프로세스가 로드한 DLL과 핸들
* 프로세스 환경변수와 Import
* 네트워크 정보
* 시스템에서 로드한 드라이버 목록
* 루트킷으로 은닉된 프로세스 오프셋
* SID(보안 식별자)
* PID
* 스레드 수, 핸들 수, 시작 및 종료 시간

#### Command Format

```
$ vol.py -f [이미지경로][플러그인]
```

```
$ vol.py -f [이미지경로] --profile=[운영체제][플러그인]
```

#### Operating system information commands

```
$ vol.py -f memory.dd imageinfo
```

- 운영체제, 메모리 주소 공간, DTB, KDBG, KCPR 주소 출력

#### Time Info Commands

```
$ vol.py -f memory.dd timeliner —output-file result.csv
```

* 아티팩트를 시간과 함께 csv 파일로 출력

#### Executable Extract Commands

```
$ vol.py -f [이미지경로] procexedump -D [저장경로] -p [PID]
```



### Option

| 옵션              | 설명                                                         |
| ----------------- | ------------------------------------------------------------ |
| -h, --help        | 모든 옵션의 도움말과 해당 옵션의 디폴트 값 출력              |
| --conf-file       | 설정파일의 경로를 설정                                       |
| -d, --debug       | Volatility를 디버그함                                        |
| --plugins         | 플러그인이 위치할 폴더 설정(세미콜론을 이용해 추가 디렉터리 포함이 가능함) |
| --info            | 지원 운영체제나 각 플러그인의 기본 정보 출력                 |
| --cache-directory | 캐시 파일이 저장된 경로를 설정                               |
| --cache           | DTB(Directory Table Base), KDBG, KPCR 주소 등, 여러 변수를 저장해 추후에 사용할 수 있도록 함 |
| --tz              | 타임존을 설정한다(유닉스 계열만 가능하다)                    |
| -f, --filename    | 메모리 이미지의 경로를 설정                                  |
| --profile         | 운영체제 및 버전을 설정                                      |
| -l, --location    | 메모리 이미지의 URN 경로를 설정                              |
| -w, -write        | 쓰기모드를 활성화                                            |
| --use-old-as      | 레거시 주소 공간을 쓰도록 설정                               |
| --dtb             | DTB 주소를 설정                                              |
| --output          | 출력 파일의 포맷을 설정                                      |
| --output-file     | 출력 파일의 경로 설정                                        |
| -v, --verbose     | 진행상황을 출력                                              |
| -g, --kdbg        | KDBG 주소 값을 설정                                          |
| -k, --kpcr        | KPCR 주소 값을 설정                                          |



### Plugin

| 기능                           | 플러그인                                                     |
| ------------------------------ | ------------------------------------------------------------ |
| 이미지 정보                    | imageinfo, kdbgscan, kpcrscan                                |
| 프로세스, DLL                  | pslist, pstree, psscan, dlllist, dlldump, handles, getsids, verinfo, enumfunc |
| 프로세스 메모리                | Memmap, memdump, procmemdump, procexedump, vadwalk, vadtree, vadinfo, vaddump |
| 커널 메모리 & 오브젝트         | connections, connscan, sockets, sockscan, netscan            |
| 레지스트리                     | Hives can, hivelist, printkey, hivedump, hashdump, lsadump, userassist |
| 크래쉬 덤프, 하이버네이션 변환 | crashinfo, hibinfo, imagecopy                                |
| Malware, 루트킷                | Malfind, svcscan, ldrmodules, impscan, apihooks, idt, gdt, threads, callbacks, driverip, devicetree, pswview, ssdt_ex, timers |
| 기타                           | strings, volshell, bioskbd, inspectcache, patcher, testsuite |

##### Timeliner Plugin

| 아티팩트       | 플러그인                                     |
| -------------- | -------------------------------------------- |
| 프로세스       | pslist, psscan, pstree, procmemdump          |
| 쓰레드         | thrdscan                                     |
| 네트워크, 소켓 | netscan(Win7), connections(XP), connscan(XP) |
| 레지스트리     | Hivelist, printkey, userassist               |
| 실행파일(exe)  | Procexedump, handles                         |
| DLL 및 핸들    | dlllist, dlldump                             |
| 드라이버       | driverscan, driverirp, moddump               |

##### 루트킷 Plugin

| 플러그인 이름 | 설명                                                  |
| ------------- | ----------------------------------------------------- |
| psxview       | pslist와 psscan으로 숨겨진 프로세스를 찾음            |
| drivers can   | 메모리에서 드라이버 오브젝트 스캔                     |
| apihooks      | API/DLL 함수 후크를 찾음                              |
| ssdt          | SSDT(System Service Descriptor Table)에서 후크를 찾음 |
| driverirp     | (IRP)I/O Request Packet 후크를 찾음                   |
| idt           | IDT(Interrupt Descriptor Table)을 출력                |





[Volatility Github]: https://github.com/volatilityfoundation/volatility/wiki/Command-Reference#psscan



## Comments

{% include comments.html %}