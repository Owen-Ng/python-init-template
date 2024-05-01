# Init python application
1.
```python3 -m venv venv```
2. 
## Activate Virtual Environment
``` source venv/bin/activate ```

## Deactivate Virtual Environment
``` deactivate ```
3.
## Install necessary packages
```pip install -r requirements.txt```

## Appendix
PUT <key> <value> O(1)
store the key in memory with value
If it is already exist we want to increment the version of that value

GET <Key> O(1)
Want to return the latest value

GET <Key> <Version> O(log n)
want return value of that specific version

<!-- k 1  v0
k 2  v1 -->

hm h1 store the key to an hahsmap h2

h2 will be key : version value: value

How do I know which version is there?

<!-- hm key: key value a list [values] the first version will always be one.

key1 [5,7] -->

hm key : key the value will be Innerhm

InnerHm: key is version value is value

hm key: key value : latest value

a single variable the latest value

log n
[[version, value], [version,value]]
arr[-1]
O(1)


# bisect_right

we return the index that is greater than the value that is passed
2 3

return 0 - 1
