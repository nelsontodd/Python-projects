#  File: TestCipher.py

#  Description: Encodes and decodes text

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Partner Name: -

#  Partner UT EID: -

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 03/26

#  Date Last Modified: 03/31


def substitution_encode ( plainList, cipherList, strng ):
    indices = []
    encodedText =''
    for i in range(len(strng)):
        if strng[i].lower() in plainList:
            indices.append(plainList.index(strng[i].lower()))
        else:
            indices.append(strng[i])
    for i in range(len(indices)):
        if isinstance( indices[i], int ):
            encodedText = encodedText +str(cipherList[indices[i]])
        else:
            encodedText = encodedText +str(indices[i])
    return encodedText
def substitution_decode ( plainList, cipherList, strng ):
    indices = []
    decodedText =''
    for i in range(len(strng)):
        if strng[i] in plainList:
            indices.append(cipherList.index(strng[i]))
        else:
            indices.append(strng[i])
    for i in range(len(indices)):
        if isinstance( indices[i], int ):
            decodedText = decodedText +str(plainList[indices[i]])
        else:
            decodedText = decodedText +str(indices[i])
    return decodedText
def vigenere_encode ( plainList,strng, passwd ):
    indices = []
    encodedText = ''
    rowindices = []
    for i in range(len(strng)): #put all the letters number in the alphabet in a list
        if strng[i].lower() in plainList:
            indices.append(plainList.index(strng[i].lower()))
        else:
            indices.append(strng[i])
    for i in range(len(passwd)): #put all the letters number in the alphabet in a list
        if passwd[i] in plainList:
            rowindices.append(plainList.index(passwd[i].lower()))
        else:
            rowindices.append(passwd[i])
    count = 0
    for i in range(len(indices)):
        if isinstance( indices[i], int ): #if the item is actually an index
            count=count+1
            rowindex = count-1
            if count >= len(rowindices): #This determines the index of the pass phrase letter we are using
                rowindex = (count)%(len(rowindices))
                rowindex = rowindex-1
                #rowindex = (len(rowindices)-1)-rowindex
            vignererow = plainList[:]

            for k in range(rowindices[rowindex]): #Shift down to the row of the passphrase letter
                vignererow = shift(vignererow)

            encodedText = encodedText + vignererow[indices[i]]
        else:
            encodedText = encodedText+str(indices[i])

    return encodedText
def vigenere_decode ( plainList, strng, passwd ):
    indices = []
    decodedText = ''
    rowindices = []

    for i in range(len(strng)):
        if strng[i] in plainList:
            indices.append(plainList.index(strng[i].lower()))
        else:
            indices.append(strng[i])
    for i in range(len(passwd)):
        if passwd[i] in plainList:
            rowindices.append(plainList.index(passwd[i].lower()))
        else:
            rowindices.append(passwd[i])
    count = 0
    for i in range(len(indices)):
        if isinstance( indices[i], int ): #if the item is actually an index
            count=count+1
            rowindex = count-1
            if count > len(rowindices): #This determines the index of the pass phrase letter we are using
                rowindex = (count)%(len(rowindices))
                rowindex = rowindex-1
            
                #rowindex = (len(rowindices)-1)-rowindex
            vignererow = plainList[:]

            for k in range(rowindices[rowindex]): #Shift down to the row of the pass phrase letter
                vignererow = shiftback(vignererow)

            decodedText = decodedText + vignererow[indices[i]]
        else:
            decodedText = decodedText+str(indices[i]) #Add the character in

    return decodedText
def shift ( shiftList ): #This shifts the alphabet over 1 index
    first = shiftList[0]
    temp = shiftList[:]
    for i in range(len(temp)-1,0,-1):
        shiftList[i-1] = temp[i]
    shiftList[len(shiftList)-1] = first
    return shiftList
def shiftback ( shiftList ): #This shifts the alphabet over the other way
    last = shiftList[len(shiftList)-1]
    temp = shiftList[:]
    for i in range(len(temp)-1):
        shiftList[i+1] = temp[i]
    shiftList[0] = last
    return shiftList
def main():
  # open file for reading
  cipherList = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u']
  cipherList.append('j')
  cipherList.append('m')
  cipherList.append('i')
  cipherList.append('k')
  cipherList.append('o')
  cipherList.append('l')
  cipherList.append('p')
  plainList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
  plainList.append('x')
  plainList.append('y')
  plainList.append('z')
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print (' ')

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (plainList, cipherList,line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print (' ')

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (plainList, cipherList, line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print (' ')

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print (' ')

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (plainList,line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print (' ')

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (plainList,line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print (' ')

  # close file
  in_file.close()

main()
