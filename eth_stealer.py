
https://github.com/pulls
from ecdsa import SigningKey, SECP256k1
import sha3
from ethplorer.address import Address

i=0xA9250218933909c222e2aaA6a963f5DEa2aF1cEb

while True:
    #Code taken from Vincent Kobel. License at: https://github.com/vkobel/ethereum-generate-wallet/blob/master/LICENSE.md
    keccak = sha3.keccak_256()
    
    priv = SigningKey.generate(curve=SECP256k1)
    
    pub = priv.get_verifying_key().to_string()
        
    keccak.update(pub)
    address = keccak.hexdigest()[24:]
    address = '0x' + address
    #End of attributed code
    
    ADD = Address(address = address)
    
    info = ADD.get_address_info()
    #print(priv.to_string().hex(), address, info['ETH'])
    try:
        if info['ETH']['balance'] != 0:
            print(priv.to_string().hex(), address, info['ETH'])
    except:
        print('An error occured')

    if (i % 100) == 0:
        print(i)
    i=i+1

    
"""MIT License
Copyright (c) 2018 Vincent Kobel
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""
MIT License
Copyright (c) 2018 Milind Bansia
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
