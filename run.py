
# coding: utf-8

# In[3]:


def cleaning():
    t = input('Please write name of the file: ')
    f = open(t, 'r')
    out = open('output.txt','w')
    for line in f:
        l = line.replace(',','').replace('.','').replace('  ',' ').lower()
        out.write(l)
    f.close()
    out.close()
    return print('\nYour file was proceeded and saved as output.txt')


# In[4]:


cleaning()

