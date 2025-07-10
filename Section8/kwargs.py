def marks(**kwargs):
    # kwargs is dictionary with all the key val pairs which are passes to marks..
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")
        
marks(Subhajit=34,souvik=54,suyatra=50,kunduvaipo=90,piyas=89)        