import weka.core.jvm as jvm
jvm.start()

jvm.start(system_cp=True, packages=True)
jvm.start(packages="/usr/local/lib/python2.7/dist-packages/weka")

jvm.start(max_heap_size="512m")

data_dir="CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING"


from  weka.classifiers  import  Classifier 
cls = Classifier(classname="weka.classifiers.trees.J48")
cls.options = ["-C", "0.3"]
print(cls.options)


jvm.stop()
