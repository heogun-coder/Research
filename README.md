# Research

## This is a Research program for JSHS Graduation Article
### 1. Summary

#### This project aims to build an autonomous network using a wireless access point based on a Raspberry Pi 5 running Kali Linux, along with a USB LTE Modem and an Alfa AWUS036ACH Wi-Fi adapter. The network includes:

##### 1. A Captive Portal for user authentication integrated with a database, secured with SSL/TLS.
##### 2. User network connection management, allowing traffic prioritization and forced disconnections.
##### 3. Security anomaly detection for MITM and DDoS attacks, with automated network management responses.
##### 4. The setup involves configuring hostapd for the access point, setting up a web server for the captive portal, managing user traffic with firewall rules and QoS, and using intrusion detection systems for security.

### 2. Expected Pricing

#### - Alfa AWUS036ACH Wi-Fi Adapter: Rokland / $49.99
#### - Huawei E3372 USB LTE Modem: Amazon / $69.99
#### - AWS 서비스: AWS는 사용량에 따라 비용이 청구되는 구조입니다. 예를 들어:
1. EC2 인스턴스 (t2.micro): 시간당 $0.0116
2. S3 스토리지: GB당 $0.023
3. Cognito (사용자 인증): 월 50,000 MAU(월간 활성 사용자)까지 무료

### 3. Project Roadmap
#### 1. Prepare Hardware and Software
- For 1 week
- Activity
- 1). Hardware : **Raspberry Pi 5, Huawei E3372 USB LTE Modem, Alfa AWUS036ACH Wi-Fi Adapter**.
  2). Software : Driver&Package Installation, Update in Rpi5
  3). AWS Account Activation(Cognito, SES,..).

#### 2. Set Network And Test
- For 2 week
- Activity
- 1). Set Raspberry Pi 5 as an AP(Access Point) (using **hostapd**, **dnsmasq**).
  2). Internet Connection Test with **Huawei E3372**.
  3). Test Signal Power, Speed, Stability of wifi with **Alfa AWUS036ACH**.

#### 3. Build Captive Portal and User Authentication System 
- For 1 month
- Activity
- 1. Set captive Portal using **Apache** or **NGINX**.
  2. Build User Database using **SQLite** or **MySQL**(or,,,, SQLAlchemy)
  3. Embody User Authentication with **AWS Cognito**.
  4. Enhance Security with **SSL/TLS**.

#### 4. Build Network Managin System
- For 1 month
활동:
iptables와 tc로 트래픽 관리 규칙 설정.
특정 사용자에 대한 트래픽 우선순위 부여 및 연결 해제 기능 구현.
사용자 인증과 네트워크 관리 기능을 통합하는 스크립트 작성.
성과물: 네트워크 관리 기능이 통합된 시스템.

#### 5. 보안 이상 탐지 및 자동화 (19-24주차)
기간: 6주 (12시간)
활동:
Snort 또는 Suricata 설치 및 MITM/DDoS 탐지 규칙 설정.
이상 탐지 시 자동 네트워크 관리 조치 스크립트 작성.
보안 기능 테스트 및 규칙 조정.
성과물: 보안 이상 탐지 및 대응 시스템.

#### 6. 통합 및 테스트 (25-30주차)
기간: 6주 (12시간)
활동:
모든 구성 요소(인증, 관리, 보안)를 통합하여 시스템 점검.
종합 테스트(사용자 인증, 네트워크 관리, 보안 기능).
실제 사용자 환경 시뮬레이션으로 성능 및 안정성 검증.
성과물: 통합된 전체 시스템.

#### 7. 문서화 및 발표 준비 (31-36주차)
기간: 6주 (12시간)
활동:
진행 과정, 구현 방법, 테스트 결과 문서화.
GitHub Readme.md 작성(프로젝트 소개 및 사용법 포함).
발표 준비 및 데모 시연 계획.
성과물: 프로젝트 문서 및 발표 자료.

#### 8. 최종 검토 및 마무리 (37-40주차)
기간: 4주 (8시간)
활동:
목표 달성 여부 검토 및 미비점 보완.
사용자 피드백 수집 및 시스템 개선.
유지보수 계획 수립.
성과물: 최종 완성된 시스템.

#### 9. 프로젝트 회고 및 평가 (41-42주차)
기간: 2주 (4시간)
활동:
성공 요인 및 개선점 분석.
팀원들과 회고 및 배운 점 공유.
성과 평가 및 다음 프로젝트 교훈 도출.
성과물: 회고 보고서.

