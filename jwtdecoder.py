#!/usr/bin/env python

import sys
import base64

def jwt_base64url_decode(s: str) -> str:
    return base64.urlsafe_b64decode(s + '='*(-len(s)%4))

def jwt_decode(jwt_str: str, pos: int=None, verbose: bool=False):
    tidy_str = jwt_str.replace(" ","").replace("\n","")
    if pos is None:
        ret = []
        for s in tidy_str.strip().split("."):
            if verbose:
                print(f"INPUT: {s}")
            ret.append(jwt_base64url_decode(s).decode(errors="ignore"))
        return ret
    else:
        s = tidy_str.strip().split(".")[pos]
        if verbose:
            print(f"INPUT: {s} at #{pos}")
        return jwt_base64url_decode(s).decode(errors="ignore")

if __name__ == "__main__" :
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
                    help="specify the position to print binary mode."
                    "0 origin")
    ap.add_argument("-v", action="store_true", dest="verbose",
                    help="enable verbose mode.")
    opt = ap.parse_args()
    if opt.jwt:
        for jwt_str in opt.jwt:
            for r in jwt_decode(jwt_str, pos=opt.position, verbose=opt.verbose):
                print(r)
    elif opt.single_shot:
        print(jwt_decode(sys.stdin.read(), pos=opt.position,
                         verbose=opt.verbose))
    else:
        for jwt_str in sys.stdin:
            for r in jwt_decode(jwt_str, pos=opt.position, verbose=opt.verbose):
                print(r)
