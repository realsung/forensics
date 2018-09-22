---
layout: post
title: PNG 구조(Structure)
date: 2018-09-18
mathjax: true
tag: [PNG, PNGSignature, PNGStructure, PNG구조]
categories: 0x00_Info-Forensic
---

### PNG File Signature

`89 50 4E 47 0D 0A 1A 0A` : ‰PNG....

PNG 파일은 8Bytes의 시그니처를 가진다.

그 뒤에는 Chunk라는 그룹으로 나뉘어져 이미지 정보가 저장된다.

### PNG Chunk

`IHDR Chunk : 이미지 헤더 정보(첫 번째 청크)`

`PLTE Chunk : 팔레트 테이블 정보(색공간 표시)`

`IDAT Chunk : 이미지 데이터 정보(IDAT 청크로 쪼개질 수 있는 이미지 테이터 정보 표시)`

`IEND Chunk : 이미지 트레일러 정보(이미지의 끝을 표시)`

#### IHDR
`IHDR` 청크는 PNG 파일 맨 앞에 위치하는 청크로, PNG 이미지의 크기, 필터링 방식, 압축 방식 등을 알 수 있다.
IHDR은 항상 13바이트이다.
```
{
 Length : 00 00 00 0D (13 byte),
 Chunk Type : IHDR,
 Chunk Data ( 13 byte ),
 {
   Width (4 byte),
   Height (4 byte),
   Bit depth (1 byte),
   Color Type (1 byte),
   Compression method (1 byte),
   Filter method (1 byte),
   Interlace method (1 byte),
 }
 CRC
}
```
#### Width, Height

이미지의 폭과 높이를 지정한다. 이 값을 바탕으로 이미지 데이터를 디코딩하고 출력한다. 따라서 이 부분을 조작하면 이미지를 일그러뜨리거나 이미지의 아랫부분을 감추는 것 등도 가능하다.

#### Bit depth

Bit depth 하나의 채널(channel)이 몇 비트로 구성될 지를 정한다. 이미지의 한 픽셀은 하나 또는 여러개의 채널로 구성될 수 있다.

#### Color Type

Color Type은 PNG 이미지의 색상을 어떻게 구성할 것인지를 정한다.

#### Compression method

PNG 압축 표준 : Deflate

#### Filter method

현재까지 PNG에서 표준으로 정의된 필터링 방식은 한 가지다.

#### Interlace method

웹 페이지 등에 이미지를 표시할 때 이미지 로딩이 완료되기 전에 먼저 해상도가 낮은 이미지를 보여주기 위하여 사용된다.

#### IDAT

`IDAT`청크는 이미지의 실제 데이터가 들어가는 부분이고, 픽셀 데이터는 필터링과 압축을 거쳐 IDAT청크에 저장된다. 한 PNG는 여러 IDAT 청크를 가지는데, 이는 데이터를 적절한 사이즈로 전송하기 위한 것이다. 일반적으로 하나의 IDAT 청크당 65534바이트의 크기를 갖는다. 그래서 PNG는 전체 이미지 데이터를 한꺼번에 압축한 뒤, 여러 IDAT 청크에 나누어 담는 방식을 사용한다. 따라서, 모든 IDAT 청크가 있어야만 이미지 디코딩이 가능하다.

```
Encoding : Pixel Data -> Filter -> Compression -> IDAT Chunk Data
Decofing : IDAT Chunk Data -> Compression -> Unfilter -> Pixel Data
```

#### IEND

`IEND`청크는 이미지의 맨 뒤에 위치하는 청크로 PNG 파일의 끝을 나타낸다. 데이터를 담는 목적으로 사용되지 않으므로 길이는 항상 0이다.

##### Footer Signature, Trailer Signature
`49 45 4E 44 AE 42 60 82` : IEND®B`‚


![Image](https://user-images.githubusercontent.com/32904385/45670907-8c743980-bb13-11e8-9753-22b8fea28629.png)

## Comments

{% include comments.html %}