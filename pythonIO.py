# To Read the entire file conent
'''
f=open('test.txt','r') 
            
f_contents = f.read()
print(f_contents)
   '''
#To Read the text from file for specified size
'''
   size_to_read = 5
   f_contents = f.read(size_to_read)
   while(len(f_contents) > 0):
                print(f_contents,end='\n')
                f_contents = f.read(size_to_read)
                '''
#To Write the text from .txt file  (creats new file)
'''
with open('test11.txt','w') as f:
             f.write('tester one ')
             '''
#To write the text for existing file
'''
f= open('test.txt','a') 
f.write('tester adding the texxt ')
f.close()
f=open('test.txt','r')             
print(f.read())
'''

