from calypte.calypte_connection_imp import CalypteConnectionImp;
from calypte.cache_exception import CacheException
from calypte.calypte_connection_proxy import CalypteConnectionProxy;
from threading import Lock;
import Queue
from queue import Empty
from queue import Full

class ClaypteConnectionPool(object):
    
    def __init__(self, host, port, minInstances, maxInstances):
        self.host             = host
        self.port             = port
        self.minInstances     = minInstances
        self.maxInstances     = maxInstances
        self.lock             = Lock()
        self.instances        = Queue.Queue()
        self.createdInstances = 0
        
        if minInstances < 0:
            raise CacheException("minInstances")
        
        if maxInstances < 1:
            raise CacheException("maxInstances")
        
        if minInstances > maxInstances:
            raise CacheException("minInstances");
        
    def get_connection(self):
        """
        Obtém uma conexão.
        @return: Conexão.
        @throws CacheException: Lançada se ocorrer uma falha ao tentar 
        recuperar ou criar uma conexão.
        """
        
        try:
            con = self.instances.get_nowait()
            
            if con != None:
                return self.__create_proxy(con);
            else:
                lock.acquire()
                try:
                    if self.createdInstances < self.maxInstances:
                        con =  __create_connection(self.host, self.port)
                        self.createdInstances += 1
                        return con;
                    
                finally:
                    lock.release()
                    
                return self.instances.get()
            
        except Exception as e:
            raise CacheException(e);
        

    def try_get_connection(self, timeout):
        """
        Tenta obter uma conexão.
        @return: Conexão.
        @throws CacheException: Lançada se ocorrer uma falha ao tentar 
        recuperar ou criar uma conexão.
        """
        
        try:
            try:
                con = self.instances.get(True, timeout)
                self.instances.task_done()
            except Empty as e:
                self.instances.task_done()
                lock.acquire()
                try:
                    if self.createdInstances < self.maxInstances:
                        con =  __create_connection(self.host, self.port)
                        self.createdInstances += 1
                        return con;
                    
                finally:
                    lock.release()
                    
                con = self.instances.get()
                self.instances.task_done()
                return con
        except Exception as e:
            raise CacheException(e);
        
    
    def release(self,con):
        """
        Libera o uso da conexão.
        @param con: Conexão.
        """
        
        try:
            self.instances.put(con)
            self.instances.task_done()
        except Full:
            self.instances.task_done()
            self.shutdown(con)
            

    def shutdown(self,con):
        """
        Remove a conexão do pool e libera o espaço para ser criada uma nova.
        @param con: Conexão.
        """
        
        lock.acquire()
        try:
            con.close()
        finally:
            self.createdInstances-= 1;
            lock.release()

    def shutdown(self):
        """
        Destrói o pool de conexões.
        """
        pass
    
    # métodos privados
            
    def __create_connection(self, host, port):
        con = CalypteConnectionImp(host, port)
        con.connect()
        return con

    def __getinstance(self):
        pass

    def __create_proxy(self, con):
        return CalypteConnectionProxy(con, self)