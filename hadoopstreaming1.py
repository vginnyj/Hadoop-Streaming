
#!/usr/bin/python
#mapper
import sys
for line in sys.stdin:
    line = line.strip()
    vals = line.split('|')
    if int(vals[11]) < 3: # lo_discount
        redin1 = vals[8] # lo_quantity
        redin2 = vals[12] # lo_revenue
        print '\t'.join([redin1,redin2])


#!/usr/bin/python
#reducer
import sys
current_key = None
current_sum = 0
key = None
for line in sys.stdin:
    split = line.strip().split('\t')
    key = split[0]
    value =int(split[1])
    if current_key == key:
        current_sum += value
    else:
	if current_key:
            print '%s\t%s' % (current_key, current_sum)
        current_key = key
        current_sum = value
if current_key == key:
print '%s\t%s' % (current_key, current_sum)
