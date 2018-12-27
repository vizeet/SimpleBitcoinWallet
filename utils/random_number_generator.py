import random
import hashlib
import binascii
import ossaudiodev

def getRawMicOutput():
	dsp = ossaudiodev.open('/dev/dsp1', 'r')
	audio = dsp.read(1280)
	return audio

#def getRandomNumber():
#        return random.SystemRandom().getrandbits(256)

def getRandomNumberBits(bit_count: int):
        h = hashlib.sha256()

        # update with raw mic output
        raw_sound = getRawMicOutput()
        print('raw sound = %s' % bytes.decode(binascii.hexlify(raw_sound)))
        h.update(raw_sound)

        # update with system random number
        sys_rand = '%x' % random.SystemRandom().randrange(0, 1 << 32)
        sys_rand_b = binascii.unhexlify(sys_rand)
        h.update(sys_rand_b)

        h_b = h.digest()
        byte_count = bit_count // 8
        rand_num_b = h_b[0:byte_count]
        return rand_num_b

if __name__ == '__main__':
        print('random number = %s' % bytes.decode(binascii.hexlify(getRandomNumberBits(256))))
