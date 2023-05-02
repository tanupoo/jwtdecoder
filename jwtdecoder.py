#!/usr/bin/env python

import sys
import base64
import json

name_map = {
# JWT Claims
"iss": "Issuer",
"sub": "Subject",
"aud": "Audience",
"exp": "Expiration Time",
"nbf": "Not Before",
"iat": "Issued At",
"jti": "JWT ID",

# JWT Headers
"typ": "Type",
"cty": "Content Type",
"alg": "Algorithm",
}

def jwt_base64url_decode(s: str) -> str:
    return base64.urlsafe_b64decode(s + '='*(-len(s)%4))

def jwt_decode(
        jwt_str: str,
        pos: int=None,
        sig_key: bytes=None,
        verbose: bool=False
        ) -> str:
    def _decode(s: str, pos: int) -> str:
        r = jwt_base64url_decode(s)
        try:
            j = json.loads(r.decode(errors="ignore"))
        except json.decoder.JSONDecodeError as e:
            return r
        else:
            return j
    #
    tidy_str = "".join(jwt_str.split())
    if verbose:
        print(f"Entire Input: {tidy_str}")
    if pos is None:
        ret = []
        for i,s in enumerate(tidy_str.split(".")):
            if verbose:
                print(f"INPUT {i}: {s}")
            ret.append(_decode(s, i))
        return ret
    else:
        s = tidy_str.split(".")[pos]
        if verbose:
            print(f"INPUT {pos}: {s}")
        return [_decode(s, pos)]

def jwt_pprint(jwt_items: str) -> str:
    for v in jwt_items:
        if isinstance(v, bytes):
            print(v.hex())
        else:
            print(json.dumps(v))

if __name__ == "__main__":
    from argparse import ArgumentParser
    from argparse import ArgumentDefaultsHelpFormatter
    ap = ArgumentParser(
            description="JWT decoder.",
            formatter_class=ArgumentDefaultsHelpFormatter)
    ap.add_argument("jwt", nargs="*",
                    help="specify the JWT.")
    ap.add_argument("-s", action="store_true", dest="single_shot",
                    help="specify the input is one JWT.")
    ap.add_argument("-p", action="store", dest="position",
                    type=int, default=None,
                    help="specify the position to print binary mode. "
                    "e.g. -p1 means the header.")
    ap.add_argument("-k", action="store", dest="sig_key",
                    help="specify the key of the signature. "
                        "a string key is supported.")
    ap.add_argument("-v", action="store_true", dest="verbose",
                    help="enable verbose mode.")
    opt = ap.parse_args()
    if opt.jwt:
        for jwt_str in opt.jwt:
            for r in jwt_decode(jwt_str, pos=opt.position,
                                sig_key=opt.sig_key, verbose=opt.verbose):
                jwt_print(r)
    elif opt.single_shot:
        jwt_print(jwt_decode(sys.stdin.read(), pos=opt.position,
                             sig_key=opt.sig_key, verbose=opt.verbose))
    else:
        for jwt_str in sys.stdin:
            r = jwt_decode(jwt_str, pos=opt.position, sig_key=opt.sig_key,
                           verbose=opt.verbose)
            jwt_pprint(r)
