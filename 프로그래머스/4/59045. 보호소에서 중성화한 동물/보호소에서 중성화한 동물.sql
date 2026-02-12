-- 코드를 입력하세요
# SELECT
#     i.ANIMAL_ID,
#     i.ANIMAL_TYPE,
#     i.NAME
# FROM 
#     ANIMAL_INS i
# JOIN 
#     ANIMAL_OUTS o
# ON 
#     i.ANIMAL_ID = o.ANIMAL_ID
# WHERE 
#     SEX_UPON_INTAKE LIKE 'Intact%' AND 
#     SEX_UPON_OUTCOME NOT LIKE 'Intact%'

# Intact : 중성화 X
SELECT
    ai.ANIMAL_ID,
    ai.ANIMAL_TYPE,
    ai.NAME
FROM
    ANIMAL_INS AS ai
LEFT JOIN
    ANIMAL_OUTS AS ao
ON
    ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE
    ai.SEX_UPON_INTAKE LIKE '%Intact%'
    AND
    ao.SEX_UPON_OUTCOME NOT LIKE '%Intact%'