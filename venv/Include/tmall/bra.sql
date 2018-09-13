CREATE TABLE `bra` (
`bra_id`  int(11) NOT NULL AUTO_INCREMENT COMMENT 'id' ,
`bra_color`  varchar(25) NULL COMMENT '颜色' ,
`bra_size`  varchar(25) NULL COMMENT '罩杯' ,
`resource`  varchar(25) NULL COMMENT '数据来源' ,
`comment`  varchar(500) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '评论' ,
`comment_time`  datetime NULL COMMENT '评论时间' ,
PRIMARY KEY (`bra_id`)
) character set utf8
;

update bra set bra_color = REPLACE(bra_color,'2B6521-无钢圈4-','');
update bra set bra_color = REPLACE(bra_color,'-1','');
update bra set bra_color = REPLACE(bra_color,'5','');
update bra set bra_size = substr(bra_size,1,3);

select 'A' as 罩杯, CONCAT(ROUND(COUNT(*)/(select count(*) from bra) * 100, 2) , "%") as 比例, COUNT(*) as 销量  from bra where bra_size like '%A'
union all select 'B' as 罩杯, CONCAT(ROUND(COUNT(*)/(select count(*) from bra) * 100, 2) , "%") as 比例, COUNT(*) as 销量  from bra where bra_size like '%B'
union all select 'C' as 罩杯, CONCAT(ROUND(COUNT(*)/(select count(*) from bra) * 100, 2) , "%") as 比例, COUNT(*) as 销量  from bra where bra_size like '%C'
union all select 'D' as 罩杯, CONCAT(ROUND(COUNT(*)/(select count(*) from bra) * 100, 2) , "%") as 比例, COUNT(*) as 销量  from bra where bra_size like '%D'
union all select 'E' as 罩杯, CONCAT(ROUND(COUNT(*)/(select count(*) from bra) * 100, 2) , "%") as 比例, COUNT(*) as 销量  from bra where bra_size like '%E'
union all select 'F' as 罩杯, CONCAT(ROUND(COUNT(*)/(select count(*) from bra) * 100, 2) , "%") as 比例, COUNT(*) as 销量  from bra where bra_size like '%F'
union all select 'G' as 罩杯, CONCAT(ROUND(COUNT(*)/(select count(*) from bra) * 100, 2) , "%") as 比例, COUNT(*) as 销量  from bra where bra_size like '%G'
union all select 'H' as 罩杯, CONCAT(ROUND(COUNT(*)/(select count(*) from bra) * 100, 2) , "%") as 比例, COUNT(*) as 销量  from bra where bra_size like '%H'
order by 销量 desc;