-- 코드를 입력하세요
# WITH rank_table AS (
#     SELECT 
#         *,
#         DENSE_RANK() OVER (ORDER BY review_cnt DESC) AS review_rank
#     FROM (
#         SELECT
#             MEMBER_ID,
#             COUNT(MEMBER_ID) AS review_cnt
#         FROM
#             REST_REVIEW 
#         GROUP BY
#             MEMBER_ID
#     ) AS tmp
# )

# SELECT 
#     mp.MEMBER_NAME,
#     r.REVIEW_TEXT,
#     DATE_FORMAT(r.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
# FROM
#     MEMBER_PROFILE AS mp
# LEFT JOIN 
#     REST_REVIEW  AS r
# ON 
#     mp.MEMBER_ID = r.MEMBER_ID
# WHERE
#     mp.MEMBER_ID IN (
#         SELECT
#             MEMBER_ID
#         FROM
#             rank_table
#         WHERE
#             review_rank = 1
#     )
# ORDER BY
#     REVIEW_DATE,
#     REVIEW_TEXT

# SELECT
#     MEMBER_NAME,
#     REVIEW_TEXT,
#     DATE_FORMAT(REVIEW_DATE,"%Y-%m-%d") AS REVIEW_DATE,
#     CNT
# FROM(
#     SELECT
#         MEMBER_NAME,
#         REVIEW_TEXT,
#         REVIEW_DATE,
#         COUNT(MEMBER_ID) OVER(PARTITION BY MEMBER_ID) AS CNT
#     FROM REST_REVIEW AS R
#     LEFT JOIN MEMBER_PROFILE AS M
#     USING (MEMBER_ID)
#     ORDER BY
#         CNT DESC        
# ) AS BASE
# WHERE CNT = (SELECT 
#                 COUNT(MEMBER_ID)
#             FROM 
#                 REST_REVIEW)

 SELECT
    m.MEMBER_NAME,
    r.REVIEW_TEXT,
    DATE_FORMAT(r.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW r
JOIN MEMBER_PROFILE m
  ON r.MEMBER_ID = m.MEMBER_ID
WHERE r.MEMBER_ID IN (
    SELECT member_id
    FROM REST_REVIEW
    GROUP BY member_id
    HAVING COUNT(*) = (
        SELECT MAX(cnt)
        FROM (
            SELECT COUNT(*) AS cnt
            FROM REST_REVIEW
            GROUP BY member_id
        ) t
    )
)
ORDER BY r.REVIEW_DATE, r.REVIEW_TEXT;
