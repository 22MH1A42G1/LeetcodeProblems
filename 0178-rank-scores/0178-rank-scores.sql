# Write your MySQL query statement below
select s1.score, (
    select count(distinct s2.score) from scores s2 where s2.score >= s1.score
    ) as `RANK` from scores s1 order by s1.score desc;