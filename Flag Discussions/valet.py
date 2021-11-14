from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode

secret_key = b64decode(b'a4a2NVT6e5dKPCDOt21gZECjZ8hjgNritmHwzD+qKFk=')
initialisation_vector = b'\xddS\xa0O\xf0\xd8?\x88\xb7\xce\xc6g'
encrypted_password = b'w\x06\xa2\xe7\xb5\xe3\xbd2{V\x03\xeaU\x8d\x9a\x93\x01\xf2\xae\x95\xaa\xba\x12\xf8\x18-I{;9cZ\xac\xd8t/\xbd\x95\xcb\x0e>\xf3\xde\n\x8c\xe3/\x8a;\x83\xaf\xf7rfS\xa9\xca\x99\xe2~\r\xaf9\xbc,\x95'

cipher = AES.new(secret_key, AES.MODE_GCM, initialisation_vector)
decrypted_pass = cipher.decrypt(encrypted_password)
decrypted_pass.decode()

# 'flag{57555e23cf996b6fbcb667a1b541c52c_thE_VAl3t_H@S_bEst_$ECURi7y}'
