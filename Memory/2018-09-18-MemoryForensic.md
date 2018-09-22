---
layout: post
title: Memory Forensic Concept
date: 2018-09-18
mathjax: true
tag: [메모리포렌식, MemoryForensic, Forensic]
categories: 0x01_MemoryForensic
---

 ![volatile_memory](https://user-images.githubusercontent.com/32904385/45638218-154f8e80-ba9c-11e8-85b2-9049ee0e929c.jpg)

<h4>What is Memory Forensic?</h4>
> 컴퓨터 하드웨어 중 주기억장치(메모리)에 존재하는 휘발성 데이터 덤프 분석하는 것을 말한다.

<h4>Memory Forensic Pros and cons</h4>
> **장점**
> - RAM은 시스템이 활성화 되어 있는 동안 시스템 런타임 상태의 중요 정보를 포함하고 있음
> - 언패킹, 루트킷 탐지, 리버스 엔지니어링 등에 도움이 된다.
>
> **단점**
> - 휘발성 데이터로 전원 차단 시 데이터가 사라짐 [컴퓨터가 커져있어야함]
> - 온전한 데이터 수집이 어렵다

<h4>What is Memory Dump?</h4>
> RAM의 물리메모리에 저장되어있는 데이터를 가져와서 파일로 만드는 것이다.
그래서 물리 메모리에 존재하는 모든 흔적들을 확인할 수 있다.

<h4>Memory Dump Method</h4>
<h6>1. 물리 메모리 덤프 방식</h6>

> 하드웨어를 이용한 덤프 : FireWire Attack(IEEE 1394)를 이용한 메모리 덤프, Tribble를 PCI 장치를 이용해 덤프한다.
장점
- 악성 프로그램에 영향을 받지 않는다.
- 빠른 메모리 덤프 가능하다.
- 무결성 최소화한다.
>
단점
- 안전성에 대한 검증이 필요하다
- 간혹 시스템 크래시 발생한다.


<h6>2. 소프트웨어를 이용한 덤프 방식</h6>
> DD, MDD, Winen, WIN32/64dd & Dumplt, Memorize ProDiscovery, HBGary, FastDumpPro, 크래시 덤프, 절전 덤프 등
장점
- 추가 장치가 필요없다.
- 오픈소스 및 프리웨어가 많다.
>
단점
- 커널 루트킷에 취약하다.
- OS 제약을 받는다.
- 수집하는 메모리쪽에 흔적이 남는다.

<h6>3. Virtual Machine Imaging</h6>
> - VMware 세션이 정지되면 물리 메모리 내용은 .vmem 확장자를 가지는 파일에 포함된다.
- vmem은 로우 포맷과 유사하고 다른 메모리 분석 도구를 통해 분석 가능하다.
- 악성코드를 가상머신에 올리고 폴더에 보면 .vmem이 생기는데 이것을 이용해서 덤프를 뜰 수 있다.

<h6>4. 절전모드 덤프(Hibernation)</h6>
> - 전력 관리를 보다 효율적으로 하기 위해 절전 상태에 돌입되면 하드 드라이브에 메모리 데이터를 기록한 다음 전력을 차단해 버리는 기능이다.
- 윈도우는 절전모드로 들어갈 경우 물리메모리 내용을 압축해 C:hiberfil.sys파일로 저장한다.
- 부팅 과정에서 hiberfil.sys가 설정되어 있으면 NTLDR에 의해서 메모리로 로드 된 후에 이전 상태로 돌아간다.

### 휘발성 강한 순서

```
1 - CPU, 캐시 및 레지스터 데이터
2 - 라우팅 테이블, ARP 캐시, 프로세스 테이블, 커널 통계
3 - 메모리
4 - 임시 파일 시스템 / 스웝 공간
5 - 하드 디스크에 있는 데이터
6 - 원격에 있는 로그 데이터
7 - 아카이브 매체에 있는 데이터
```

## Comments

{% include comments.html %}