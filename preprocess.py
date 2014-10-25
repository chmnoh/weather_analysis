#!/usr/bin/python
# -*- encoding: latin-1 -*-

# convert multi-line "REMARK" field into single line.

fp_in = open('data/StormDB.csv', 'rb')
fp_out = open('data/StormDB2.csv', 'w')

nrow = 0
for l in fp_in: # header
	fp_out.write(l)
	nrow += 1
	break

cnt = 0
buf = []
for l in fp_in:
	line = ""
	#print repr(l[-5:])
	if l[-5:] == ".00\r\n":
		if len(buf) > 0:
			buf.append(l)
			line = ''.join(buf)
			buf = []
			#print "merged line: ", line
		else:
			line = l
	else:
		if len(buf) == 0:
			cnt += 1
			#print nrow, "fail"
		buf.append(l.replace("\r","").replace("\n",""))
		continue
	fp_out.write(line)
	nrow += 1
	#if nrow > 10:
		#break

fp_in.close()
fp_out.close()

print "total failed line: %d/%d" % (cnt,nrow)
