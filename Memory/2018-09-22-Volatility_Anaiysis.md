---
layout: post
title: Volatility Memory Analysis 1
date: 2018-09-22
mathjax: true
tag: [Volatility, MemoryAnalysis]
categories: 0x01_MemoryForensic
---

Volatility를 이용해서 자주 사용하는 명령어들을 사용해 vmss 이미지 파일을 분석할 것이다.

GrrCON CTF 2015에 메모리 포렌식 문제로 나왔던 이미지 파일을 분석할 것이다.

![vol1](https://user-images.githubusercontent.com/32904385/45915391-89df5000-be43-11e8-9c90-c8b429c43d25.png)

> $ vol.py -f [분석할 이미지(vmem, raw)] image info

Target1-1dd8701f.vmss 메모리 덤프에 대한 이미지 정보를 나타내는 명령어이다.

imageinfo 플러그인에서 중요한 정보는 Suggested Profile(s)의 정보가 중요하고 분석하는데 필요하다.

이 메모리 덤프는 Win7SP1x86_23418, Win7SP0x86, Win7SP1x86이다.



![vol2](https://user-images.githubusercontent.com/32904385/45915488-16d6d900-be45-11e8-9180-d8fac9b91928.png)

> $ vol.py -f [분석할 이미지] --profile=[imageinfo의 Profile 값] pslist

> $ vol.py -f [분석할 이미지] --profile=[imageinfo의 Profile 값] splits > analysis_memory.txt

위에는 일반적으로 터미널에서 출력할 수 있는 반면에 아래와 같이 "> analysis_memory.txt"를 이용해 따로 txt 파일로 만들 수 있다.

 pslist는 시스템의 프로세스들을 보여주기 위해 사용된다.

차례대로 오프셋, 프로세스 이름, PID, 부모 프로세스, 쓰레드 수, 핸들 수, 프로세스 시작과 종료 시간이 있다.

> PID

PID(Process Identification Number)는 프로세스 각각을 구별할 수 있는 유일한 데이터이다.

> PPID

PPID(Parent Process Identification Number)는 프로세스를 만든 부모 프로세스 PID를 나타내는 값이다.

쉘 프롬포트에서 명령어를 입력해 프로그램을 실행하면 쉘이 부모 프로세스가 되어 쉘의 PID가 프로세스의 PPID로 할당된다.



![vol3](https://user-images.githubusercontent.com/32904385/45919718-7e167c80-be89-11e8-9d67-ba85c3a31535.png)

pstree는 프로세스를 트리 형태로 출력하기 위해 사용한다. p





참고 문헌 : [Ahnlab Forensic](https://www.ahnlab.com/kr/site/securityinfo/secunews/secuNewsView.do?seq=22109)



## Comments

{% include comments.html %}