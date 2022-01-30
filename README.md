# Whaling Server

가상화폐 투표 서비스 웨일링의 백엔드 서버입니다. 가상화폐 시세 기준은 [Upbit](https://upbit.com/home) 입니다.

# 기술 스택

### Infra

|Docker|Github Actions|
|---|---|
|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/30f0f63b-c694-4b32-b2d8-7ab2468a9374/docker.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150641Z&X-Amz-Expires=86400&X-Amz-Signature=9f741701b635150719440df58d6e639fdde4861002f68f87933027f76f7636e3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22docker.png%22&x-id=GetObject" width="50px" height="50px" title= "Docker"/></p>|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fcfbd392-1dca-44d7-b7be-69e6c731d77c/github_actions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150726Z&X-Amz-Expires=86400&X-Amz-Signature=1d361f61aca12b61cc5900c42896c57d3d25822f06e830a771ee5a9da4393ee5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22github%2520actions.png%22&x-id=GetObject" width="50px" height="50px" title= "Github Actions"/></p>|

### DataBase

|MySQL|RDS|S3|
|---|---|---|
|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/05d6790c-42bc-4e04-8401-cf7bca77b498/Amazon-RDS_MySQL_instance_light-bg4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145313Z&X-Amz-Expires=86400&X-Amz-Signature=429f9427facffc71c6d038989da9033fa2f8abf81685849a147148c8eb4b8e47&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Amazon-RDS_MySQL_instance_light-bg%25404x.png%22&x-id=GetObject" width="50px" height="50px" title= "MySQL"/>|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/74b76f22-b587-42af-b9af-3f3785ce4cdb/Amazon-RDS_Amazon-RDS_instance_light-bg4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145516Z&X-Amz-Expires=86400&X-Amz-Signature=e813299d120ec2e31d321dabe131e4befc228a9e0165cf85fe25b39ca69ae825&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Amazon-RDS_Amazon-RDS_instance_light-bg%25404x.png%22&x-id=GetObject" width="50px" height="50px" title="RDS"/>|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/17678404-159b-49d3-9fe2-f0c6701992c7/Amazon-Simple-Storage-Service-S3_Bucket-with-Objects_light-bg4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145600Z&X-Amz-Expires=86400&X-Amz-Signature=b881eb509a98b2f00f995e0dbeb54b8e1b1d0d47a48bdc50942a3c408a360b24&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Amazon-Simple-Storage-Service-S3_Bucket-with-Objects_light-bg%25404x.png%22&x-id=GetObject" width="50px" height="50px" title="S3" />

### Web Server

|EC2|ELB|Django|Nginx|gunicorn|
|---|---|---|---|---|
|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/12d9cdd2-bb95-4a6f-9c78-11fffab1def1/Amazon-EC24x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145706Z&X-Amz-Expires=86400&X-Amz-Signature=e83e7f6a3aff5bb8b528f5f169967fbf156266f7f3065284b98c1b77df6f3ae1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Amazon-EC2%25404x.png%22&x-id=GetObject" width="50px" height="50px" title="EC2" />|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/46674649-30fa-4de3-90bd-622784dffa80/Elastic-Load-Balancing-ELB_Application-load-balancer_light-bg4x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T145752Z&X-Amz-Expires=86400&X-Amz-Signature=d9dde558162d5c45d6454f5cb1e6a2038b71b5cdcb932828d65a7e35a6e3fe9d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Elastic-Load-Balancing-ELB_Application-load-balancer_light-bg%25404x.png%22&x-id=GetObject" width="50px" height="50px" title="ELB" />|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1ffb0fcd-aef1-4f33-afe0-29de68a1bb0b/django_original_logo_icon_146559.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150314Z&X-Amz-Expires=86400&X-Amz-Signature=d66642ec98dfa1597a5bfa87d82c85173a9d762da2699f4f8f05374c47512bcd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22django_original_logo_icon_146559.png%22&x-id=GetObject" width="50px" height="50px" title="Django" />|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b7c8a183-f394-4d27-8f2c-1fef602c2945/nginx.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150338Z&X-Amz-Expires=86400&X-Amz-Signature=d378c2cb7315d743544319229b9ef12888d187be2138154932c78ff21c038697&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22nginx.png%22&x-id=GetObject" width="50px" height="50px" title="Nginx" />|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4604d77c-c032-4556-a015-dcbb1fbad634/gunicorn_logo_icon_170045.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150410Z&X-Amz-Expires=86400&X-Amz-Signature=ddc96ba6009d44b1e5af1a96cdc9316a8e9d8a4693bc5724af703617c2ddbf0d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22gunicorn_logo_icon_170045.png%22&x-id=GetObject" width="50px" height="50px" title="gunicorn" />

### Tracking

|Celery|Redis|Upbit
|---|---|---|
|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/aa576cba-e5b9-4851-b852-6e3c17b3e833/pngwing.com.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150811Z&X-Amz-Expires=86400&X-Amz-Signature=9703d4590d101a7055eb16c4bdf1ef00787c98e208e4a3d1d9527e42aa3ea838&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22pngwing.com.png%22&x-id=GetObject" width="50px" height="50px" title="gunicorn" />|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7eeac880-db91-4344-9d0e-9813f58189ea/redis_plain_wordmark_logo_icon_146367.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T150821Z&X-Amz-Expires=86400&X-Amz-Signature=2aa58fc0812a51cf3ee17432e21592b5dd7c5d6ba4f61c609ef5f6383a90817c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22redis_plain_wordmark_logo_icon_146367.png%22&x-id=GetObject" width="50px" height="50px" title="gunicorn" />|<p align="center"><img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3775bfa6-7637-43ab-b9b3-876adbfd85bd/upbit.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220130T151416Z&X-Amz-Expires=86400&X-Amz-Signature=50fa3ccda61aecca3011c98ab0b56692be8b4c6414999199fa3d54eff0bbc7c2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22upbit.svg%22&x-id=GetObject" width="50px" height="50px" title="Upbit" />