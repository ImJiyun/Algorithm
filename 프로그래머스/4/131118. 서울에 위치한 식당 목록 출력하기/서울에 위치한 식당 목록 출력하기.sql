-- 코드를 입력하세요
# SELECT 
#     ri.rest_id, 
#     ri.rest_name, 
#     ri.food_type, 
#     ri.favorites, 
#     ri.address, 
#     ROUND(AVG(rr.review_score), 2) AS score
# FROM 
#     rest_info ri
# JOIN 
#     rest_review rr ON ri.rest_id = rr.rest_id
# WHERE 
#     ri.address LIKE '서울%'
# GROUP BY 
#     ri.rest_id, ri.rest_name, ri.food_type, ri.address
# ORDER BY 
#     score DESC, ri.favorites DESC;


SELECT
    ri.REST_ID,
    ri.REST_NAME,
    ri.FOOD_TYPE,
    ri.FAVORITES,
    ri.ADDRESS,
    ROUND(AVG(rr.REVIEW_SCORE), 2) AS SCORE
FROM
    REST_INFO AS ri
JOIN
    REST_REVIEW AS rr
ON
    ri.REST_ID = rr.REST_ID
WHERE
    ADDRESS LIKE "서울%"
GROUP BY
    ri.REST_ID
ORDER BY
    SCORE DESC,
    FAVORITES DESC