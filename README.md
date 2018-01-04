# Hadoop-Streaming
Implemented the below using Hadoop streaming with python.

Added simple test query
SELECT lo_quantity, SUM(lo_revenue)
FROM lineorder
WHERE lo_discount < 3
GROUP BY lo_quantity;
