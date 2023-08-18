# 1. How many bus routes exist in Chicago?
# 2. How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?
# 3. What is the total number of rides taken on each bus route?
# 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

# 1.
len({s['route'] for s in rows})
# 181

# 2
[s['rides'] for s in rows if (s['route'] == '22' and s['date'] == '02/02/2011')][0]
# 5055

#3
for s in rows:
    totals[s['route']] += s['rides']

#4

