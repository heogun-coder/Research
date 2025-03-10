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
1. Hardware : **Raspberry Pi 5, Huawei E3372 USB LTE Modem, Alfa AWUS036ACH Wi-Fi Adapter**.
2. Software : Driver&Package Installation, Update in Rpi5
3. AWS Account Activation(Cognito, SES,..).

#### 2. Set Network And Test
- For 2 week
- Activity
1. Set Raspberry Pi 5 as an AP(Access Point) (using **hostapd**, **dnsmasq**).
2. Internet Connection Test with **Huawei E3372**.
3. Test Signal Power, Speed, Stability of wifi with **Alfa AWUS036ACH**.

#### 3. Build Captive Portal and User Authentication System 
- For 1 month
- Activity
1. Set captive Portal using **Apache** or **NGINX**.
2. Build User Database using **SQLite** or **MySQL**(or,,,, SQLAlchemy)
3. Embody User Authentication with **AWS Cognito**.
4. Enhance Security with **SSL/TLS**.

#### 4. Build Network Managiment System
- For 1 month
- Activity
1. Set Traffic Managin Rules with **Iptables** and **tc**.
2. Embody Priority and Connection disabling for Specific User.
3. Write Script for Integration of User Authentication and Network Management.

#### 5. 보안 이상 탐지 및 자동화 (19-24주차)
- For 1 month
- Activity
1. Set Rule for Detecting MITM, DDos with **Snort** or **Suricata** Installed.
2. Write Script for Automatic Execution when Anomaly Detected.
3. Adjust Security Rule and Test them.
