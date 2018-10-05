
class CacheException(Exception):
    
    """
    Exceção lançada quando ocorre uma falha ao 
    interagir com o cache.
    """
    def __init__(self, message, code, cause):
        super(CacheException, self).__init__(message)
        self.code  = code    
        self.cause = cause;