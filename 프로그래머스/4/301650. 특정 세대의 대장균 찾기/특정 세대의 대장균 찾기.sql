-- 코드를 작성해주세요
# SELECT 
#     F.ID
# FROM 
#     ECOLI_DATA F
# JOIN 
#     ECOLI_DATA S
# ON 
#     F.PARENT_ID = S.ID
# JOIN
#     ECOLI_DATA T
# ON 
#     S.PARENT_ID = T.ID
# WHERE
#     T.PARENT_ID IS NULL
# ORDER BY
#     F.ID

# SELECT
#     *
# FROM
#     ECOLI_DATA AS g1
# JOIN
#     ECOLI_DATA AS g2
# ON
#     g1.PARENT_ID = g2.ID
# JOIN
#     ECOLI_DATA AS g3
# ON
#     g2.PARENT_ID = g3.ID



SELECT
    g3.ID
FROM
    ECOLI_DATA AS g1
JOIN
    ECOLI_DATA AS g2
ON
    g1.ID = g2.PARENT_ID
JOIN
    ECOLI_DATA AS g3
ON
    g2.ID = g3.PARENT_ID
WHERE
    g1.PARENT_ID IS NULL
ORDER BY
    g3.ID
    