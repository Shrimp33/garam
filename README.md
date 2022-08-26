# Garam, for arrays too big for memory    
## A dictionary / list that is stored on the disk for ram intensive operations.
<br/>

# Construction
## ``` def __init__(self, path, mode='binary', save=True): ```  
<br/>

## Path  
### Prettly self explanatory, where to load and store elements of the garam instance.
## Mode 
### The default mode stores and reads elements as pickled files   
 ``` mode='binary' ```  
### Mode text stores and reads the elements as strings in a text file  
``` mode='text' ```  
## Save  
<h3 style="color:orange">Warning: this moudle uses rmtree to clear the directory at deconstuction when save=False, so all files in the path set at construction will be lost. Please use save=True unless you are sure that there are no important files left on the path.</h3>

### Saves the stored elements on disk (Default)
```save=True```  
### Deletes everything in the path set on construction 
``` save=False ```  
<br/>

# Examples  
## Excerpts are from test.py

```
# First and Foremost
import garam
```

### Testing the mode binary
```
def bintest():  # Test binary mode
    # Create garam instance at path
    p = garam('path', save=False)

    # Test usings strings as keys
    p['test'] = 'test'
    assert p['test'] == 'test'
    print("bintest 1 passed")

    # Test stacking 
    p['test1']['test2'] = 'test3'
    assert p['test1']['test2'] == 'test3'
    print("bintest 2 passed")

    # Test usings ints as keys
    p[0] = '000'
    assert p[0] == '000'
    print("bintest 3 passed")

    # Test stacking 
    p[1][2] = '111'
    assert p[1][2] == '111'
    print("bintest 4 passed")

    print("all bintests passed")
```
### Testing mode text  
```
def texttest():  # Test text mode
    # Create garam instance at path
    p = garam('path', mode='text', save=False)

        # Test usings strings as keys
    p['test'] = 'test'
    assert p['test'] == 'test'
    print("texttest 1 passed")

    # Test stacking 
    p['test1']['test2'] = 'test3'
    assert p['test1']['test2'] == 'test3'
    print("texttest 2 passed")

    # Test usings ints as keys
    p[0] = '000'
    assert p[0] == '000'
    print("texttest 3 passed")

    # Test stacking 
    p[1][2] = '111'
    assert p[1][2] == '111'
    print("texttest 4 passed")

    print("all texttests passed")
    

```