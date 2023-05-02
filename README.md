jwtdecoder
==========

A simple JWT decoder.

It can take a JWT string from an argument, or stdin.

```
jwtdecoder.py JWTSTRING
```

```
echo JWTSTRING | jwtdecoder.py
```

A new line charactor is treated as a separator of multiple JWT strings.
So that you can decode some JWTs at one time.

```
cat multiple_jwt_lines.txt | jwtdecoder.py
```

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
