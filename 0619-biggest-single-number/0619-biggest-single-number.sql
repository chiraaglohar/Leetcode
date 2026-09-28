select max(num) as num
from mynumbers
where num in (
    select *
    from mynumbers
    group by num
    having count(*) = 1
)
