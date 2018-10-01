from socket import socket;
import abc;

class ClaypteConnection(object):
    """
    Permite o armazenamento, atualização, remoção de um item no Calypte.
    """
    
    def __init__(self, host, port):
        
        self.host = host;
        self.port = port;
        self.sock     = socket.socket(
                            socket.AF_INET, 
                            socket.SOCK_STREAM);
        self.sock.connect((self.host, self.port));
        
    @abc.abstractmethod
    def close(self):
        """
        Fecha a conexão com o servidor.
        @raise CacheException:  Lançada caso ocorra alguma falha ao tentar fechar a conexão com o servidor.
        """
        pass
    
    @abc.abstractmethod
    def closed(self):
        """
        Verifica se a conexão está fechada.
        @return: true se a conexão está fechada. Caso contrátio, false.
        """
        pass
    
    #métodos de coleta
    
    @abc.abstractmethod
    def replace(self,key,value,timeToLive, timeToIdle):
        """
            Substitui o valor associado à chave somente se ele existir.
            @param key:  chave associada ao valor.
            @param value: valor para ser associado à chave.
            @param timeToLive: é a quantidade máxima de tempo que um item expira após sua criação.
            @param timeToIdle: é a quantidade máxima de tempo que um item expira após o último acesso.
            @return: true se o valor for substituido. Caso contrário, false.
            @raise CacheException: Lançada se ocorrer alguma falha com o servidor.
         """
        pass
        
    
    @abc.abstractmethod
    def replace_value(self, key, oldValue, newValue, timeToLive, timeToIdle):
        """
            Substitui o valor associado à chave somente se ele for igual a um determinado valor.
            @param key: chave associada ao valor.
            @param oldValue: valor esperado associado à chave.
            @param newValue: valor para ser associado à chave.
            @param timeToLive: é a quantidade máxima de tempo que um item expira após sua criação.
            @param timeToIdle: é a quantidade máxima de tempo que um item expira após o último acesso.
            @return: true se o valor for substituido. Caso contrário, false.
            @throws CacheException: Lançada se ocorrer alguma falha com o servidor.
        """
        pass
    
    @abc.abstractmethod
    def put_if_absent(self, key, value, timeToLive, timeToIdle):
        """
        Associa o valor à chave somente se a chave não estiver associada a um valor.
        @param key: chave associada ao valor.
        @param value: valor para ser associado à chave.
        @param timeToLive: é a quantidade máxima de tempo que um item expira após sua criação.
        @param timeToIdle: é a quantidade máxima de tempo que um item expira após o último acesso.
        @return: anterior associado à chave.
        @raise CacheException: Lançada se ocorrer alguma falha com o servidor.
        """
        pass
    
    @abc.abstractmethod
    def set(self, key, value, timeToLive, timeToIdle):
        """
        Associa o valor à chave somente se a chave não estiver associada a um valor.
        @param key chave associada ao valor.
        @param value valor para ser associado à chave.
        @param timeToLive é a quantidade máxima de tempo que um item expira após sua criação.
        @param timeToIdle é a quantidade máxima de tempo que um item expira após o último acesso.
        @return true se o valor for substituído. Caso contrário, false.
        @raise CacheException: Lançada se ocorrer alguma falha com o servidor.
        """
        pass
    
    @abc.abstractmethod
    def put(self, key, value, timeToLive, timeToIdle):
        """
        Associa o valor à chave.
        @param key: chave associada ao valor.
        @param value: valor para ser associado à chave.
        @param timeToLive: é a quantidade máxima de tempo que um item expira após sua criação.
        @param timeToIdle: é a quantidade máxima de tempo que um item expira após o último acesso.
        @return : true se o item for substituido. Caso contrário, false
        @raise CacheException: Lançada se ocorrer alguma falha com o servidor.
        """
        pass
    
    @abc.abstractmethod
    def get(self, key, forUpdate=False):
        """
        Obtém o valor associado à chave bloqueando ou não 
        seu acesso as demais transações.
        @param key: chave associada ao valor.
        @param forUpdate: true para bloquear o item. Caso contrário false.
        @return valor: associado à chave ou <code>null</code>.
        @raise CacheException: Lançada se ocorrer alguma falha com o servidor.
        """
        pass
    
    # métodos de remoção
    
    @abc.abstractmethod
    def remove(self,key,value=None):
        """
        Remove o valor assoiado à chave somente se ele for igual a um determinado valor.
        @param key chave associada ao valor.
        @param value valor associado à chave.
        @return <code>true</code> se o valor for removido. Caso contrário, <code>false</code>.
        @throws CacheException Lançada se ocorrer alguma falha com o servidor.
        """
        pass
    
    @abc.abstractmethod
    def set_auto_commit(self,value):
        """
        Define o modo de confirmação automática. Se o modo de confirmação automática
        estiver ligado, todas as operações serão tratadas como transações individuais. Caso contrário,
        as operações serão agrupadas em uma transação que deve ser confirmada com o método {@link #commit()} ou
        descartadas com o método {@link #rollback()}. Por padrão, cada nova conexão inicia com o 
        modo de confirmação automática ligada. 
        @param value: true para ligar o modo de confirmação automática. Caso contrário, false. 
        @raise CacheException: Lançada se o estado desejado já estiver em vigor ou se a conexão estiver fechada.
        """
        pass
    
    @abc.abstractmethod
    def auto_commit(self):
        """
        Obtém o estado atual do modo de confirmação automática.
        @return true se o modo de confirmação automática estiver ligado. Caso contrário, false.
        @throws CacheException: Lançada se ocorrer alguma falha com o servidor ou se a conexão estiver fechada.
        """
        pass
    
    @abc.abstractmethod
    def commit(self):
        """
        Confirma todas as operações da transação atual e libera todos os bloqueios detidos por essa conexão.
        @throws CacheException: Lançada se ocorrer alguma falha com o servidor, se a conexão estiver fechada ou se o
        modo de confirmação automática estiver ligada.
        """
        pass
    
    @abc.abstractmethod
    def rollback(self):
        """
        Desfaz todas as operações da transação atual e libera todos os bloqueios detidos por essa conexão.
        @throws CacheException: Lançada se ocorrer alguma falha com o servidor, se a conexão estiver fechada ou se o
        modo de confirmação automática estiver ligada.
        """
        pass

    @abc.abstractmethod
    def flush(self):
        """
        Limpa o cache.
        @throws CacheException: Lançado se ocorrer alguma falha ao tentar limpar o cache.
        """
        pass
    
    @abc.abstractmethod
    def host(self):
        """
        Obtém o endereço do servidor.
        @return: Endereço do servidor.
        """
        pass

    @abc.abstractmethod
    def port(self):
        """
        Obtém a porta do servidor.
        @return: Porta do servidor.
        """
        pass
        
