import re
class ParseError(RuntimeError):
    pass

class Parser:
    
    def __init__(self):
        self.elements = []
        self.regelems = {}
    
    def addelems(self, *args):
        self.elements += list(args)
        self.elements = sorted(self.elements, key=len, reverse=True)
        
    def setregelems(self, **kwargs):
        self.regelems = kwargs
        
    def parse(self, string):
        try: 
            temp = []
            parse = string
            while parse:
                switch = True
                switch2 = True
                for x in self.regelems:
                    if (found := self.regelems[x].match(parse)):
                        temp.append({x:found.group(0)})
                        parse = parse[len(found.group(0)):]
                        switch = False
                        switch2 = False
                        break
                        
                if switch:
                    for x in self.elements:
                        if re.match(x,parse):
                            temp.append(x)
                            parse = parse[len(x):]
                            switch2 = False
                            break
                            
                if switch2:
                    raise ParseError(f"An invalid token was found when the remaining string was '{parse}' .")
                    
            return temp
        except BaseException as e:
            raise ParseError(f"An error occured while parsing '{string}':\n {e}")
            

if __name__ == "__main__":
    try:
        import re
        tester = Parser()
        tester.setregelems(string = re.compile(r'".*"'),num = re.compile(r"\d+"))
        tester.addelems('a','b','c','ba')
        assert tester.parse('aabbaacabbbaacccc1559372cccca4432baacccccc"string"acb4332453253253bc') == ['a', 'a', 'b', 'ba', 'a', 'c', 'a', 'b', 'b', 'ba', 'a', 'c', 'c', 'c', 'c', {'num': '1559372'}, 'c', 'c', 'c', 'c', 'a', {'num': '4432'}, 'ba', 'a', 'c', 'c', 'c', 'c', 'c', 'c', {'string': '"string"'}, 'a', 'c', 'b', {'num': '4332453253253'}, 'b', 'c']
        print("Test successful!")
    except AssertionError:
        print("Test failed.")
    except BaseException as e:
        print(f"Error:\n{e}")
