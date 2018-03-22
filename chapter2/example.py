#####PYthon Class Example
class myfunctions:
    def addition(x, y):
        return x+y

#>> myfunctions.addition(2, 3)
#5


#python class exmple of using __init__

class atom:
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.position = (x, y, z) 


#python class example of using clas

class exampleFunction:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def incrementByOne(self):
        self.x += 1
        self.y += 1
        self.z += 1
    
    def __repr__(self):
        return ("the value of x, y, z are %d %d %d" % (self.x, self.y, self.z))

#Python Example: Molecule Class

class molecule:
    def __init__(self, name='Generic'):
        self.name = name
        self.atomlist = []
    
    def addatom(self, atom):
        self.atomlist.append(atom)
    
    def __repr__(self):
        str = "This is a molecule named %s\n" % self.name
        str = str + 'It has %d atoms\n' % len(self.atomlist)
        for atom in self.atomlist:
            str = str + ''.join(atom) + '\n'
        return str


if __name__ == "__main__":
    mol = molecule('Water')
    at = atom(8, 0., 0., 0.)
    mol.addatom(at)
    mol.addatom(atom(1, 0., 0., 1.))
    mol.addatom(atom(1, 0., 1., 0.))
    print(mol)