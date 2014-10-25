#!/usr/bin/python
# -*- encoding: utf-8 -*-

# convert multi-line "REMARK" field into single line.

fp_in = open('data/StormDB-unzipped.csv', 'rb')
fp_out = open('data/StormDB.csv', 'wb')

nrow = 0
for l in fp_in: # header
	fp_out.write(l.replace("\r",""))
	nrow += 1
	break

cnt = 0
buf = []
line_no = 2
for line in fp_in:
	last_elem = line.split(',')[-1].strip().split('.')
	if len(last_elem) == 2 and last_elem[0].isalnum() and last_elem[1] == '00':
		nrow += 1
		data = ""
		if len(buf) == 0:
			data = line
		else:
			buf.append(line)
			data = ''.join(buf)
			buf = []
		fp_out.write(data.replace("\r","").replace('""',''))
	else:
		if len(buf) == 0:
			cnt += 1
		buf.append(line.strip())
		#if cnt % 1000 == 0:
		#	print line_no, "fmt err (%d)" % nrow
	line_no += 1

fp_in.close()
fp_out.close()

#print "total format error line: %d/%d" % (cnt,nrow)
