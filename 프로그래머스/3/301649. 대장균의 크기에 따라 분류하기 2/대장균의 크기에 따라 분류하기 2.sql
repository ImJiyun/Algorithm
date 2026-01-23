-- 코드를 작성해주세요
# SELECT
#     e.ID,
#     CASE 
#         WHEN e.percent <= 0.25 THEN 'CRITICAL'
#         WHEN e.percent <= 0.5 THEN 'HIGH'
#         WHEN e.percent <= 0.75 THEN 'MEDIUM'
#         ELSE 'LOW'
#     END AS COLONY_NAME
# FROM
#     (SELECT
#         ID,
#         percent_rank() OVER (ORDER BY SIZE_OF_COLONY DESC) as percent
#      FROM
#         ECOLI_DATA 
#     ) e
# ORDER BY
#     e.ID

WITH size_rank_table AS (
    SELECT
        *,
        PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS size_rank
    FROM
        ECOLI_DATA 
)

SELECT
    ID,
    CASE 
        WHEN size_rank <= 0.25 THEN 'CRITICAL'
        WHEN size_rank <= 0.5 THEN 'HIGH'
        WHEN size_rank <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM
    size_rank_table
ORDER BY
    ID