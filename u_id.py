'''
Author : Mahesh Narayana
Date : 12/12/2016
This algorithm will generate 56 charter UUID  example : 133a2bb-5cbf19f2-dfdf-588e-a169-06e2807481ce-a84aaf543bb
Algorithm use python Universally Unique Identifiers UUID5 to generate a random UUID. A UUID is simply a 128-bit value. 
The meaning of each bit is defined by any of several variants. For human-readable display, many systems use a canonical format 
using hexadecimal text with inserted hyphen characters. For example: 123e4567-e89b-12d3-a456-426655440000
This alogrteim use UUID5, UUID5 using a SHA-1 hash of a namespace UUID and a name

SHA: The Secure Hash Algorithm is a family of cryptographic hash functions published by 
the National Institute of Standards and Technology (NIST) as a U.S. Federal Information Processing Standard

SHA-1: A 160-bit hash function which resembles the earlier MD5 algorithm. 
This was designed by the National Security Agency (NSA) to be part of the Digital Signature Algorithm. 

The algorithm will get today date YYYYMMDD and Time HMSMS , Then converted to hex decimal.
0x part of hex date and time is striped and connncatenated to UUID5 to avoid hash collisions in UUID generation.

UUID5 using a SHA-1 hash of a namespace UUID and a name , name can be made futher unique based on system of source record.


'''
import uuid
import datetime
import time
def u_id():
    today = datetime.date.today()
    tm = (time.strftime("%H%M%S%F"))
    u_id = hex(int(today.strftime('%Y%m%d'))) + '-'+ str(uuid.uuid5(uuid.NAMESPACE_DNS, 'WRS')) + '-' + hex(int(tm.replace("-","")))
    print u_id.replace("0x", "")
if __name__ == "__main__":
    u_id()
