import easyocr
import pdb

reader = easyocr.Reader(['hi'])

inpfile = 'csd.png'

res = reader.readtext(inpfile)

breakpoint()
with open('easyocr_csd_outp.txt', 'w+') as outp:
    outp.writelines([repr(l) for l in res])
    

