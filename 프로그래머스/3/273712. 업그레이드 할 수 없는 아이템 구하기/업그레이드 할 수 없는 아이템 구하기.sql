-- 코드를 작성해주세요
# SELECT
#     ITEM_ID
# FROM
#     ITEM_TREE
# WHERE
#     ITEM_ID NOT IN (
#         SELECT
#             PARENT_ITEM_ID
#         FROM
#             ITEM_TREE 
#         GROUP BY
#             PARENT_ITEM_ID
#     )

SELECT
    ii.ITEM_ID,
    ii.ITEM_NAME,
    ii.RARITY
FROM
    ITEM_INFO AS ii
LEFT JOIN
    ITEM_TREE AS it
ON 
    ii.ITEM_ID = it.PARENT_ITEM_ID
WHERE
    it.ITEM_ID IS NULL
ORDER BY
    ii.ITEM_ID DESC