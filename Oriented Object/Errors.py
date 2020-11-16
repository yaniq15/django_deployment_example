try:
    f = open("tes.txt", "w")
    f.write("Hello Kimbo")
except IOError:
    print("could not find file")

# else:
#     print("Success ")
#     f.close()

finally:
    print("I ALWAYS WORKS")