class nomina:
    def afp(self, sb):
        return sb * 0.07
    
    def ars(self, sb):
        return sb * 0.02
    def totaldesc(self,afp,ars):
        return afp + ars
    
    def sueldoneto (self,sb,td):
        return sb - td 
    
    
n = nomina ()
sueldo =float(input("entre sueldo base: "))
afp = n.afp(sueldo)
ars = n.ars(sueldo)
descuentos=n.totaldesc(afp,ars)
sn = n.sueldoneto (sueldo,descuentos)

print ("afp             : (:0.2f)".format(afp))
print ("afp             : (:0.2f)".format(ars))
print ("descuentos      : (:0.2f)".format(descuentos))
print ("sueldo neto     : (:0.2f)".format(sn))
