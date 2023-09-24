from mockito import when, mock, unstub
from expects import *
from mamba import description, context, it
import src.cnd_cr_object as cnd_cr_object
import tests.vars as vars


with description("CrObject") as self:
    with before.each:
        unstub()
        self.cnd_cr_object = cnd_cr_object.CrObject(vars._print)
        
    with context('__init__'):
        with it('should set _print'):
            expect(self.cnd_cr_object._print).to(equal(vars._print))
            
    with context('create'):
        with it('should return True is create success'):
            result = self.cnd_cr_object.create()
            expect(result).to(equal(True))
            
    with context('all'):
        with it('should all object'):
            result = cnd_cr_object.CrObject.all(vars._print)
            expect(isinstance(result, list)).to(equal(True))
            expect(isinstance(result[0], cnd_cr_object.CrObject)).to(equal(True))
            
    with context('find_by_id'):
        with it('should find_by_id object'):
            result = cnd_cr_object.CrObject.find_by_id(vars._id, vars._print)
            expect(isinstance(result, cnd_cr_object.CrObject)).to(equal(True))
            
    with context('update'):
        with it('should update object'):
            result = self.cnd_cr_object.update({})
            expect(result).to(equal(True))
 
    with context('destroy'):
        with it('should destroy object if object is found'):
            result = self.cnd_cr_object.destroy()
            expect(result).to(equal(True))
 
    with context('has_children'):
        with it('should return has_children object'):
            result = self.cnd_cr_object.has_children()
            expect(result).to(equal(True))
 
    with context('find_relation'):
        with it('should return find_relation object'):
            result = self.cnd_cr_object.find_relation()
            expect(result).to(equal(True))
            
