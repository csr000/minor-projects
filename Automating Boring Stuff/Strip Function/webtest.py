import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

class InstanceCounter(object): 
    count = 0                   # class attribute, will be accessible to all instances 
    logging.debug('count: '+str(count))
    def __init__(self, val): 
        self.val = val 
        logging.debug('self.val: '+str(self.val))
       
         # Increment the value of class attribute, accessible through class name 
# In above line, class ('InstanceCounter') act as an object 

 
    def get_count(self): 
        logging.debug('InstanceCounter.count(1): '+str(InstanceCounter.count))
        InstanceCounter.count +=1  
        logging.debug('InstanceCounter.count(2): '+str(InstanceCounter.count))
        return InstanceCounter.count 
a = InstanceCounter(9) 
b = InstanceCounter(18) 
c = InstanceCounter(27) 
 
for obj in (a, b, c): 
   # print ('val of obj: %s' %(obj.get_val()))    # Initialized value ( 9, 18, 27) 
    print ('count: %s' %(obj.get_count()))        # always 3 