import sys
sys.path.append('gen-py')

from ThriftAsync import ThriftAsyncServer
from ThriftAsync.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server import TNonblockingServer

class ThriftAsyncHandler:
    
    def add(self, i1, i2):
        """
        Parameters:
         - i1
         - i2
        """
        print 'add called'
        return i1 + i2
        

    def multiply(self, i1, i2):
        """
        Parameters:
         - i1
         - i2
        """
        print 'multiply called'
        return i1 * i2


handler = ThriftAsyncHandler()
processor = ThriftAsyncServer.Processor(handler)
transport = TSocket.TServerSocket(port=9097)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# You could do one of these for a multithreaded server
#server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

# Non-blocking server
#server = TNonblockingServer.TNonblockingServer(processor, transport)

print('Starting the server...')
server.serve()
print('done.')
