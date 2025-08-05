print("insula comorii")
prima = input("in ce parte o iei Stanga sau dreapta ").lower()
doi = input("alearga sau inoata").lower()
trei = input("albastru,galben,rosu,negru").lower()
if prima == "stanga":
     if doi == "inoata":
         print("mancat de testoasa")
         if trei == "negru":
             print("mort")
     elif trei == "rosu":
        print("cox")
else :
    print("mort")