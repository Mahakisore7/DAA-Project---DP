def lcs_rec(str1, str2):
   
    if not str1 or not str2:
        return 0
    
    if str1[-1] == str2[-1]:
        return 1 + lcs_rec(str1[:-1], str2[:-1])
    else:
        ans1 = lcs_rec(str1[:-1], str2)
        ans2 = lcs_rec(str1, str2[:-1])
        return max(ans1, ans2)

if __name__ == "__main__":
    str1 = "acbcd"
    str2 = "abed"

    print(lcs_rec(str1, str2))