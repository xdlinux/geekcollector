import sys

def usage():
    print "Usage:tasc2dot.py [output_path] [color_list] [color_1] [[color_2] ...]\n"
    print "color-list:"
    print "\td: Dark blue"
    print "\tb: Blue"
    print "\tg: Green"
    print "\tr: Red"
    print "\tl: Light green"
    print "\tt: Brown"
    print "\ty: Yellow"
    print "\th: Blue black"
    print "\to: Orange"
    print "\ts: Sky blue"
    print "\td: Light blue"
    print "\tc: Gray"
    print "\ti: Light gray"
    print "\tw: Dark white"
    print "\tz: black"
    print "\nshanzi Copyright 2011\n" 
    return

def main(output,asc,flist):
    count=0
    out=[]
    outp=[]
    for filename in flist:
        f=open(filename)
        fs=f.read()
        f.close()
        if (len(asc)<len(flist)):
            print 'Error:\n\tLength of color_list is short than number of colors.\n'
            return usage()
        if(len(out)==0):
            out=list(' '*len(fs))
        for i in range(len(out)):
            if(not fs[i] in ' \n'):
                out[i]=asc[count]
        count+=1
        if count>7:
            break
    for i in range(len(out)):
        if(out[i] !=' '):
            try:
                outp.append('[%d,%d,%d]'% (i%(41),i/(41),'dbgrltyhosjciwz'.index(out[i])))
            except:
                print 'Error:\n\rUnexpect char "%s"\n ' % out[i]
                return usage()
    f=open(output,'w')
    f.write('{"grid":{"incr":15,"size":40},"dots":[')
    f.write(','.join(outp))
    f.write(']},\n')
    f.close()
    return

if (len(sys.argv)<2 or sys.argv[1]=='help'):
    usage()
elif(len(sys.argv)<3):
    print "Not Enough arguments\nUsage:\n\tasc2dot.py [output_path] [color_list] [color_1] [[color_2] ...]\n"
    usage()
else:
    main(sys.argv[1],sys.argv[2],sys.argv[3:])

