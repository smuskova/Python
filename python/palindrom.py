def daliEpalindrom(n):
    if n==n[::-1]:
        return int(True)
    else:
       return int(False)

print(daliEpalindrom(n=input()))
