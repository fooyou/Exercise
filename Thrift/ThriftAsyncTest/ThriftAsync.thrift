namespace java com.neusoft.thrift.ThriftAsync
namespace py ThriftAsync
namespace cpp ThriftAsync

typedef i32 int
typedef i64 long

service ThriftAsync {
    long add(1:int i1, 2:int i2)
    long multiply(1:int i1, 2:int i2)
}
