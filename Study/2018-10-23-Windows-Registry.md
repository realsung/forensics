---
layout: post
title: Windows 레지스트리
date: 2018-10-23
mathjax: true
tag: [레지스트리]
categories: 0x00_Info-Forensic
---

## Windows 레지스트리

### Hive 파일

- 레지스트리 정보를 저장하고 있는 물리적인 파일
- key값들이 논리적인 구조로 저장
- 활성 시스템의 커널에서 하이브 파일을 관리

### 구성

5개의 루트키를 가진다. 각 루트키 아래의 하위 키부터 모든 하위 키를 포함하는 트리 구조를 하이브라고 한다. 그리고 각각의 하이브는 고유한 파일과 로그를 가지고 있다.

 ![](https://user-images.githubusercontent.com/32904385/47325467-d87c4600-d69e-11e8-9c72-f4222f09a585.png)



### HKEY_CLASSES_ROOT

`Windows 탐색기`를 사용해 파일을 열 때 정확한 프로그램이 열리도록 하고 윈도우에서 사용하는 프로그램과 각 프로그램에 연결된 `확장자`에 대한 정보를 담고 있다.



### HKEY_CURRENT_USER

현재 로그온하고 있는 사용자의 `구성 정보 루트`, 사용자 `프로필` 정보를 담고 있다.

| 하위키                 | 설명                                                   |
| ---------------------- | ------------------------------------------------------ |
| AppEvents              | 사운드, 이벤트 관련 키                                 |
| CLSID                  | COM 객체 연결 정보                                     |
| Console                | 명령 프롬프트 윈도우 설정 정보(가로, 세로크기, 색상등) |
| ControlPanel           | 데스크탑 테마, 키보드/마우스 세팅 등의 환경 설정 정보  |
| Environment            | 환경변수 정의                                          |
| EUDC                   | 최종 사용자가 정의한 문자 정보                         |
| Identities             | 윈도우 메일 계정 정보                                  |
| KeyboardLayout         | 키보드 레이 아웃 설정 정보                             |
| Network                | 네트워크 드라이브 매핑 정보, 환경설정 값               |
| Printers               | 프린트 연결 설정                                       |
| Session Information    | 작업 표시줄에 표시 되는 현재 실행되는 프로그램 설정    |
| Software               | 로그인 한 사용자 소프트웨어 목록                       |
| System                 | HKLM/SYSTEM 하위키의 일부(Control, Policies, Services) |
| UNICODE Program Groups | 로그인 한 사용자 시작 메뉴 그룹 정의                   |
| Volatile Environment   | 휘발성 환경 변수                                       |



### HKEY_LOCAL_MACHINE

시스템의 `하드웨어` , `소프트웨어` 설정 및 환경정보를 담고있다.

| 하위키      | 내용                                                         |
| ----------- | ------------------------------------------------------------ |
| BCD00000000 | Boot Configuration Data 관리(XP의Boot.ini 대체)              |
| COMPONENTS  | 설치된 Components와 관련된 정보 관리                         |
| HARDWARE    | 시스템 하드웨어 디스크립션과 모든 하드웨어의 장치 드라이버 매핑 정보(Volatile hive) |
| SAM         | 로컬 계정 정보와 그룹 정보(시스템 계정만 접근 가능)          |
| SECURITY    | 시스템 보안정책과 권한 할당 정보(시스템 계정만 접근 가능)    |
| SOFTWARE    | 시스템 부팅에 필요 없는 시스템 전역 구성 정보(소프트웨어 정보) |
| SYSTEM      | 시스템 부팅에 필요한 시스템 전역 구성 정보                   |



### HKEY_USERS

시스템의 `모든 사용자`와 `그룹`에 관한 프로파일 정보



### HKEY_CURRENT_CONFIG

시스템이 시작할 때 사용되는 `하드웨어` 프로파일 정보



### 기본 시스템 정보 확인

`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion`![](https://user-images.githubusercontent.com/32904385/47327383-01550900-d6a8-11e8-9a94-a84cabb28392.png)

cmd창에서 `systeminfo`를 사용해서도 활성정보 수집을 할 수 있다.



### 컴퓨터 이름 확인

`HKLM\SYSTEM\ControlSet00X\Control\ComputerName\ActiveComputerName`의 ComputerName을 확인하면 컴퓨터 이름을 확인 할 수 있다.![](https://user-images.githubusercontent.com/32904385/47327612-f2228b00-d6a8-11e8-8b33-b1e4c71ab497.png)



### 시스템 종료 시간

`HKLM\SYSTEM\ControlSet00X\Control\Windows`의 ShutdownTime을 확인하면 마지막 종료 시간이 저장된다. 그런데 인코딩 되어있어서 디코더를 이용해서 OS버전과 맞춰 확인해야한다.

![](https://user-images.githubusercontent.com/32904385/47331453-ff467680-d6b6-11e8-818f-f9a78e0ba14f.png)

내 시스템의 ShutdownTime은 `1d de 31 75 7e 63 d4 01`이다.

![](https://user-images.githubusercontent.com/32904385/47331615-99a6ba00-d6b7-11e8-968c-0f0dbc7c7b92.png)

디코딩해보면 내가 컴퓨터를 마지막으로 종료한 시간은 UTC기준으로 2018년 10월 14일 일요일 5시 26분 28초이다.

