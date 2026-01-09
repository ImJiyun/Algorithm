-- 코드를 입력하세요
WITH rank_table AS (
    SELECT 
        *,
        DENSE_RANK() OVER (ORDER BY review_cnt DESC) AS review_rank
    FROM (
        SELECT
            MEMBER_ID,
            COUNT(MEMBER_ID) AS review_cnt
        FROM
            REST_REVIEW 
        GROUP BY
            MEMBER_ID
    ) AS tmp
)

SELECT 
    mp.MEMBER_NAME,
    r.REVIEW_TEXT,
    DATE_FORMAT(r.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM
    MEMBER_PROFILE AS mp
LEFT JOIN 
    REST_REVIEW  AS r
ON 
    mp.MEMBER_ID = r.MEMBER_ID
WHERE
    mp.MEMBER_ID IN (
        SELECT
            MEMBER_ID
        FROM
            rank_table
        WHERE
            review_rank = 1
    )
ORDER BY
    REVIEW_DATE,
    REVIEW_TEXT