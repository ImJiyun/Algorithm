-- 코드를 작성해주세요
# 실패 (1060, "Duplicate column name 'ID'")
# 처음 시도 : DIFFERENTIATION_DATE을 기준으로 세대를 구하려고 했음 
# WITH no_children AS (
#     SELECT
#         t1.ID,
#         t1.PARENT_ID,
#         t1.SIZE_OF_COLONY,
#         t1.DIFFERENTIATION_DATE
#     FROM 
#         ECOLI_DATA AS t1
#     LEFT JOIN 
#         ECOLI_DATA AS t2
#     ON
#         t1.ID = t2.PARENT_ID
#     WHERE
#         t2.ID IS NULL
# ), add_generation AS (
#     SELECT
#         DISTINCT DIFFERENTIATION_DATE,
#         DENSE_RANK() OVER (ORDER BY DIFFERENTIATION_DATE) AS generation
#     FROM
#         ECOLI_DATA
# )

# SELECT
#     COUNT(generation) AS COUNT, 
#     generation
# FROM (
#     SELECT 
#         generation, 
#         id
#     FROM 
#         no_children AS nc
#     LEFT JOIN 
#         add_generation AS ag
#     ON 
#         nc.DIFFERENTIATION_DATE = ag.DIFFERENTIATION_DATE
# ) AS t
# GROUP BY 
#     generation
# ORDER BY 
#     generation

# SELECT
#     ID,
#     PARENT_ID,
#     generation AS 1
# FROM 
#     ECOLI_DATA 
# WHERE
#     PARENT_ID IS NULL
    
# UNION ALL

# SELECT
#     ID,
#     PARENT_ID,
#     generation + 1
# FROM 
#     ECOLI_DATA AS t1
# LEFT JOIN 
#     ECOLI_DATA AS t2
# ON
#     t1.ID = t2.PARENT_ID

WITH RECURSIVE gen AS (
    -- 1세대(루트)
    SELECT
        id,
        parent_id,
        1 AS generation
    FROM ECOLI_DATA
    WHERE parent_id IS NULL

    UNION ALL

    -- 자식으로 내려가며 세대 +1
    SELECT
        c.id,
        c.parent_id,
        g.generation + 1
    FROM ECOLI_DATA c
    JOIN gen g
      ON c.parent_id = g.id
),
leaf AS (
    -- 자식이 없는 개체(leaf)
    SELECT g.id, g.generation
    FROM gen g
    LEFT JOIN ECOLI_DATA ch
      ON ch.parent_id = g.id
    WHERE ch.id IS NULL
)
SELECT
    COUNT(*) AS COUNT,
    generation
FROM leaf
GROUP BY generation
ORDER BY generation;