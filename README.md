jwtdecoder
==========

A simple JWT decoder.

There are two ways to decode JWTs.

```
jwtdecoder.py JWTSTRING
```

```
echo JWTSTRING | jwtdecoder.py
```

```
cat | jwtdecoder.py -s
```

in the 3rd way, copy and paste JWTSTRING to the terminal at once.

## examples

```
% jwtdecoder.py eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9
{"typ":"JWT",
 "alg":"HS256"}
```

```
% echo eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ | ./jwtdecoder.py 
{"alg":"HS512","typ":"JWT"}
{"sub":"1234567890","name":"John Doe","iat":1516239022}
```
