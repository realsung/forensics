---
layout: post
title: Virtual Machine Files
date: 2018-09-23
mathjax: true
tag: [Virtual_Machine_Files]
categories: 0x00_Info-Forensic
---

가상머신 메모리 덤프를 뜨려면 어느정도 알아둬야 하는 가상머신 파일들이다.



> .vmss : 게스트 운영체제를 일시 중지(Suspend)상태로 변경할 때, 게스트 운영체제 상태를 저장한 파일

> .vmem : 가상머신의 메모리 정보를 저장한 파일이다. 게스트 운영체제에 대한 실질적인 가상 페이징 파일

> .log : 가상머신에 대한 일반적인 활동 기록 파일

> .vmdk : 게스트 운영체제에 대한 실질적인 가상 하드 드라이브

> .vmsn : 스냅샷 파일로, 게스트 운영체제에 대한 상태 저장

> .vmsd : 스냅샷 파일에 대한 메타데이터 기록 파일

> .nvram : 게스트 운영체제에 대한 바이오스 정보 기록 파일

> .vmx : 게스트 운영체제에 대한 설정 기록 파일