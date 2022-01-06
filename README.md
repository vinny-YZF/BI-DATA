select level,time,count(*),count(*)/count(level)  from test7 group by level,time;

create table hosts(id int(32),name varchar(255),host varchar(255));


insert into hosts (id,name,host) values ("1","E站主站","example.com"),("2","E站主站","www.example.com"),("3","E站论坛","bbs.example.com");



select time,func,level ,message, plateform, uid, host, uri 
from test6

select time(date,'%Y-%m-%d') func,level ,message, plateform, uid, host, uri from test6 

SELECT distinct(DATE_FORMAT(time,'%Y-%m-%d')) FROM test6;

--数据清洗
insert into test7 select DATE_FORMAT(time,'%Y-%m-%d'),func,level,message,plateform,uid,host,uri from test6;

--严重程度随时间变化率
select
a.time,a.level,rate1 / rate2
from 
(select level ,time,count(*) rate1  from test7 group by level,time) a 
join
(SELECT time ,count(*) rate2 FROM test7 group by time) b 
on a.time = b.time;

--用户渠道随时间变化率
select
a.time,a.plateform,rate1 / rate2
from 
(select plateform ,time,count(*) rate1  from test7 group by plateform,time) a 
join
(SELECT time ,count(*) rate2 FROM test7 group by time) b 
on a.time = b.time;


--用户域名渠道随时间变化率
select
a.time,a.host,rate1 / rate2,c.name
from 
(select host ,time,count(*) rate1  from test7 group by host,time) a 
join
(select time ,count(*) rate2 FROM test7 group by time) b 
on a.time = b.time
join
hosts c
on 
a.host = c.host

