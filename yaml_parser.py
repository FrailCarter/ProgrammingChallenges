

import yaml
# Imports a yaml-dictionary into a class

class YamlObject:

    def __init__(self , input_dict):
        self.__dict__.update(dict(self.create_tree(input_dict))) 
    
    def create_tree(self , input_dict):
        for k , v in input_dict.items():
            if isinstance(v , dict):
                yield k , YamlObject(v)
            elif isinstance(v , list):
                yield k , list(self._parse_list(v))
            else:
                yield k , v 
    
    def __getattr__(self , k):
        return self.__dict__[k]
    
    def __setattr__(self , k , v):
        self.__dict__[k] = v 

    def _parse_list(self , input_list):
        for i in input_list:
            if isinstance(i , dict):
                yield YamlObject(i)
            elif isinstance(i , list):
                yield list(self._parse_list(i))
            else:
                yield i 
    
    def _stringify_list(self , selfList):
        for i in selfList:
            if isinstance(i , YamlObject):
                yield dict(i._stringify())
            elif isinstance(i , list):
                yield list(self._stringify_list(i))
            else:
                yield i 
    
    def _stringify(self):
        for k , v in self.__dict__.items():
            if isinstance(v , YamlObject):
                yield k , dict(v._stringify()) 
            elif isinstance(v , list):
                yield k , list(self._stringify_list(v))
            else:
                yield k , v 
    
    def jsonify(self):
        return dict(self._stringify())
    
    def yamlify(self):
        return yaml.dump(self.jsonify())
    
    def get_keys(self):
        return list(self.__dict__.keys())


    
    
