def result(math,oe,ade,oops,ds,itpm)->str:
    if math+oe+ade+oops+ds+itpm >40:
        return "Pass"
    
    else:
        return "Fail"
subjects={
    "math":20,
    "oe":16,
    "ade":17,
    "oops":18,
    "ds":18,
    "itpm":19
}
print(result(**subjects))