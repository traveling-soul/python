启动项目
1、启动fdfs分布式系统
sudo /usr/bin/restart.sh /usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf
sudo /usr/bin/restart.sh /usr/bin/fdfs_storaged /etc/fdfs/storage.conf

2、redis服务器启动，存储购物车相关信息
sudo redis-server /etc/redis/redis.conf

3、进入django项目目录

4、启动nginx服务器，监听fdfs接口和uwsgi接口
sudo /usr/local/nginx/sbin/nginx

5、启动uwsgi服务器
uwsgi --ini uwsgi.ini

6、浏览器输入网址
