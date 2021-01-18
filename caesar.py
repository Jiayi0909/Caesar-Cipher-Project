#!/usr/bin/env python
# coding: utf-8

# In[42]:


def encrypt(key,plaintext):
    ciphertext=""
    # traverse text 
    for i in range(len(plaintext)): 
        char = plaintext[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            ciphertext += chr((ord(char) + key-65) % 26 + 65)     
    
    return ciphertext


# In[43]:


#check the above function 
key = 1
plaintext = "BASE"
print("Plaintext : " + plaintext)
print("Shift : " + str(key))
print("Cipher: " + encrypt(key,plaintext))


# In[44]:


def decrypt(key,ciphertext):
    plaintext=""
    # traverse text 
    for i in range(len(ciphertext)): 
        char = ciphertext[i] 
  
        # Decrypt uppercase characters 
        if (char.isupper()): 
            plaintext += chr((ord(char) - key-65) % 26 + 65)    
    
    return plaintext


# In[45]:


#check the above function 
key = 1
ciphertext = "CBTF"
print("Ciphertext : " + ciphertext)
print("Shift : " + str(key))
print("Cipher: " + decrypt(key,ciphertext))


# In[ ]:




