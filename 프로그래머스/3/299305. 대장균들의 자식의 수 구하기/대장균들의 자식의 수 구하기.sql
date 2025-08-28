# SELECT parent.id, 
#        COUNT(child.id) child_count
# FROM ecoli_data parent
# LEFT JOIN ecoli_data child 
# ON parent.id = child.parent_id
# GROUP BY parent.id
# ORDER BY parent.id ASC

SELECT 
    ID,
    (SELECT COUNT(*) 
     FROM ECOLI_DATA child 
     WHERE child.PARENT_ID = parent.ID) AS CHILD_COUNT
FROM ECOLI_DATA parent
ORDER BY ID;