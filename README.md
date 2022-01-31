# Whaling Server

## 소개
**[웨일링 홈페이지(Whaling)](https://whaling.co.kr)**

가상화폐 투표 서비스 웨일링의 Backend Server Repository입니다.

가상화폐 시세 기준 :  [Upbit](https://upbit.com/home)

## 기술 스택

### Infra

|Docker|Github Actions|
|:---:|:---:|
|<img src = "https://www.docker.com/sites/default/files/d8/2019-07/Moby-logo.png" width="50px" title="Docker"/>|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5e3891d9-f8c5-4e0a-bba0-01a7804a3ed7/44036562.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220131T144307Z&X-Amz-Expires=86400&X-Amz-Signature=dd3676a8f500ed4ce60eebae2a86ee901b1ee4d9b610988930c912b7def463f6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%2244036562.png%22&x-id=GetObject" width="50px" title="Github Actions"/>

### DataBase

|MySQL|RDS|S3|
|---|---|---|
|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/05d6790c-42bc-4e04-8401-cf7bca77b498/Amazon-RDS_MySQL_instance_light-bg4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145313Z&X-Amz-Expires=86400&X-Amz-Signature=429f9427facffc71c6d038989da9033fa2f8abf81685849a147148c8eb4b8e47&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Amazon-RDS_MySQL_instance_light-bg%25404x.png%22&x-id=GetObject" width="50px"  title= "MySQL"/>|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/74b76f22-b587-42af-b9af-3f3785ce4cdb/Amazon-RDS_Amazon-RDS_instance_light-bg4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145516Z&X-Amz-Expires=86400&X-Amz-Signature=e813299d120ec2e31d321dabe131e4befc228a9e0165cf85fe25b39ca69ae825&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Amazon-RDS_Amazon-RDS_instance_light-bg%25404x.png%22&x-id=GetObject" width="50px"  title="RDS"/>|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/17678404-159b-49d3-9fe2-f0c6701992c7/Amazon-Simple-Storage-Service-S3_Bucket-with-Objects_light-bg4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145600Z&X-Amz-Expires=86400&X-Amz-Signature=b881eb509a98b2f00f995e0dbeb54b8e1b1d0d47a48bdc50942a3c408a360b24&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Amazon-Simple-Storage-Service-S3_Bucket-with-Objects_light-bg%25404x.png%22&x-id=GetObject" width="50px"  title="S3" />

### Web Server

|EC2|ELB|Django|Nginx|gunicorn|
|---|---|---|---|---|
|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/12d9cdd2-bb95-4a6f-9c78-11fffab1def1/Amazon-EC24x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145706Z&X-Amz-Expires=86400&X-Amz-Signature=e83e7f6a3aff5bb8b528f5f169967fbf156266f7f3065284b98c1b77df6f3ae1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Amazon-EC2%25404x.png%22&x-id=GetObject" width="50px"  title="EC2" />|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/46674649-30fa-4de3-90bd-622784dffa80/Elastic-Load-Balancing-ELB_Application-load-balancer_light-bg4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145752Z&X-Amz-Expires=86400&X-Amz-Signature=d9dde558162d5c45d6454f5cb1e6a2038b71b5cdcb932828d65a7e35a6e3fe9d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Elastic-Load-Balancing-ELB_Application-load-balancer_light-bg%25404x.png%22&x-id=GetObject" width="50px"  title="ELB" />|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1ffb0fcd-aef1-4f33-afe0-29de68a1bb0b/django_original_logo_icon_146559.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150314Z&X-Amz-Expires=86400&X-Amz-Signature=d66642ec98dfa1597a5bfa87d82c85173a9d762da2699f4f8f05374c47512bcd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22django_original_logo_icon_146559.png%22&x-id=GetObject" width="50px"  title="Django" />|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b7c8a183-f394-4d27-8f2c-1fef602c2945/nginx.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150338Z&X-Amz-Expires=86400&X-Amz-Signature=d378c2cb7315d743544319229b9ef12888d187be2138154932c78ff21c038697&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22nginx.png%22&x-id=GetObject" width="50px"  title="Nginx" />|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4604d77c-c032-4556-a015-dcbb1fbad634/gunicorn_logo_icon_170045.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150410Z&X-Amz-Expires=86400&X-Amz-Signature=ddc96ba6009d44b1e5af1a96cdc9316a8e9d8a4693bc5724af703617c2ddbf0d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22gunicorn_logo_icon_170045.png%22&x-id=GetObject" width="70px"  title="gunicorn" />

### Tracking

|Celery|Redis|Upbit
|---|---|---|
|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/aa576cba-e5b9-4851-b852-6e3c17b3e833/pngwing.com.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150811Z&X-Amz-Expires=86400&X-Amz-Signature=9703d4590d101a7055eb16c4bdf1ef00787c98e208e4a3d1d9527e42aa3ea838&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22pngwing.com.png%22&x-id=GetObject" width="50px"  title="gunicorn" />|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7eeac880-db91-4344-9d0e-9813f58189ea/redis_plain_wordmark_logo_icon_146367.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150821Z&X-Amz-Expires=86400&X-Amz-Signature=2aa58fc0812a51cf3ee17432e21592b5dd7c5d6ba4f61c609ef5f6383a90817c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22redis_plain_wordmark_logo_icon_146367.png%22&x-id=GetObject" width="50px"  title="gunicorn" />|<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3775bfa6-7637-43ab-b9b3-876adbfd85bd/upbit.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T151416Z&X-Amz-Expires=86400&X-Amz-Signature=50fa3ccda61aecca3011c98ab0b56692be8b4c6414999199fa3d54eff0bbc7c2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22upbit.svg%22&x-id=GetObject" width="50px"  title="Upbit" />

## Feature

### API

추후 업뎃 예정

## Developer

|&nbsp;|정환우|권민아|
|:---:|:---:|:---:|
|역|코인 서버 구축</br>트래킹 기능 구현</br> 도메인 서버 배포|소셜 로그인</br>메인 서버 구축</br>API 서버 담당|
|Profile|Github Link: [sossont](https://github.com/sossont)| Github Link : [mingulmangul](https://github.com/mingulmangul)

