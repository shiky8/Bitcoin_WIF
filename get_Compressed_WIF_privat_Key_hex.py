import binascii, hashlib, base58, sys
arq = open('WIF_founds_list.txt', 'w')

def convert(z):

    private_key_static = z

    extended_key = "80"+private_key_static+"01"

    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()

    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()

    final_key = extended_key+second_sha256[:8]

    WIF = base58.b58encode(binascii.unhexlify(final_key)).decode ('ascii')

    print ("Private Key on WIF Compressed format below")
    print (WIF)
    arq.write("%s \n" % WIF)

with open("hex_private_key_list.txt") as file:
    for line in file:
        print (str.strip(line))
        convert(str.strip(line))
