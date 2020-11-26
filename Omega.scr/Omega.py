import sys

class Start:
    def __init__(self):
        self.openfile = open(sys.argv[1])
        self.opl = self.openfile.readlines()
        self.funcs = []
        self.openfile.close()
    
    def run(self):
        for line in self.opl:
            line1 = "".join(line).split();line1 = "".join(line1)
            if line1.startswith("func"):
                function=line1.replace("func", "")
                Omega1().run(function)
            
            elif line1.startswith("def"):
                self.deffunc = line1.replace("def", "").replace("{", "")

class Omega1:
    def __init__(self):
        self.setopf = open("set.oms", "w")
        self.opf = open(sys.argv[1])
        self.read = self.opf.read()
        self.opf.close()
    
    def run(self, function):
        read = self.read.split("\n")
        read = "".join(read).split()
        try:
            read = "".join(read).split(function+"{")[1]
            read = "".join(read).split("end")[0]
            re = Omega2(function, read).run()
            OmegaMain(Omega3(re).run()).run()
        except IndexError:
            #TODO:NotFoundFuncErr
            print("NotFoundFuncErr: {}が見つかりません".format(function))
            sys.exit()

class Omega2:
    def __init__(self, func, vart):
        self.func = func
        self.vart = vart
    
    def run(self):
        self.vart = "".join(self.vart).split()
        self.vart = "".join(self.vart)
        self.vart = "".join(self.vart).replace("[", "").replace("]", "").replace("'", "")#.replace(";", "\n")
        self.vart = self.vart.split()
        self.vart = "".join(self.vart)
        return self.vart

class Omega3:
    def __init__(self, list_a):
        self.funcdata = list_a.split(";")
    def run(self):
        return self.funcdata

class OmegaMain:
    def __init__(self, function):
        self.f = function
        self.dic1 = {}
        self.func = {}
    def run(self):
        for i in range(len(self.f)):
            line = self.f[i]
            line = line.split("//")[0]
            if "print" and '"' in line:
                    pr = line.replace("print", "").replace("{", "").replace("}", "").replace('"', "").replace(";", "")
                    print(pr)
            #TODO:変数の定義
            elif line.startswith("int") or line.startswith("str"):
                self.var = line.replace('\n', "")
                varname = self.var.split("=")[0]#変数名
                if line.startswith("int"):
                    try:
                        #TODO:int型の要素
                        self.ele = eval(self.var.split("=")[-1].replace("int", ""))

                    except NameError:
                        print("Err: NameErr")
                        self.ele = "Not int"
                
                elif line.startswith("str"):
                    self.ele = self.var.split("=")[-1].replace("str", "")#int型の要素
                self.dic1[varname] = self.ele
            
            #引数に変数を指定するprint
            elif "print" in line:
                line = line.replace("print", "").replace("{", "").replace("}", "").replace("\n", "").replace(";", "")
                try:
                    print(self.dic1[line])
                except KeyError:
                    print("変数名{}が見つかりません".format(line[3:]))
                    sys.exit()

            elif line in "\n":
                pass


def main():
    Start().run()

if __name__ == '__main__':
    main()
